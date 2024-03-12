"""
References       
- https://huggingface.co/docs/diffusers/en/api/pipelines/stable_diffusion/gligen
"""
import os
import time
from typing import List, Union, Optional

from modal import (
    Stub,
    Image,
    Secret,
    NetworkFileSystem,
    gpu,
    method,
)

from sb_models.logger import log
from sb_models.network import multi_store_jpg_to_uri
from sb_models.usage_models import BaseStableDiffusionUsage
from sb_models.types.outputs import InferenceRun
from sb_models.types.request import SubstrateRequest
from sb_models.stablediffusion_utils import get_seed_generators

# TODO(ben): replace with new public .models (carefully! in use)
from sb_models.substratecore.deprecated_models import (
    StableDiffusionImage,
)

BASE_ID = "anhnct/Gligen_Text_Image"
CACHE_DIR = "/cache"
OUT_PATH = "/root/outs"
GPU_TYPE = gpu.A100()
MODEL_FOLDER = "gligen"
WRITE_PATH = os.path.join(OUT_PATH, MODEL_FOLDER)


def download_models():
    from huggingface_hub import snapshot_download

    log.info("downloading main model")
    snapshot_download(BASE_ID, cache_dir=CACHE_DIR)


image = (
    Image.debian_slim("3.10")
    .apt_install("libgl1-mesa-glx", "libglib2.0-0", "git")
    .pip_install(
        "accelerate~=0.25",
        "transformers~=4.35",
        "safetensors~=0.4",
        "diffusers~=0.25.1",
        "xformers~=0.0.23",
        "invisible-watermark>=0.2.0",
        "pytorch-lightning==1.9.5",
        "requests==2.28.1",
        "hf-transfer~=0.1",
        "peft==0.6.2",
    )
    .env({"HF_HUB_ENABLE_HF_TRANSFER": "1"})
    .run_function(
        download_models,
        secrets=[
            Secret.from_name("huggingface-secret", environment_name="main"),
            Secret.from_dict({"TRANSFORMERS_CACHE": CACHE_DIR}),
        ],
        timeout=60 * 30,
    )
    .pip_install("compel")
)

stub = Stub("gligen", image=image)
assets_nfs = NetworkFileSystem.persisted("assets-nfs")


@stub.cls(
    gpu=GPU_TYPE,
    secret=Secret.from_dict({"TRANSFORMERS_CACHE": CACHE_DIR}),
    container_idle_timeout=60 * 4,
    timeout=60 * 5,
    concurrency_limit=8,
    network_file_systems={OUT_PATH: assets_nfs},
)
class GLIGEN:
    def __init__(self):
        import torch
        from diffusers import (
            StableDiffusionGLIGENTextImagePipeline,
        )

        t0 = time.time()
        pipe = StableDiffusionGLIGENTextImagePipeline.from_pretrained(
            BASE_ID,
            torch_dtype=torch.float16,
            cache_dir=CACHE_DIR,
            local_files_only=True,
            add_watermarker=False,
        ).to("cuda")
        pipe.watermark = None
        pipe.set_progress_bar_config(disable=True)
        self.pipe = pipe
        t1 = time.time()
        log.info(f"LOADED MODELS IN {t1 - t0:.2f}s")
        # TODO: warmup?

    @method()
    def generate(
        self,
        prompt: str,
        object_text_prompts: List[str],
        object_bboxes: List[List[float]],
        negative_prompt: Optional[str] = None,
        num_images: Optional[int] = None,
        store: Union[str, bool] = False,
        height: Optional[int] = None,
        width: Optional[int] = None,
        seeds: Optional[List[int]] = None,
        req: Optional[SubstrateRequest] = None,
    ) -> InferenceRun[List[StableDiffusionImage], BaseStableDiffusionUsage]:
        from diffusers import StableDiffusionGLIGENTextImagePipeline

        if width is None or width > 512:
            width = 512
        if height is None or height > 512:
            height = 512
        if num_images is None:
            num_images = 1

        t0 = time.time()
        generators = get_seed_generators(seeds, num_images)
        seeds = [s.initial_seed() for s in generators]

        log.info(f"PROMPT: {prompt}")
        pipe: StableDiffusionGLIGENTextImagePipeline = self.pipe

        boxes = [[0.2676, 0.4088, 0.4773, 0.7183]]
        # gligen_image = load_image(
        #     "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/gligen/backpack.jpeg"
        # )

        images = pipe(
            gligen_phrases=object_text_prompts,
            gligen_boxes=object_bboxes,
            # gligen_images=[gligen_image],
            gligen_scheduled_sampling_beta=1,
            prompt=prompt,
            negative_prompt=negative_prompt,
            num_inference_steps=25,
            # num_inference_steps=steps,
            num_images_per_prompt=num_images,
            width=width,
            height=height,
        ).images
        log.info(f"Generated {num_images} latent(s) in {time.time() - t0:.2f}s")

        ims = []
        total_img_bytes = 0
        for im in images:
            total_img_bytes += len(im.tobytes())
            ims.append(im)

        uris = multi_store_jpg_to_uri(store, ims, WRITE_PATH, MODEL_FOLDER, req=req)

        result = []
        for i, uri in enumerate(uris):
            out = StableDiffusionImage(uri=uri, seed=seeds[i])
            result.append(out)

        execution_s = time.time() - t0
        log.info(f"Generated {len(result)} images in {execution_s:.2f}s")

        usage = BaseStableDiffusionUsage(
            execution_seconds=execution_s,
            machine_config=str(GPU_TYPE),
            prompt_length=len(prompt),
            output_image_bytes=total_img_bytes,
            output_image_count=len(result),
            output_width=width,
            output_height=height,
        )
        return InferenceRun(result=result, usage=usage)


@stub.local_entrypoint()
async def local() -> None:
    import base64

    sd = GLIGEN()
    generation = sd.generate.remote(
        prompt="cyberpunk neo tokyo at night lit by neon lights bokeh cinematic HD",
        width=512,
        height=512,
        # guidance_scale=7.5,
        # store="hosted",
        # seed=88888,
        negative_prompt="blur, lowres, bad anatomy, bad hands, cropped, worst quality",
    )
    output_path = os.path.expanduser(f"~/Downloads/gligen-{int(time.time())}.jpg")
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(generation.result[0].uri))
    try:
        os.system(f"open {output_path}")
    except Exception:
        pass
