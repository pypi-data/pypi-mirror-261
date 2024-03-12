"""
References:
- https://github.com/TencentARC/PhotoMaker
NOTE: I tested this out and it doesn't work that well with non-famous faces
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
from sb_models.network import load_image, multi_store_jpg_to_uri
from sb_models.types.outputs import InferenceRun
from sb_models.types.request import SubstrateRequest
from sb_models.substratecore.models import GenerateImageOut

MODEL_ID = "stabilityai/stable-diffusion-xl-base-1.0"
PHOTOMAKER_ID = "InstantX/InstantID"
PHOTOMAKER_TRIGGER = "<trigger>"
SAFETY_CHECK_ID = "CompVis/stable-diffusion-safety-checker"
CLIP_PROCESSOR_ID = "openai/clip-vit-base-patch32"
MODEL_DIR = "/model"
VAE_FIX = "madebyollin/sdxl-vae-fp16-fix"
CACHE_DIR = "/cache"
OUT_PATH = "/root/outs"
MODEL_FOLDER = "sdxl"
WRITE_PATH = os.path.join(OUT_PATH, MODEL_FOLDER)
GPU_TYPE = gpu.A100()


def download_models():
    import os

    from huggingface_hub import snapshot_download

    ignore = [
        "*.bin",
        "pytorch_model.bin",
        "*.onnx_data",
        "*.onnx",
        "*diffusion_pytorch_model.safetensors",
        "*flax*",
        "*openvino*",
        "model.safetensors",
        "sd_xl_base_1.0_0.9vae.safetensors",
    ]

    log.info("downloading main model")
    snapshot_download(MODEL_ID, cache_dir=CACHE_DIR, ignore_patterns=ignore)
    log.info("downloading safety checker")
    snapshot_download(SAFETY_CHECK_ID, cache_dir=CACHE_DIR)
    log.info("downloading clip processor")
    snapshot_download(
        CLIP_PROCESSOR_ID,
        cache_dir=CACHE_DIR,
        ignore_patterns=["tf_model.h5", "*flax*"],
    )
    snapshot_download(VAE_FIX, cache_dir=CACHE_DIR)

    log.info("downloading photomaker model")
    os.makedirs(MODEL_DIR, exist_ok=True)
    snapshot_download(repo_id="TencentARC/PhotoMaker", local_dir=MODEL_DIR)


image = (
    Image.debian_slim("3.10")
    .apt_install("libgl1-mesa-glx", "libglib2.0-0", "git")
    .pip_install(
        "accelerate~=0.25",
        "transformers~=4.35",
        "safetensors~=0.4",
        "diffusers~=0.25.1",
        "invisible-watermark>=0.2.0",
        "torch==2.1.2",
        "torchvision==0.16.2",
        "requests==2.28.1",
        "boto3==1.34.47",
        "hf-transfer~=0.1",
        "peft==0.6.2",
    )
    .run_commands(
        "pip install git+https://github.com/TencentARC/PhotoMaker.git",
        gpu="any",
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

stub = Stub("photomaker", image=image)
assets_nfs = NetworkFileSystem.persisted("assets-nfs")


def get_models():
    import torch
    from diffusers import (
        AutoencoderKL,
        EulerDiscreteScheduler,
    )
    from photomaker import PhotoMakerStableDiffusionXLPipeline
    from transformers import CLIPImageProcessor
    from diffusers.pipelines.stable_diffusion import StableDiffusionSafetyChecker

    t0 = time.time()

    model_id = MODEL_ID
    log.info(f"using {model_id}")

    extra_args = {}

    vae = AutoencoderKL.from_pretrained(
        VAE_FIX,
        torch_dtype=torch.float16,
        device_map="auto",
        cache_dir=CACHE_DIR,
        local_files_only=True,
    )
    pipe = PhotoMakerStableDiffusionXLPipeline.from_pretrained(
        MODEL_ID,
        torch_dtype=torch.float16,
        # add_watermarker=False,
        variant="fp16",
        # use_safetensors=True,
        cache_dir=CACHE_DIR,
        local_files_only=True,
        device_map="auto",
        vae=vae,
        **extra_args,
    )

    pipe.load_photomaker_adapter(MODEL_DIR, weight_name="photomaker-v1.bin", trigger_word=PHOTOMAKER_TRIGGER)
    pipe.scheduler = EulerDiscreteScheduler.from_config(pipe.scheduler.config)

    safety_checker = StableDiffusionSafetyChecker.from_pretrained(
        SAFETY_CHECK_ID,
        cache_dir=CACHE_DIR,
        local_files_only=True,
    )
    clip_features = CLIPImageProcessor.from_pretrained(
        CLIP_PROCESSOR_ID,
        cache_dir=CACHE_DIR,
        local_files_only=True,
    )

    pipe.watermark = None
    pipe.set_progress_bar_config(disable=True)

    t1 = time.time()
    log.info(f"PIPELINE LOADED: {t1 - t0:.2f}s")
    return pipe, safety_checker, clip_features


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
    def __init__(
        self,
    ):
        self.pipe, self.safety_checker, self.clip_features = get_models()
        # TODO: warmup pipeline

    @method()
    def generate(
        self,
        prompt: str,
        style_prompt: str,
        image_urls: List[str],  # TODO: support multiple images
        style_strength: Optional[float] = None,
        negative_prompt: Optional[str] = None,
        steps: Optional[int] = None,
        num_images: Optional[int] = None,
        store: Union[str, bool] = False,
        height: Optional[int] = None,
        width: Optional[int] = None,
        seed: Optional[int] = None,
        guidance_scale: Optional[float] = None,
        high_noise_frac: float = 0.8,
        run_safety_check: bool = False,
        req: Optional[SubstrateRequest] = None,
    ) -> InferenceRun[List[GenerateImageOut], None]:
        import torch

        if not steps:
            steps = 30
        if guidance_scale is None:
            guidance_scale = 5.0
        if width is None:
            width = 1024
        if height is None:
            height = 1024
        if style_strength is None:
            style_strength = 0.5

        generator = None
        if seed:
            generator = torch.Generator(device="cuda").manual_seed(seed)
            generator.manual_seed(seed)

        prompt = f"{prompt} {PHOTOMAKER_TRIGGER} {style_prompt}"
        log.info(f"PROMPT: {prompt}")
        t0 = time.time()

        pipe = self.pipe

        start_merge_step = int(style_strength * steps)
        if start_merge_step > 30:
            start_merge_step = 30
        # TODO: this is for 50 steps - example code does a clamp to max 30/50
        log.info(f"start_merge_step {start_merge_step}")
        images = []
        for url in image_urls:
            image = load_image(url, req.user_id, req.organization_id)
            images.append(image)

        images = pipe(
            prompt=prompt,
            negative_prompt=negative_prompt,
            input_id_images=images,
            start_merge_step=start_merge_step,
            num_inference_steps=steps,
            num_images_per_prompt=num_images if num_images else 1,
            height=height,
            width=width,
            generator=generator,
            guidance_scale=guidance_scale,
        ).images
        log.info(f"Generated {num_images} latent(s) in {time.time() - t0:.2f}s")

        nsfw = None
        if run_safety_check:
            nsfw = self.run_safety_check(images)

        ims = []
        for i, im in enumerate(images):
            if run_safety_check and nsfw and nsfw[i]:
                log.info(f"Skipping NSFW image[{i}], {prompt}")
                continue
            else:
                ims.append(im)

        uris = multi_store_jpg_to_uri(store, ims, WRITE_PATH, MODEL_FOLDER, req=req)
        result = list(map(lambda uri: GenerateImageOut(image_uri=uri, seed=seed or 0), uris))

        return InferenceRun(result=result, usage=None)

    def run_safety_check(self, images):
        import numpy as np
        import torch

        t0 = time.time()
        image_latents = self.clip_features(images, return_tensors="pt").to("cuda")
        from torch.cuda.amp import autocast

        # need to autocast because the safety checker uses half tensors
        with autocast():
            images, has_nsfw_concept = self.safety_checker(
                images=[np.array(im) for im in images],
                clip_input=image_latents.pixel_values.to(torch.float16),
            )
        t1 = time.time()
        log.info(f"Ran safety check in {t1 - t0:.2f}s")
        return has_nsfw_concept


@stub.local_entrypoint()
async def local() -> None:
    urls = [
        "https://media.substrate.run/ben.jpeg",
        "https://media.substrate.run/ben_1.jpg",
        "https://media.substrate.run/ben_2.jpg",
        "https://media.substrate.run/ben_3.jpg",
    ]
    # urls = [
    #     "https://github.com/TencentARC/PhotoMaker/blob/main/examples/newton_man/newton_0.jpg?raw=true"
    #     "https://github.com/TencentARC/PhotoMaker/blob/main/examples/newton_man/newton_1.jpg?raw=true"
    #     "https://github.com/TencentARC/PhotoMaker/blob/main/examples/newton_man/newton_2.jpg?raw=true"
    #     "https://github.com/TencentARC/PhotoMaker/blob/main/examples/newton_man/newton_3.jpg?raw=true"
    # ]

    prompt = "a half-body portrait of a skinny asian man in front of a mountain"
    style_prompt = "cinematic RAW photo photorealistic fashionable vibrant sharp focus"
    negative_prompt = "(asymmetry, worst quality, low quality, illustration, 3d, 2d, painting, cartoons, sketch), open mouth, grayscale"
    sd = SDXL()
    generation = sd.generate.remote(
        prompt=prompt,
        style_prompt=style_prompt,
        negative_prompt=negative_prompt,
        image_urls=urls,
        style_strength=0.3,
        steps=50,
        store=False,
        num_images=4,
        # seed=88888,
    )
    for i, result in enumerate(generation.result):
        output_path = os.path.expanduser(f"~/Downloads/controlnet_-{int(time.time())}-gen{i}.jpg")
        with open(output_path, "wb") as f:
            f.write(base64.b64decode(result.uri))
        try:
            os.system(f"open {output_path}")
        except Exception:
            pass
