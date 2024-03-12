import os
import time
import base64
import random
from typing import List, Union, Optional

from modal import Stub, Image as ModalImage, Secret, NetworkFileSystem, gpu, method

from sb_models.logger import log
from sb_models.network import (
    load_image,
    multi_store_jpg_to_uri,
)
from sb_models.image_utils import resize_to_resolution
from sb_models.usage_models import StableDiffusionWithImageUsage
from sb_models.types.outputs import InferenceRun
from sb_models.types.request import SubstrateRequest
from sb_models.substratecore.models import GenerateImageOut
from sb_models.stablediffusion_utils import get_seed_generators

random.seed(None)


MODEL_ID = "Lykon/AbsoluteReality"
CACHE_DIR = "/cache"
OUT_PATH = "/root/outs"
MODEL_FOLDER = "sdxl"
WRITE_PATH = os.path.join(OUT_PATH, MODEL_FOLDER)
GPU_TYPE = gpu.A100()
CONTROLNET_MODELIDS = {
    "qr": "monster-labs/control_v1p_sd15_qrcode_monster",
}


def download_models():
    from huggingface_hub import snapshot_download

    log.info(f"downloading detectors")
    snapshot_download("valhalla/t2iadapter-aux-models", cache_dir=CACHE_DIR)

    log.info(f"downloading main model: {MODEL_ID}")
    snapshot_download(MODEL_ID, cache_dir=CACHE_DIR)

    for model in CONTROLNET_MODELIDS.values():
        log.info(f"downloading control model: {model}")
        snapshot_download(model, cache_dir=CACHE_DIR)


image = (
    ModalImage.debian_slim(python_version="3.10")
    .apt_install("libgl1-mesa-glx", "libglib2.0-0")
    .pip_install(
        "accelerate~=0.25",
        "transformers~=4.35",
        "safetensors~=0.4",
        "diffusers~=0.25.1",
        "pillow==10.2.0",
        "pytorch-lightning==1.9.5",
        "hf-transfer~=0.1",
        "controlnet-aux==0.0.7",
        "opencv-python==4.9.0.80",
        "timm==0.6.7",
        "requests==2.28.1",
        "boto3==1.34.47",
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
)
stub = Stub("sd1_5_controlnet_qr", image=image)
assets_nfs = NetworkFileSystem.persisted("assets-nfs")


def load_stable_diffusion(controlnet: str):
    import torch
    from diffusers.models.controlnet import ControlNetModel
    from diffusers.pipelines.pipeline_utils import DiffusionPipeline

    controlnet_modelid = CONTROLNET_MODELIDS.get(controlnet)
    controlnet_model = ControlNetModel.from_pretrained(
        controlnet_modelid,
        torch_dtype=torch.float16,
        cache_dir=CACHE_DIR,
        local_files_only=True,
        device_map="auto",
    )

    pipe = DiffusionPipeline.from_pretrained(
        MODEL_ID,
        controlnet=controlnet_model,
        custom_pipeline="stable_diffusion_controlnet_img2img",
        torch_dtype=torch.float16,
        local_files_only=True,
        cache_dir=CACHE_DIR,
        device_map="auto",
    )
    return pipe


@stub.cls(gpu=GPU_TYPE, secrets=[Secret.from_name("aws-file-storage-key", environment_name="main")])
class SD:
    def __init__(
        self,
    ):
        import torch

        # load pipes
        t0 = time.time()
        torch.backends.cuda.matmul.allow_tf32 = True
        pipe = load_stable_diffusion(controlnet="qr")
        pipe.enable_model_cpu_offload()
        self.pipe = pipe
        t1 = time.time()
        log.info(f"PIPELINE LOADED: {t1 - t0:.2f}s")

        # TODO: warmup

    @method()
    def generate(
        self,
        prompt: str,
        image_uri: str,
        negative_prompt: Optional[str] = None,
        output_resolution: Optional[int] = None,
        conditioning_scale: Optional[float] = None,
        steps: Optional[int] = None,
        num_images: Optional[int] = 1,
        store: Union[str, bool] = False,
        seeds: Optional[List[int]] = None,
        guidance_scale: Optional[float] = None,
        req: Optional[SubstrateRequest] = None,
    ) -> InferenceRun[List[GenerateImageOut], StableDiffusionWithImageUsage]:
        from PIL import Image as PILImage

        if guidance_scale is None:
            guidance_scale = 7.5
        if steps is None:
            steps = 30
        if num_images is None:
            num_images = 1
        if output_resolution is None:
            output_resolution = 1024
        if conditioning_scale is None:
            conditioning_scale = 0.9
        if prompt is None:
            prompt = "best quality, high resolution, HD, professional"

        t0 = time.time()
        extra_args = {}
        control_image: PILImage.Image = load_image(image_uri, req)
        condition_image = resize_to_resolution(control_image, output_resolution)
        extra_args = {"image": condition_image, "strength": 1, **extra_args}
        extra_args = {
            "controlnet_conditioning_image": condition_image,
            "controlnet_conditioning_scale": conditioning_scale,
            "width": condition_image.size[0],
            "height": condition_image.size[1],
            **extra_args,
        }
        generators = get_seed_generators(seeds, num_images)
        seeds = [s.initial_seed() for s in generators]

        images = self.pipe(
            prompt=prompt,
            negative_prompt=negative_prompt,
            num_inference_steps=steps,
            guidance_scale=guidance_scale,
            num_images_per_prompt=num_images,
            generator=generators,
            **extra_args,
        ).images

        total_img_bytes = 0
        for img in images:
            total_img_bytes += len(img.tobytes())

        uris = multi_store_jpg_to_uri(store, images, WRITE_PATH, MODEL_FOLDER, req=req)
        result = []
        for i, uri in enumerate(uris):
            out = GenerateImageOut(image_uri=uri, seed=seeds[i])
            result.append(out)

        execution_s = time.time() - t0
        log.info(f"Generated {len(result)} images in {execution_s:.2f}s")

        usage = StableDiffusionWithImageUsage(
            execution_seconds=execution_s,
            machine_config=str(GPU_TYPE),
            prompt_length=len(prompt),
            output_image_bytes=total_img_bytes,
            output_image_count=len(result),
            output_width=extra_args["width"],
            output_height=extra_args["height"],
            input_image_bytes=len(control_image.tobytes()),
        )
        return InferenceRun(result=result, usage=usage)


@stub.local_entrypoint()
async def local() -> None:
    sd = SD()
    image_url = "https://media.substrate.run/spiral_wide.jpeg"
    # image_url = "https://media.substrate.run/docs-hokusai-great-wave.jpeg"

    # image_url = "https://media.substrate.run/yoga.png"
    # image_url = "https://media.substrate.run/frame_00094.jpg"
    generation = sd.generate.remote(
        prompt="hokusai the great wave in front of manhattan skyline, cinematic hd bokeh",
        image_uri=image_url,
        output_resolution=512,
        guidance_scale=7.5,
        conditioning_scale=0.9,
    )
    output_path = os.path.expanduser(f"~/Downloads/sd15_output-{int(time.time())}.jpg")
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(generation.result[0].image_uri))
    try:
        os.system(f"open {output_path}")
    except Exception:
        pass
