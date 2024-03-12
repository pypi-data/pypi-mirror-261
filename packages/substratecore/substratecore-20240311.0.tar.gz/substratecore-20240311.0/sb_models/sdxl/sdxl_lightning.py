"""
References       
- https://huggingface.co/ByteDance/SDXL-Lightning
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
from sb_models.substratecore.models import GenerateImageOut
from sb_models.stablediffusion_utils import get_seed_generators

BASE_ID = "stabilityai/stable-diffusion-xl-base-1.0"
CACHE_DIR = "/cache"
OUT_PATH = "/root/outs"
GPU_TYPE = gpu.A100()
MODEL_FOLDER = "sdxl"
WRITE_PATH = os.path.join(OUT_PATH, MODEL_FOLDER)

LIGHT_REPO = "ByteDance/SDXL-Lightning"
LIGHT_CKPT = "sdxl_lightning_4step_unet.safetensors"
MODEL_DIR = "/model"
LIGHT_PATH = f"{MODEL_DIR}/{LIGHT_CKPT}"


def download_models():
    from huggingface_hub import hf_hub_download, snapshot_download

    ignore = [
        "*.bin",
        "pytorch_model.bin",
        "*.onnx_data",
        "*.onnx",
        "*diffusion_pytorch_model.safetensors",
        "*flax*",
        "*openvino*",
        "model.safetensors",
        "sd_xl_refiner_1.0_0.9vae.safetensors",
        "sd_xl_base_1.0_0.9vae.safetensors",
    ]

    log.info("downloading main model")
    snapshot_download(BASE_ID, cache_dir=CACHE_DIR, ignore_patterns=ignore)

    log.info("downloading lightning")
    hf_hub_download(LIGHT_REPO, LIGHT_CKPT, local_dir=MODEL_DIR)


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

stub = Stub("sdxl_lightning", image=image)
assets_nfs = NetworkFileSystem.persisted("assets-nfs")


@stub.cls(
    gpu=GPU_TYPE,
    secret=Secret.from_dict({"TRANSFORMERS_CACHE": CACHE_DIR}),
    container_idle_timeout=60 * 4,
    timeout=60 * 5,
    concurrency_limit=8,
    network_file_systems={OUT_PATH: assets_nfs},
)
class SDXL:
    def __init__(self):
        import torch
        from diffusers import (
            UNet2DConditionModel,
            EulerDiscreteScheduler,
            StableDiffusionXLPipeline,
        )
        from safetensors.torch import load_file

        t0 = time.time()
        unet = UNet2DConditionModel.from_config(BASE_ID, subfolder="unet").to("cuda", torch.float16)
        unet.load_state_dict(load_file(LIGHT_PATH, device="cuda"))
        pipe = StableDiffusionXLPipeline.from_pretrained(
            BASE_ID,
            unet=unet,
            torch_dtype=torch.float16,
            variant="fp16",
            cache_dir=CACHE_DIR,
            local_files_only=True,
            add_watermarker=False,
            device_map="auto",
        )
        pipe.scheduler = EulerDiscreteScheduler.from_config(pipe.scheduler.config, timestep_spacing="trailing")
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
        negative_prompt: Optional[str] = None,
        num_images: Optional[int] = None,
        store: Union[str, bool] = False,
        height: Optional[int] = None,
        width: Optional[int] = None,
        seeds: Optional[List[int]] = None,
        high_noise_frac: float = 0.8,
        req: Optional[SubstrateRequest] = None,
    ) -> InferenceRun[List[GenerateImageOut], BaseStableDiffusionUsage]:
        from diffusers import StableDiffusionXLPipeline

        if width is None:
            width = 1024
        if height is None:
            height = 1024
        if num_images is None:
            num_images = 1

        t0 = time.time()
        generators = get_seed_generators(seeds, num_images)
        seeds = [s.initial_seed() for s in generators]

        log.info(f"PROMPT: {prompt}")
        pipe: StableDiffusionXLPipeline = self.pipe

        steps = 4  # locked to lightning checkpoint
        guidance_scale = 0
        images = pipe(
            prompt=prompt,
            negative_prompt=negative_prompt,
            denoising_end=high_noise_frac,
            num_images_per_prompt=num_images,
            generator=generators,
            width=width,
            height=height,
            num_inference_steps=steps,
            guidance_scale=guidance_scale,
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
            out = GenerateImageOut(image_uri=uri, seed=seeds[i])
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

    sd = SDXL()
    generation = sd.generate.remote(
        prompt="the futuristic ancient city of atlantis, fantasy, solarpunk, cyberpunk, at night lit by gas lamps",
        width=1024,
        height=1024,
        # guidance_scale=7.5,
        # store="hosted",
        # seed=88888,
        negative_prompt="blur, lowres, bad anatomy, bad hands, cropped, worst quality",
    )
    output_path = os.path.expanduser(f"~/Downloads/sdxl_lightning-{int(time.time())}.jpg")
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(generation.result[0].uri))
    try:
        os.system(f"open {output_path}")
    except Exception:
        pass
