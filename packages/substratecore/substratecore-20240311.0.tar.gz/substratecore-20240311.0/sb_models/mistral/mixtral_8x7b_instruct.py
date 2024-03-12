import os
import time
from typing import Optional

from modal import Dict, Stub, Image, Secret, Function, gpu, method, web_endpoint
from fastapi import Header, HTTPException

from sb_models.hash import hash_args
from sb_models.logger import log
from sb_models.types.outputs import TextCompletion, TextGeneration
from sb_models.types.request import SubstrateRequest, TextGenerationArgs
from sb_models.types.response import SuccessResponse

MODEL_DIR = "/model"
BASE_MODEL = "mistralai/Mixtral-8x7B-Instruct-v0.1"
GPU_COUNT = 2
GPU = gpu.A100(memory=80, count=GPU_COUNT)
DEFAULT_MAX_TOKENS = 888


def download_model():
    from huggingface_hub import snapshot_download
    from transformers.utils import move_cache

    os.makedirs(MODEL_DIR, exist_ok=True)

    snapshot_download(
        BASE_MODEL,
        local_dir=MODEL_DIR,
        ignore_patterns="*.pt",  # Use safetensors
    )
    move_cache()


image = (
    Image.from_registry("nvcr.io/nvidia/pytorch:23.10-py3")
    .pip_install("torch==2.1.1")
    .pip_install("hf-transfer==0.1.4", "huggingface_hub")
    .env({"HF_HUB_ENABLE_HF_TRANSFER": "1"})
    .apt_install("git")
    .pip_install("git+https://github.com/stanford-futuredata/megablocks.git", gpu="any")
    .run_commands(
        "pip install https://github.com/vllm-project/vllm/releases/download/v0.2.6/vllm-0.2.6-cp310-cp310-manylinux1_x86_64.whl",
        gpu="any",
    )
    .run_function(
        download_model,
        secret=Secret.from_name("huggingface-secret", environment_name="main"),
        timeout=60 * 10,
    )
)

stub = Stub("mixtral-8x7b-instruct", image=image)
stub.cache = Dict.new()
TEMPLATE = """<s> [INST] {user} [/INST] """


@stub.cls(
    gpu=GPU,
    secret=Secret.from_name("huggingface-secret", environment_name="main"),
    container_idle_timeout=60 * 10,
    concurrency_limit=1,
    timeout=60 * 10,
)
class Mixtral:
    def __enter__(self):
        from vllm import LLM

        if GPU.count > 1:
            # Patch issue from https://github.com/vllm-project/vllm/issues/1116
            import ray

            ray.shutdown()
            ray.init(num_gpus=GPU.count)

        self.llm = LLM(MODEL_DIR, gpu_memory_utilization=0.9, tensor_parallel_size=GPU_COUNT)

        self.template = "<s> [INST] {user} [/INST] "

        # Performance improvement from https://github.com/vllm-project/vllm/issues/2073#issuecomment-1853422529
        if GPU.count > 1:
            import subprocess

            RAY_CORE_PIN_OVERRIDE = "cpuid=0 ; for pid in $(ps xo '%p %c' | grep ray:: | awk '{print $1;}') ; do taskset -cp $cpuid $pid ; cpuid=$(($cpuid + 1)) ; done"
            subprocess.call(RAY_CORE_PIN_OVERRIDE, shell=True)

    @method()
    def generate(
        self,
        input_prompts,
        system="",
        n: int = 1,
        presence_penalty: float = 1.1,
        frequency_penalty: float = 0.0,
        repetition_penalty: float = 1.0,
        temperature: float = 0.75,
        top_p: float = 1.0,
        max_tokens: int = DEFAULT_MAX_TOKENS,
        req: Optional[SubstrateRequest] = None,
    ) -> TextGeneration:
        from vllm import SamplingParams

        if isinstance(input_prompts, str):
            input_prompts = [input_prompts]

        cache_key = hash_args(*input_prompts, str(n), str(temperature), str(max_tokens))
        if cache_key in stub.cache:
            log.info(f"Cache hit for {cache_key}")
            return stub.cache[cache_key]

        t0 = time.time()
        prompts = [self.template.format(user=q) for q in input_prompts]

        sampling_params = SamplingParams(
            presence_penalty=presence_penalty,
            frequency_penalty=frequency_penalty,
            repetition_penalty=repetition_penalty,
            temperature=temperature,
            top_p=top_p,
            max_tokens=max_tokens or DEFAULT_MAX_TOKENS,
            n=n,
        )
        outputs = self.llm.generate(prompts, sampling_params)
        # TODO(rob): this should be organized by prompt, returning a list
        completions = [
            TextCompletion(text=output.text, token_count=len(output.token_ids)) for o in outputs for output in o.outputs
        ]
        total_tokens = sum([len(o.outputs[0].token_ids) for o in outputs])
        log.info(f"Generated {total_tokens} tokens in {time.time() - t0:.2f}s")
        res = TextGeneration(completions=completions, token_count=total_tokens)
        stub.cache[cache_key] = res
        return res


@stub.function(secrets=[Secret.from_name("api-secret-key", environment_name="main")])
@web_endpoint(method="POST")
async def api(
    args: TextGenerationArgs,
    x_proxy_path: str = Header(None),
    x_organization_id: str = Header(None),
    x_user_id: str = Header(None),
    x_modal_secret: str = Header(None),
) -> SuccessResponse[TextGeneration]:
    secret = os.environ["API_SECRET_KEY"]

    if secret and x_modal_secret != secret:
        raise HTTPException(status_code=401, detail={"error": "Not authorized"})

    if not x_user_id and not x_organization_id:
        raise HTTPException(status_code=401, detail={"error": "Not authorized"})
    if not x_proxy_path:
        raise HTTPException(status_code=400, detail={"error": "Invalid request"})

    if not args.prompts and not args.prompt:
        raise HTTPException(
            status_code=400,
            detail={"error": "Must provide a prompt or list of prompts"},
        )

    if args.prompts and args.prompt:
        raise HTTPException(
            status_code=400,
            detail={"error": "Must provide a prompt or list of prompts, not both"},
        )

    prompts = args.prompts
    if args.prompt:
        prompts = [args.prompt]

    text_gen = Mixtral().generate.remote(
        prompts,
        system=args.system,
        presence_penalty=args.presence_penalty,
        frequency_penalty=args.frequency_penalty,
        repetition_penalty=args.repetition_penalty,
        temperature=args.temperature,
        top_p=args.top_p,
        max_tokens=args.max_tokens,
        n=args.n,
    )
    usage = Function.lookup("substrate-usage", "notify_usage")
    usage.spawn(
        user_id=x_user_id,
        organization_id=x_organization_id,
        path=x_proxy_path,
        metadata={
            "token_count": text_gen.token_count,
            "prompt_count": len(prompts) if prompts else 1,
        },
    )
    return SuccessResponse(data=text_gen)


@stub.local_entrypoint()
def main():
    model = Mixtral()
    questions = ["Implement a Python function to compute the Fibonacci numbers."]
    output = model.generate.remote(questions)
    log.info(output.completions)
