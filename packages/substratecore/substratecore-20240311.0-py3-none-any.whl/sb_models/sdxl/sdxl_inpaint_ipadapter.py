"""
References:
- https://huggingface.co/ByteDance/SDXL-Lightning
- https://huggingface.co/h94/IP-Adapter
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
from sb_models.image_utils import resize_to_resolution
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
MODEL_DIR = "/model"

IPADAPTER_ID = "h94/IP-Adapter"
IP_FOLDER = "sdxl_models"
IP_WEIGHTS = "ip-adapter_sdxl_vit-h.bin"
IP_FACE_WEIGHTS = "ip-adapter-plus-face_sdxl_vit-h.bin"
IP_PATH = f"{MODEL_DIR}/{IP_FOLDER}/{IP_WEIGHTS}"
IP_FACE_PATH = f"{MODEL_DIR}/{IP_FOLDER}/{IP_FACE_WEIGHTS}"

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

    log.info("downloading ip-adapter")
    snapshot_download(IPADAPTER_ID, local_dir=MODEL_DIR)

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

stub = Stub("sdxl_inpaint_ipadapter", image=image)
assets_nfs = NetworkFileSystem.persisted("assets-nfs")


def load_pipe(face: bool = False, inpaint: bool = False):
    import torch
    from diffusers import (
        UNet2DConditionModel,
        EulerDiscreteScheduler,
        StableDiffusionXLImg2ImgPipeline,
        StableDiffusionXLInpaintPipeline,
    )
    from transformers import CLIPVisionModelWithProjection
    from safetensors.torch import load_file

    # TODO: this currently loads from internet, not disk
    image_encoder = CLIPVisionModelWithProjection.from_pretrained(
        "h94/IP-Adapter",
        subfolder="models/image_encoder",
        torch_dtype=torch.float16,
    ).to("cuda")
    unet = UNet2DConditionModel.from_config(BASE_ID, subfolder="unet").to("cuda", torch.float16)
    unet.load_state_dict(load_file(LIGHT_PATH, device="cuda"))
    pipe_class = StableDiffusionXLInpaintPipeline if inpaint else StableDiffusionXLImg2ImgPipeline
    pipe = pipe_class.from_pretrained(
        BASE_ID,
        unet=unet,
        variant="fp16",
        torch_dtype=torch.float16,
        use_safetensors=True,
        cache_dir=CACHE_DIR,
        local_files_only=True,
        device_map="auto",
        image_encoder=image_encoder,
    )
    pipe.load_ip_adapter(
        IP_PATH if not face else IP_FACE_PATH,
        subfolder=IP_FOLDER,
        weight_name=IP_WEIGHTS if not face else IP_FACE_WEIGHTS,
        local_files_only=True,
    )
    pipe.scheduler = EulerDiscreteScheduler.from_config(pipe.scheduler.config, timestep_spacing="trailing")
    pipe.enable_xformers_memory_efficient_attention()
    pipe.watermark = None
    pipe.set_progress_bar_config(disable=True)
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
        t0 = time.time()
        self.pipes = {"face": {}, "standard": {}}
        self.pipes["face"]["img2img"] = load_pipe(face=True, inpaint=False)
        self.pipes["face"]["inpaint"] = load_pipe(face=True, inpaint=True)
        self.pipes["standard"]["img2img"] = load_pipe(face=False, inpaint=False)
        self.pipes["standard"]["inpaint"] = load_pipe(face=False, inpaint=True)
        t1 = time.time()
        log.info(f"LOADED MODELS IN: {t1 - t0:.2f}s")
        # TODO: warmup?

    @method()
    def generate(
        self,
        prompt: str,
        image_uri: str,
        image_prompt_uri: str,
        use_face_model: bool = False,
        mask_image_uri: Optional[str] = None,
        strength: Optional[float] = None,
        ip_adapter_scale: Optional[float] = None,
        negative_prompt: Optional[str] = None,
        output_resolution: Optional[int] = None,
        num_images: Optional[int] = None,
        store: Union[str, bool] = False,
        seeds: Optional[List[int]] = None,
        req: Optional[SubstrateRequest] = None,
    ) -> InferenceRun[List[GenerateImageOut], StableDiffusionWithImageUsage]:
        from diffusers import StableDiffusionXLPipeline

        if num_images is None:
            num_images = 1
        if output_resolution is None:
            output_resolution = 1024
        if strength is None:
            strength = 0.5
        if ip_adapter_scale is None:
            ip_adapter_scale = 0.5
        image = load_image(image_uri, req=req)
        resized_mask_image = None
        resized_image = resize_to_resolution(image, output_resolution)

        pipe: StableDiffusionXLPipeline
        if use_face_model:
            if mask_image_uri:
                pipe = self.pipes["face"]["inpaint"]
            else:
                pipe = self.pipes["face"]["img2img"]
        else:
            if mask_image_uri:
                pipe = self.pipes["standard"]["inpaint"]
            else:
                pipe = self.pipes["standard"]["img2img"]
        pipe.set_ip_adapter_scale(ip_adapter_scale)

        if mask_image_uri:
            mask_image = load_image(mask_image_uri, req=req)
            resized_mask_image = resize_to_resolution(mask_image, output_resolution)

        image_prompt = load_image(image_prompt_uri, req=req)

        generators = get_seed_generators(seeds, num_images)
        seeds = [s.initial_seed() for s in generators]

        log.info(f"PROMPT: {prompt}")
        t0 = time.time()

        width = resized_image.size[0]
        height = resized_image.size[1]
        log.info(f"resized image size: {width}x{height}")

        generators = get_seed_generators(seeds, num_images)
        seeds = [s.initial_seed() for s in generators]

        width = resized_image.size[0]
        height = resized_image.size[1]
        steps = 4  # locked to lightning checkpoint
        guidance_scale = 0
        images = pipe(
            prompt=prompt,
            negative_prompt=negative_prompt,
            strength=strength,
            ip_adapter_image=image_prompt,
            mask_image=resized_mask_image,
            image=resized_image,
            width=width,
            height=height,
            num_inference_steps=steps,
            num_images_per_prompt=num_images if num_images else 1,
            generator=generators,
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

        usage = StableDiffusionWithImageUsage(
            execution_seconds=execution_s,
            machine_config=str(GPU_TYPE),
            prompt_length=len(prompt),
            output_image_bytes=total_img_bytes,
            output_image_count=len(result),
            output_width=width,
            output_height=height,
            input_image_bytes=len(image.tobytes()),
        )
        return InferenceRun(result=result, usage=usage)


@stub.local_entrypoint()
async def local() -> None:
    uri = "https://media.substrate.run/yoga.png"
    mask_uri = "https://media.substrate.run/yoga_floor.jpg"
    # image_url = "https://github.com/tencent-ailab/IP-Adapter/blob/main/assets/images/ai_face.png?raw=true"
    image_url = (
        "https://www.armanrugs.com/pub/media/catalog/product/cache/98dd9305e69fae08552c5375c4472d51/2/0/209581_3.jpg"
    )

    sd = SDXL()
    generation = sd.generate.remote(
        # prompt="A beautiful sunlit yoga studio in the morning",
        use_face_model=False,
        prompt="beautiful square persian rug on the floor of a sunlit yoga studio",
        image_uri=uri,
        image_prompt_uri=image_url,
        mask_image_uri=mask_uri,
        prompt_strength=0.9,
        store=False,
        # seed=88888,
        negative_prompt="blur, lowres, bad anatomy, bad hands, cropped, worst quality",
    )
    output_path = os.path.expanduser(f"~/Downloads/sdxl_img2img_output-{int(time.time())}.jpg")
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(generation.result[0].image_uri))
    try:
        os.system(f"open {output_path}")
    except Exception:
        pass
