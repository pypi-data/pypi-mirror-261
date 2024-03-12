import os
import time
import asyncio
from typing import List, Union, Optional

import ray
import torch
import requests
from PIL import Image
from ray import serve
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import (
    AutoProcessor,
    LlavaForConditionalGeneration,
)
from huggingface_hub import snapshot_download

from sb_models.logger import log
from sb_models.network import async_load_image
from sb_models.usage_models import FirellavaUsage
from sb_models.types.outputs import (  # TODO: migrate to types in models
    FirellavaOut,
    InferenceRun,
    FirellavaItem,
    InferenceError,
)

CACHE_DIR = "/cache"
MODEL_NAME = "fireworks-ai/FireLLaVA-13b"


app = FastAPI()


class FirellavaInternalSpec(BaseModel):
    prompt: str
    image_url_batch: Optional[List[str]]
    image_url: Optional[str]
    max_tokens: Optional[int]
    _output_collect: Optional[bool] = False


def _get_model():
    model = LlavaForConditionalGeneration.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.float16,
        token=os.environ["HUGGINGFACE_TOKEN"],
        cache_dir=CACHE_DIR,
        local_files_only=True,
        # attn_implementation="flash_attention_2",
    ).to("cuda")
    processor = AutoProcessor.from_pretrained(MODEL_NAME, cache_dir=CACHE_DIR, token=os.environ["HUGGINGFACE_TOKEN"])
    log.info(f"Loaded model {MODEL_NAME}")

    return model, processor


def save_model():
    if not os.path.exists(os.path.join(CACHE_DIR, MODEL_NAME.replace("/", "--"))):
        log.info("Downloading model...")
        snapshot_download(MODEL_NAME, cache_dir=CACHE_DIR, token=os.environ["HUGGINGFACE_TOKEN"])
    else:
        log.info("Model already downloaded. Using cached model.")


def warm_model(model, processor):
    url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg"
    prompt = "USER: <image>\nWhat is the make of the car? Answer with one word or phrase.\n\nASSISTANT:"
    raw_image = Image.open(requests.get(url, stream=True).raw)
    t0 = time.time()
    inputs = processor(prompt, raw_image, return_tensors="pt").to("cuda", torch.float16)
    output = model.generate(**inputs, max_new_tokens=6, do_sample=False)
    log.info(
        f"WARM UP RES {time.time() - t0:.2f}s, {processor.decode(output[0], skip_special_tokens=True)}",
    )


@serve.deployment()
@serve.ingress(app)
class Firellava:
    def __init__(self):
        t0 = time.time()
        save_model()
        self.model, self.processor = _get_model()
        log.info(f"Loaded model in {time.time() - t0:.2f}s")

    @app.post("/")
    async def post(
        self, req: FirellavaInternalSpec
    ) -> Union[InferenceRun[FirellavaOut, FirellavaUsage], InferenceError]:
        START = "ASSISTANT:"

        t0 = time.time()
        if not req.image_url_batch and req.image_url:
            req.image_url_batch = [req.image_url]
        if not req.image_url_batch:
            req.image_url_batch = []

        log.info(f"GENERATE: {req.prompt}")
        formatted_prompt = f"USER: <image>\n{req.prompt}\n\n{START}"

        try:
            images = await asyncio.gather(*[async_load_image(url, req) for url in req.image_url_batch])
        except Exception as e:
            log.error(f"Failed to download image: {e}")
            return InferenceError(error_message=f"Failed to download images: {req.image_url_batch}")
        responses = []
        input_token_ct = 0
        output_token_ct = 0
        total_image_bytes = 0
        for im in images:
            total_image_bytes += len(im.tobytes())
            inputs = self.processor(formatted_prompt, im, return_tensors="pt").to("cuda", torch.float16)
            output = self.model.generate(**inputs, max_new_tokens=req.max_tokens, do_sample=False)
            response: str = self.processor.decode(output[0], skip_special_tokens=True)
            if START in response:
                parsed_response = response.split(START)[-1].strip()
            else:
                parsed_response = response.strip()

            log.info("RESP", parsed_response)
            log.info(f"Generated response in {time.time() - t0:.2f}s")
            responses.append(parsed_response)
            input_token_ct += inputs["input_ids"].numel()
            output_token_ct += output[0].numel()

        if req._output_collect:
            collected_responses = "\n\n".join(responses)
            result = FirellavaOut(result=[FirellavaItem(generated_text=collected_responses)])
        else:
            result = FirellavaOut(result=[FirellavaItem(generated_text=r) for r in responses])
        usage = FirellavaUsage(
            execution_seconds=time.time() - t0,
            machine_config=str(torch.cuda.get_device_name()),
            input_image_bytes=total_image_bytes,
            input_image_count=len(images),
            input_token_count=input_token_ct,
            output_token_count=output_token_ct,
        )
        return InferenceRun(result=result, usage=usage)


firellava = Firellava.bind()

if __name__ == "__main__":
    ray.init(address="ray://localhost:10001")
    serve.run(firellava)
