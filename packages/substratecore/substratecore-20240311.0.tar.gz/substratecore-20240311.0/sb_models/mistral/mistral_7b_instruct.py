import os
import time
from typing import Any, Dict, List, Union, Optional

from modal import (
    Stub,
    Image,
    Period,
    Secret,
    Function,
    gpu,
    method,
)

from sb_models.logger import log
from sb_models.usage_models import MistralUsage
from sb_models.types.outputs import InferenceRun
from sb_models.types.request import SubstrateRequest
from sb_models.substratecore.deprecated_models import (
    MistralPrompt,
    MistralResult,
)

MODEL_DIR = "/model"
BASE_MODEL = "TheBloke/Mistral-7B-Instruct-v0.2-AWQ"
GPU_COUNT = 1
GPU_TYPE = gpu.A100(count=GPU_COUNT)


def download_model():
    from huggingface_hub import snapshot_download

    os.makedirs(MODEL_DIR, exist_ok=True)
    snapshot_download(
        BASE_MODEL,
        local_dir=MODEL_DIR,
    )


image = (
    Image.from_registry("nvcr.io/nvidia/pytorch:23.10-py3")
    .pip_install("torch==2.1.1")
    .pip_install("hf-transfer==0.1.4", "huggingface_hub")
    .env({"HF_HUB_ENABLE_HF_TRANSFER": "1"})
    .pip_install("outlines==0.0.24")
    .run_function(
        download_model,
        timeout=60 * 10,
    )
    .run_commands(
        "pip install https://github.com/vllm-project/vllm/releases/download/v0.2.6/vllm-0.2.6-cp310-cp310-manylinux1_x86_64.whl",
        gpu="any",
    )
)

stub = Stub("mistral-7b-instruct", image=image)
TEMPLATE = """<s>[INST]
{system}

{user} [/INST] """


@stub.cls(
    gpu=GPU_TYPE,
    secrets=[Secret.from_name("huggingface-secret", environment_name="main")],
    container_idle_timeout=60 * 2,
    concurrency_limit=18,
    timeout=60 * 8,
)
class Mistral:
    def __enter__(self):
        from vllm import LLM

        if GPU_COUNT > 1:
            import ray
            import torch

            ray.shutdown()
            ray.init(num_gpus=torch.cuda.device_count())

        self.llm = LLM(
            MODEL_DIR,
            tensor_parallel_size=GPU_COUNT,
            gpu_memory_utilization=0.9,
            max_model_len=32768,
            quantization="awq",
        )
        self.template = TEMPLATE

    @method(
        keep_warm=1 if os.environ.get("MODAL_ENVIRONMENT", "main") == "main" else None,
    )
    def generate(
        self,
        # from MistralIn
        prompts: List[Dict[str, Any]],
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        num_completions: Optional[int] = None,
        json_schema: Optional[Union[str, Dict]] = None,
        # Extra args
        system="",
        presence_penalty: float = 1.1,
        frequency_penalty: float = 0.0,
        repetition_penalty: float = 1.0,
        top_p: float = 0.9,
        req: Optional[SubstrateRequest] = None,
    ) -> InferenceRun[List[MistralResult], MistralUsage]:
        import json

        import vllm.model_executor.layers.sampler as sampler
        from vllm import SamplingParams
        from outlines.serve.vllm import (
            JSONLogitsProcessor,
            _patched_apply_logits_processors,
        )

        prompts_arg: List[MistralPrompt] = list(map(lambda p: MistralPrompt(**p), prompts))
        input_prompts = list(map(lambda p: p.prompt, prompts_arg))

        if isinstance(input_prompts, str):
            input_prompts = [input_prompts]

        t0 = time.time()
        fmt_prompts = [self.template.format(system=system, user=q) for q in input_prompts]

        sampler._apply_logits_processors = _patched_apply_logits_processors
        extra_kwargs = {
            **(temperature is not None and {"temperature": temperature} or {}),
            **(max_tokens and {"max_tokens": max_tokens} or {}),
            **(num_completions and {"n": num_completions} or {}),
            **(json_schema and {"logits_processors": [JSONLogitsProcessor(json_schema, self.llm.llm_engine)]} or {}),
        }
        sampling_params = SamplingParams(
            presence_penalty=presence_penalty,
            frequency_penalty=frequency_penalty,
            repetition_penalty=repetition_penalty,
            top_p=top_p,
            **extra_kwargs,
        )
        input_tokens = self.llm.get_tokenizer()(fmt_prompts)
        input_ids = input_tokens["input_ids"]
        input_token_count = sum([len(ids) for ids in input_ids])

        outputs = self.llm.generate(fmt_prompts, sampling_params)
        total_tokens = sum([len(o.outputs[0].token_ids) for o in outputs])
        duration = time.time() - t0
        rate = round((total_tokens + input_token_count) / duration)
        log.info(
            f"Generated {total_tokens} tokens (on {input_token_count} input) in {duration:.2f}s ({rate} tokens/s))"
        )
        out = []
        for o in outputs:
            completions = []
            json_completions = []
            for output in o.outputs:
                completions.append(output.text)
                if json_schema:
                    try:
                        json_output = json.loads(output.text)
                        json_completions.append(json_output)
                    except Exception:
                        pass
            if json_schema:
                out.append(MistralResult(json_completions=json_completions))
            else:
                out.append(MistralResult(completions=completions))

        usage = MistralUsage(
            execution_seconds=duration,
            machine_config=str(GPU_TYPE),
            output_token_count=total_tokens,
            input_token_count=input_token_count,
        )
        return InferenceRun(result=out, usage=usage)


@stub.function(schedule=Period(minutes=1))
def stats_log():
    if os.environ.get("MODAL_ENVIRONMENT", "main") != "main":
        return

    fn = Function.lookup("mistral-7b-instruct", "Mistral.generate", environment_name="main")
    # FunctionStats(backlog=0, num_active_runners=16, num_total_runners=31)
    stats = fn.get_current_stats()
    datadog = Function.lookup("datadog", "log_metric", environment_name="main")
    datadog.remote(
        name="mistral-7b-instruct-backlog",
        value=stats.backlog,
    )
    datadog.remote(
        name="mistral-7b-instruct-total-runners",
        value=stats.num_total_runners,
    )
    datadog.remote(
        name="mistral-7b-instruct-active-runners",
        value=stats.num_active_runners,
    )


@stub.local_entrypoint()
async def local_one():
    model = Mistral()
    prompts = [{"prompt": "what are the largest cities in the world?"}]
    result = model.generate.remote(prompts=prompts)
    log.info(result)
