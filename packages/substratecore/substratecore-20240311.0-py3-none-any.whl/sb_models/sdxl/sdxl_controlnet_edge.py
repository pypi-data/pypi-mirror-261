"""
References
- https://huggingface.co/ByteDance/SDXL-Lightning
"""
import os
import time
import base64
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
from sb_models.network import (
    load_image,
    multi_store_jpg_to_uri,
)
from sb_models.usage_models import StableDiffusionWithImageUsage
from sb_models.types.outputs import InferenceRun
from sb_models.types.request import SubstrateRequest
from sb_models.substratecore.models import GenerateImageOut
from sb_models.stablediffusion_utils import get_seed_generators

BASE_ID = "stabilityai/stable-diffusion-xl-base-1.0"
CACHE_DIR = "/cache"
OUT_PATH = "/root/outs"
MODEL_FOLDER = "sdxl"
WRITE_PATH = os.path.join(OUT_PATH, MODEL_FOLDER)
GPU_TYPE = gpu.A100()

LIGHT_REPO = "ByteDance/SDXL-Lightning"
LIGHT_CKPT = "sdxl_lightning_4step_unet.safetensors"
MODEL_DIR = "/model"
LIGHT_PATH = f"{MODEL_DIR}/{LIGHT_CKPT}"


CONTROLNET_MODELIDS = {
    "canny": "diffusers/controlnet-canny-sdxl-1.0",
}


def download_models():
    from huggingface_hub import hf_hub_download, snapshot_download

    ignore = [
        "*.bin",
        "pytorch_model.bin",
        "*.onnx_data",
        "*.onnx",
        # "*diffusion_pytorch_model.safetensors",
        "*flax*",
        "*openvino*",
        "sd_xl_refiner_1.0_0.9vae.safetensors",
        "sd_xl_base_1.0_0.9vae.safetensors",
    ]

    log.info(f"downloading detectors")
    snapshot_download("valhalla/t2iadapter-aux-models", cache_dir=CACHE_DIR)

    log.info("downloading main model")
    snapshot_download(BASE_ID, cache_dir=CACHE_DIR, ignore_patterns=ignore)

    for model in CONTROLNET_MODELIDS.values():
        log.info(f"downloading controlnet model: {model}")
        snapshot_download(model, cache_dir=CACHE_DIR)

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
        "boto3==1.34.47",
        "hf-transfer~=0.1",
        "peft==0.6.2",
        "controlnet-aux==0.0.7",
        "opencv-python==4.9.0.80",
        "timm==0.6.7",
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

stub = Stub("sdxl_controlnet_edge", image=image)
assets_nfs = NetworkFileSystem.persisted("assets-nfs")


def load_pipe(controlnet: str):
    from diffusers import (
        ControlNetModel,
        UNet2DConditionModel,
        EulerDiscreteScheduler,
        StableDiffusionXLControlNetPipeline,
    )
    from safetensors.torch import load_file

    t0 = time.time()
    controlnet_modelid = CONTROLNET_MODELIDS.get(controlnet)
    controlnet_model = ControlNetModel.from_pretrained(
        controlnet_modelid,
        use_safetensors=True,
        cache_dir=CACHE_DIR,
        local_files_only=True,
        device_map="auto",
    )
    unet = UNet2DConditionModel.from_config(BASE_ID, subfolder="unet").to("cuda")
    unet.load_state_dict(load_file(LIGHT_PATH, device="cuda"))
    pipe = StableDiffusionXLControlNetPipeline.from_pretrained(
        BASE_ID,
        unet=unet,
        controlnet=controlnet_model,
        add_watermarker=False,
        use_safetensors=True,
        cache_dir=CACHE_DIR,
        local_files_only=True,
        device_map="auto",
    )
    pipe.scheduler = EulerDiscreteScheduler.from_config(pipe.scheduler.config, timestep_spacing="trailing")
    pipe.watermark = None
    pipe.set_progress_bar_config(disable=True)
    t1 = time.time()
    log.info(f"LOADED {controlnet} PIPE IN: {t1 - t0:.2f}s")
    return pipe


@stub.cls(
    gpu=GPU_TYPE,
    secrets=[
        Secret.from_dict({"TRANSFORMERS_CACHE": CACHE_DIR}),
        Secret.from_name("aws-file-storage-key", environment_name="main"),
    ],
    container_idle_timeout=60 * 4,
    timeout=60 * 5,
    concurrency_limit=8,
    network_file_systems={OUT_PATH: assets_nfs},
)
class SDXL:
    def __init__(self):
        from controlnet_aux import (
            CannyDetector,
        )

        t0 = time.time()
        self.detector = CannyDetector()
        self.pipe = load_pipe("canny")
        t1 = time.time()
        log.info(f"LOADED MODELS IN {t1 - t0:.2f}s")
        # TODO: warmup?

    @method()
    def generate(
        self,
        prompt: str,
        image_uri: str,
        negative_prompt: Optional[str] = None,
        prompt_strength: Optional[float] = None,
        output_resolution: Optional[int] = None,
        conditioning_scale: Optional[float] = None,
        num_images: Optional[int] = None,
        store: Union[str, bool] = False,
        seeds: Optional[List[int]] = None,
        req: Optional[SubstrateRequest] = None,
    ) -> InferenceRun[List[GenerateImageOut], StableDiffusionWithImageUsage]:
        from diffusers import StableDiffusionXLControlNetPipeline

        if num_images is None:
            num_images = 1
        if output_resolution is None:
            output_resolution = 1024
        if conditioning_scale is None:
            conditioning_scale = 0.9
        if prompt_strength is None:
            prompt_strength = 0.5

        generators = get_seed_generators(seeds, num_images)
        seeds = [s.initial_seed() for s in generators]

        log.info(f"PROMPT: {prompt}")
        t0 = time.time()

        control_image = load_image(image_uri, req)
        condition_image = self.detector(control_image, detect_resolution=512, image_resolution=output_resolution)

        self.pipe: StableDiffusionXLControlNetPipeline = self.pipe
        width = condition_image.size[0]
        height = condition_image.size[1]
        steps = 4  # locked to lightning checkpoint
        guidance_scale = 0
        images = self.pipe(
            prompt=prompt,
            negative_prompt=negative_prompt,
            strength=prompt_strength,
            image=condition_image,
            controlnet_conditioning_image=condition_image,
            controlnet_conditioning_scale=conditioning_scale,
            width=width,
            height=height,
            num_images_per_prompt=num_images if num_images else 1,
            generator=generators,
            num_inference_steps=steps,
            guidance_scale=guidance_scale,
        ).images

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

        usage = StableDiffusionWithImageUsage(
            execution_seconds=execution_s,
            machine_config=str(GPU_TYPE),
            prompt_length=len(prompt),
            output_image_bytes=total_img_bytes,
            output_image_count=len(result),
            output_width=width,
            output_height=height,
            input_image_bytes=len(control_image.tobytes()),
        )
        return InferenceRun(result=result, usage=usage)


@stub.local_entrypoint()
async def local() -> None:
    sd = SDXL()
    # image_url = "https://media.substrate.run/docs-hokusai-great-wave.jpeg"
    # image_url = "https://media.substrate.run/spiral-logo.jpeg"
    image_url = "https://media.substrate.run/yoga.png"
    generation = sd.generate.remote(
        # canny
        # prompt="a corporate logo in front of the beautiful large headquarters in brooklyn new york for a large tech company, cinematic, bokeh, high quality",
        # prompt="ice dragon, cinematic, fantasy, futuristic, steampunk",
        # prompt="a robot, mount fuji in the background, 4k photo, highly detailed",
        # depth
        # prompt="A beautiful sunlit yoga studio in the morning",
        prompt_strength=0.9,
        # prompt="a large cresting wave in the style of van gogh, mount fuji in the background, 4k hd oil painting",
        # prompt="hokusai the great wave in front of the manhattan skyline, cinematic hd bokeh",
        prompt="the futuristic ancient city of atlantis, fantasy, solarpunk, cyberpunk, at night lit by gas lamps",
        image_uri=image_url,
        conditioning_scale=0.8,
        # seed=88888,
        # negative_prompt="blur, lowres, bad anatomy, bad hands, cropped, worst quality",
    )
    output_path = os.path.expanduser(f"~/Downloads/sdxl_controlnet-{int(time.time())}.jpg")
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(generation.result[0].image_uri))
    try:
        os.system(f"open {output_path}")
    except Exception:
        pass
