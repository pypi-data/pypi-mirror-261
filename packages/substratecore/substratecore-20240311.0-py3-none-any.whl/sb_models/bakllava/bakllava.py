import os
import time
from typing import Optional

from modal import Stub, Image, Secret, gpu, method

from sb_models.logger import log
from sb_models.types.outputs import InferenceRun, AssistantChatCompletion
from sb_models.types.request import SubstrateRequest

GPU_TYPE = gpu.A10G()
MODEL_DIR = "/model"
MODEL_NAME = "BakLLaVA-1-Q4_K_M.gguf"
CLIP_MODEL_PATH = f"{MODEL_DIR}/BakLLaVA-1-clip-model.gguf"
BASE_MODEL = "advanced-stack/bakllava-mistral-v1-gguf"


def download_model():
    from huggingface_hub import snapshot_download

    os.makedirs(MODEL_DIR, exist_ok=True)
    snapshot_download(
        BASE_MODEL,
        local_dir=MODEL_DIR,
        token=os.environ["HUGGINGFACE_TOKEN"],
    )


image = (
    Image.from_registry(
        "nvidia/cuda:12.1.1-devel-ubuntu22.04",
        add_python="3.11",
    )
    .run_commands(
        'CUDA_DOCKER_ARCH=all LLAMA_CUBLAS=1 CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python --no-cache-dir --force-reinstall',
    )
    .apt_install("git")
    .pip_install("git+https://github.com/SubstrateLabs/py-llm-core.git@dd5ec35")
    .pip_install("hf-transfer==0.1.4", "huggingface_hub")
    .run_function(
        download_model,
        secret=Secret.from_name("huggingface-secret", environment_name="main"),
        timeout=60 * 10,
    )
    .env({"MODELS_CACHE_DIR": MODEL_DIR})
)

stub = Stub("bakllava-1", image=image)


@stub.cls(
    gpu=GPU_TYPE,
    secrets=[Secret.from_name("huggingface-secret", environment_name="main")],
    container_idle_timeout=60 * 3,
    concurrency_limit=12,
)
class Bakllava:
    def __enter__(self):
        from llm_core.llm import LLaVACPPModel

        t0 = time.time()
        log.info("Starting LLaVACPP")
        llm = LLaVACPPModel(
            name=MODEL_NAME,
            llama_cpp_kwargs={
                "verbose": False,
                "logits_all": True,
                "n_ctx": 8000,
                "n_gpu_layers": 1000,
                "n_threads": 1,
                "clip_model_path": CLIP_MODEL_PATH,
            },
        )
        llm.load_model()
        log.info(f"Loaded model in {time.time() - t0:.2f}s")
        self.llm = llm

    @method()
    def generate(
        self,
        prompt: str,
        image_url: str,
        history=None,
        temperature: Optional[float] = 0.1,
        req: Optional[SubstrateRequest] = None,
    ) -> InferenceRun[AssistantChatCompletion, None]:
        history = history or [{"role": "user", "content": [{"type": "image_url", "image_url": image_url}]}]

        import ssl

        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        t0 = time.time()
        log.info(f"GENERATE: {prompt}")
        response = self.llm.ask(prompt, history=history, temperature=temperature)
        log.info(f"Generated response ({response.usage.completion_tokens} tokens) in {time.time() - t0:.2f}s")
        completion_tokens = response.usage.completion_tokens
        prompt_tokens = response.usage.prompt_tokens
        result = AssistantChatCompletion(
            message=response.choices[0].message.content,
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            total_tokens=response.usage.total_tokens,
        )
        return InferenceRun(result=result, usage=None)


@stub.local_entrypoint()
def main():
    from sb_models.logger import log

    prompt = "Describe this image in detail"
    image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/TheCheethcat.jpg/800px-TheCheethcat.jpg"
    results = Bakllava().generate.remote(prompt=prompt, image_url=image_url)
    log.info(results)
