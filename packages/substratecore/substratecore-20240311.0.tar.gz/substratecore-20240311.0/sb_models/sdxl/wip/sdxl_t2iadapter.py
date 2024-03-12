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

MODEL_ID = "stabilityai/stable-diffusion-xl-base-1.0"
SAFETY_CHECK_ID = "CompVis/stable-diffusion-safety-checker"
CLIP_PROCESSOR_ID = "openai/clip-vit-base-patch32"
VAE_FIX = "madebyollin/sdxl-vae-fp16-fix"
CACHE_DIR = "/cache"
OUT_PATH = "/root/outs"
MODEL_FOLDER = "sdxl"
WRITE_PATH = os.path.join(OUT_PATH, MODEL_FOLDER)
GPU_TYPE = gpu.A100()


T2IADAPTER_MODELS = {
    "canny": "TencentARC/t2i-adapter-canny-sdxl-1.0",
    "depth_midas": "TencentARC/t2i-adapter-depth-midas-sdxl-1.0",
    # "sketch": "TencentARC/t2i-adapter-sketch-sdxl-1.0",
    # "lineart": "TencentARC/t2i-adapter-lineart-sdxl-1.0",
    # "openpose": "TencentARC/t2i-adapter-openpose-sdxl-1.0",
}


def download_models():
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
        "SSD-1B-A1111*",
        "SSD-1B-modelspec.*",
        "sd_xl_refiner_1.0_0.9vae.safetensors",
        "sd_xl_base_1.0_0.9vae.safetensors",
    ]

    log.info(f"downloading detectors")
    snapshot_download("valhalla/t2iadapter-aux-models", cache_dir=CACHE_DIR)

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
    log.info("downloading vae fix")
    snapshot_download(VAE_FIX, cache_dir=CACHE_DIR)

    for model in T2IADAPTER_MODELS.values():
        log.info(f"downloading t2i adapter model: {model}")
        snapshot_download(model, cache_dir=CACHE_DIR)


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
)

stub = Stub("sdxl_t2iadapter", image=image)
assets_nfs = NetworkFileSystem.persisted("assets-nfs")


def load_stablediffusion(t2iadapter: str):
    import torch
    from diffusers import (
        T2IAdapter,
        AutoencoderKL,
        EulerAncestralDiscreteScheduler,
        StableDiffusionXLAdapterPipeline,
    )

    vae = AutoencoderKL.from_pretrained(
        VAE_FIX,
        torch_dtype=torch.float16,
        cache_dir=CACHE_DIR,
        local_files_only=True,
        device_map="auto",
    )
    adapter_model_id = T2IADAPTER_MODELS.get(t2iadapter)
    adapter = T2IAdapter.from_pretrained(
        adapter_model_id,
        torch_dtype=torch.float16,
        variant="fp16",
        use_safetensors=True,
        cache_dir=CACHE_DIR,
        local_files_only=True,
        device_map="auto",
    )
    euler_a = EulerAncestralDiscreteScheduler.from_pretrained(
        MODEL_ID, subfolder="scheduler", torch_dtype=torch.float16
    )
    pipe = StableDiffusionXLAdapterPipeline.from_pretrained(
        MODEL_ID,
        adapter=adapter,
        scheduler=euler_a,
        variant="fp16",
        torch_dtype=torch.float16,
        use_safetensors=True,
        cache_dir=CACHE_DIR,
        local_files_only=True,
        device_map="auto",
        vae=vae,
    )
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
class SDXL_T2IAdapter:
    def __init__(self):
        from transformers import CLIPImageProcessor
        from controlnet_aux import (
            CannyDetector,
            MidasDetector,
        )
        from diffusers.pipelines.stable_diffusion import StableDiffusionSafetyChecker

        # load detectors
        self.detectors = {}
        self.detectors["depth_midas"] = MidasDetector.from_pretrained(
            "valhalla/t2iadapter-aux-models",
            filename="dpt_large_384.pt",
            model_type="dpt_large",
            cache_dir=CACHE_DIR,
        ).to("cuda")
        self.detectors["canny"] = CannyDetector()

        self.safety_checker = StableDiffusionSafetyChecker.from_pretrained(
            SAFETY_CHECK_ID,
            cache_dir=CACHE_DIR,
            local_files_only=True,
        )
        self.clip_features = CLIPImageProcessor.from_pretrained(
            CLIP_PROCESSOR_ID,
            cache_dir=CACHE_DIR,
            local_files_only=True,
        )
        # load pipes
        t0 = time.time()
        self.pipes = {}
        self.pipes["canny"] = load_stablediffusion("canny")
        self.pipes["depth_midas"] = load_stablediffusion("depth_midas")
        t1 = time.time()
        log.info(f"PIPELINE LOADED: {t1 - t0:.2f}s")

        # TODO: warmup

    @method()
    def generate(
        self,
        prompt: str,
        t2i_adapter: str,
        image_uri: str,
        negative_prompt: Optional[str] = None,
        output_resolution: Optional[int] = None,
        conditioning_scale: Optional[float] = None,
        steps: Optional[int] = None,
        num_images: Optional[int] = None,
        store: Union[str, bool] = False,
        seeds: Optional[List[int]] = None,
        guidance_scale: Optional[float] = None,
        run_safety_check: bool = False,
        req: Optional[SubstrateRequest] = None,
    ) -> InferenceRun[List[GenerateImageOut], StableDiffusionWithImageUsage]:
        import diffusers

        if guidance_scale is None:
            guidance_scale = 7.5
        if steps is None:
            steps = 30
        if num_images is None:
            num_images = 1
        if output_resolution is None:
            output_resolution = 1024
        if conditioning_scale is None:
            conditioning_scale = 7.5
        control_image = load_image(image_uri, req)
        condition_image = resize_to_resolution(control_image, output_resolution)

        generators = get_seed_generators(seeds, num_images)
        seeds = [s.initial_seed() for s in generators]

        log.info(f"PROMPT: {prompt}")
        t0 = time.time()

        control_image = load_image(image_uri, req)
        detector = self.detectors[t2i_adapter]
        condition_image = detector(control_image, detect_resolution=512, image_resolution=output_resolution)

        self.pipe: diffusers.StableDiffusionXLAdapterPipeline = self.pipes[t2i_adapter]
        width = condition_image.size[0]
        height = condition_image.size[1]
        images = self.pipe(
            prompt=prompt,
            negative_prompt=negative_prompt,
            image=condition_image,
            adapter_conditioning_scale=conditioning_scale,
            width=width,
            height=height,
            num_inference_steps=steps,
            num_images_per_prompt=num_images if num_images else 1,
            generator=generators,
            guidance_scale=guidance_scale,
        ).images
        log.info(f"Generated {num_images} latent(s) in {time.time() - t0:.2f}s")

        nsfw = None
        if run_safety_check:
            nsfw = self.run_safety_check(images)

        ims = []
        total_img_bytes = 0
        for i, im in enumerate(images):
            total_img_bytes += len(im.tobytes())
            if run_safety_check and nsfw and nsfw[i]:
                log.info(f"Skipping NSFW image[{i}], {prompt}")
                continue
            else:
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
            output_resolution=output_resolution,
        )
        return InferenceRun(result=result, usage=usage)

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
    # image_url = "https://media.substrate.run/docs-hokusai-great-wave.jpeg"
    image_url = "https://media.substrate.run/yoga.png"
    sd = SDXL_T2IAdapter()
    generation = sd.generate.remote(
        # canny
        # prompt="a corporate logo in front of the beautiful large headquarters in brooklyn new york for a large tech company, cinematic, bokeh, high quality",
        # prompt="ice dragon, cinematic, fantasy, futuristic, steampunk",
        # prompt="a robot, mount fuji in the background, 4k photo, highly detailed",
        # depth
        prompt="A beautiful sunlit yoga studio in the morning",
        # prompt="hokusai the great wave in front of the manhattan skyline, cinematic hd bokeh",
        # prompt="the futuristic ancient city of atlantis, fantasy, solarpunk, cyberpunk, at night lit by gas lamps",
        guidance_scale=7.5,
        t2i_adapter="depth_midas",
        image_uri=image_url,
        conditioning_scale=0.8,
        # negative_prompt="blur, lowres, bad anatomy, bad hands, cropped, worst quality",
    )
    output_path = os.path.expanduser(f"~/Downloads/sdxl_t2i_output-{int(time.time())}.jpg")
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(generation.result[0].image_uri))
    try:
        os.system(f"open {output_path}")
    except Exception:
        pass
