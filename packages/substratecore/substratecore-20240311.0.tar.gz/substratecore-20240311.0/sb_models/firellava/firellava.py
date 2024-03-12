import os
import time
import asyncio
from typing import Union, Optional

from modal import Stub, Image, Secret, gpu, method

from sb_models.logger import log
from sb_models.network import async_load_image
from sb_models.usage_models import FirellavaUsage
from sb_models.types.outputs import (  # TODO: migrate to types in models
    FirellavaOut,
    InferenceRun,
    FirellavaItem,
    InferenceError,
)
from sb_models.types.request import SubstrateRequest

GPU_TYPE = gpu.A100()
CACHE_DIR = "/cache"
MODEL_NAME = "fireworks-ai/FireLLaVA-13b"


def _get_model():
    import torch
    from transformers import (
        AutoProcessor,
        LlavaForConditionalGeneration,
    )

    model = LlavaForConditionalGeneration.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.float16,
        token=os.environ["HUGGINGFACE_TOKEN"],
        cache_dir=CACHE_DIR,
        local_files_only=True,
        attn_implementation="flash_attention_2",
    ).to("cuda")
    processor = AutoProcessor.from_pretrained(MODEL_NAME, cache_dir=CACHE_DIR)

    return model, processor


def save_model():
    from huggingface_hub import snapshot_download

    snapshot_download(MODEL_NAME, cache_dir=CACHE_DIR)


def warm_model(model, processor):
    import torch
    import requests
    from PIL import Image

    url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg"
    prompt = "USER: <image>\nWhat is the make of the car? Answer with one word or phrase.\n\nASSISTANT:"
    raw_image = Image.open(requests.get(url, stream=True).raw)
    t0 = time.time()
    inputs = processor(prompt, raw_image, return_tensors="pt").to("cuda", torch.float16)
    output = model.generate(**inputs, max_new_tokens=6, do_sample=False)
    log.info(
        f"WARM UP RES {time.time() - t0:.2f}s, {processor.decode(output[0], skip_special_tokens=True)}",
    )


image = (
    Image.from_registry(
        "nvidia/cuda:12.1.1-devel-ubuntu22.04",
        add_python="3.11",
    )
    .apt_install("git")
    .pip_install(
        "transformers==4.37.2",
        "Pillow==10.2.0",
        "boto3==1.34.47",
        "requests==2.28.1",
        "torch==2.2.0",
        "accelerate==0.26.1",
        "optimum==1.16.2",
        "safetensors==0.4.2",
        "hf-transfer==0.1.5",
        "huggingface_hub==0.20.3",
    )
    .env({"HF_HUB_ENABLE_HF_TRANSFER": "1"})
    .run_function(
        save_model,
        secret=Secret.from_name("huggingface-secret", environment_name="main"),
        timeout=60 * 10,
    )
    .run_commands(
        ["pip install -U wheel", "pip install flash-attn==2.5.0 --no-build-isolation"],
        gpu="any",
    )
)


stub = Stub("firellava", image=image)


@stub.cls(
    gpu=GPU_TYPE,
    secrets=[
        Secret.from_name("huggingface-secret", environment_name="main"),
        Secret.from_name("aws-file-storage-key", environment_name="main"),
    ],
    container_idle_timeout=60 * 3,
    concurrency_limit=16,
    timeout=60 * 10,
    allow_concurrent_inputs=4,
)
class Firellava:
    def __enter__(self):
        t0 = time.time()
        self.model, self.processor = _get_model()
        log.info(f"Loaded model in {time.time() - t0:.2f}s")

    @method()
    async def generate(
        self,
        prompt: str,
        image_url: str = "",
        max_tokens: Optional[int] = 32,
        image_url_batch: Optional[str] = None,
        _output_collect: Optional[bool] = False,
        req: Optional[SubstrateRequest] = None,
    ) -> Union[InferenceRun[FirellavaOut, FirellavaUsage], InferenceError]:
        import torch

        START = "ASSISTANT:"

        t0 = time.time()
        if not image_url_batch:
            image_url_batch = [image_url]

        log.info(f"GENERATE: {prompt}")
        formatted_prompt = f"USER: <image>\n{prompt}\n\n{START}"

        try:
            images = await asyncio.gather(*[async_load_image(url, req) for url in image_url_batch])
        except Exception as e:
            log.error(f"Failed to download image: {e}")
            return InferenceError(error_message=f"Failed to download images: {image_url_batch}")
        responses = []
        input_token_ct = 0
        output_token_ct = 0
        total_image_bytes = 0
        for im in images:
            total_image_bytes += len(im.tobytes())
            inputs = self.processor(formatted_prompt, im, return_tensors="pt").to("cuda", torch.float16)
            output = self.model.generate(**inputs, max_new_tokens=max_tokens, do_sample=False)
            response: str = self.processor.decode(output[0], skip_special_tokens=True)
            if START in response:
                parsed_response = response.split(START)[-1].strip()
            else:
                parsed_response = response.strip()

            log.info(f"RESP {parsed_response}")
            log.info(f"Generated response in {time.time() - t0:.2f}s")
            responses.append(parsed_response)
            input_token_ct += inputs["input_ids"].numel()
            output_token_ct += output[0].numel()

        if _output_collect:
            collected_responses = "\n\n".join(responses)
            result = FirellavaOut(result=[FirellavaItem(generated_text=collected_responses)])
        else:
            result = FirellavaOut(result=[FirellavaItem(generated_text=r) for r in responses])
        usage = FirellavaUsage(
            execution_seconds=time.time() - t0,
            machine_config=str(GPU_TYPE),
            input_image_bytes=total_image_bytes,
            input_image_count=len(images),
            input_token_count=input_token_ct,
            output_token_count=output_token_ct,
        )
        return InferenceRun(result=result, usage=usage)


@stub.local_entrypoint()
def main():
    # prompt = "Describe this image in detail."
    # url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg"
    prompt = "What steps would you take to transform this into a yoga studio?"
    url = "https://media.substrate.run/yoga.png"
    t0 = time.time()
    # results = []
    # for r in Firellava().generate.starmap(
    #     [(prompt, url)] * 4, kwargs=dict(max_tokens=24)
    # ):
    #     results.append(r)
    # log.info(results)
    res = Firellava().generate.remote(prompt, image_url=url, max_tokens=512)
    log.info(res)
    log.info(f"TOTAL TIME: {time.time() - t0:.2f}s")
