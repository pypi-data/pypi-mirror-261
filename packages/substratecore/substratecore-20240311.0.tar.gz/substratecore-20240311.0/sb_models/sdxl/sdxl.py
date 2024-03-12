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

MODEL_ID = "stabilityai/stable-diffusion-xl-base-1.0"
REFINER_ID = "stabilityai/stable-diffusion-xl-refiner-1.0"
SAFETY_CHECK_ID = "CompVis/stable-diffusion-safety-checker"
CLIP_PROCESSOR_ID = "openai/clip-vit-base-patch32"
TURBO_ID = "stabilityai/sdxl-turbo"
VAE_FIX = "madebyollin/sdxl-vae-fp16-fix"
CACHE_DIR = "/cache"
OUT_PATH = "/root/outs"
MODEL_FOLDER = "sdxl"
WRITE_PATH = os.path.join(OUT_PATH, MODEL_FOLDER)
GPU_TYPE = gpu.A100()


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
        "sd_xl_refiner_1.0_0.9vae.safetensors",
        "sd_xl_base_1.0_0.9vae.safetensors",
    ]

    log.info("downloading main model")
    snapshot_download(MODEL_ID, cache_dir=CACHE_DIR, ignore_patterns=ignore)
    log.info("downloading refiner")
    snapshot_download(REFINER_ID, cache_dir=CACHE_DIR, ignore_patterns=ignore)
    log.info("downloading safety checker")
    snapshot_download(SAFETY_CHECK_ID, cache_dir=CACHE_DIR)
    log.info("downloading clip processor")
    snapshot_download(
        CLIP_PROCESSOR_ID,
        cache_dir=CACHE_DIR,
        ignore_patterns=["tf_model.h5", "*flax*"],
    )
    snapshot_download(VAE_FIX, cache_dir=CACHE_DIR)


def download_turbo():
    import torch
    from diffusers import AutoPipelineForText2Image

    AutoPipelineForText2Image.from_pretrained(
        TURBO_ID,
        torch_dtype=torch.float16,
        variant="fp16",
        cache_dir=CACHE_DIR,
    )


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
    .run_function(
        download_turbo,
        secrets=[
            Secret.from_name("huggingface-secret", environment_name="main"),
            Secret.from_dict({"TRANSFORMERS_CACHE": CACHE_DIR}),
        ],
    )
)

stub = Stub("sdxl", image=image)
assets_nfs = NetworkFileSystem.persisted("assets-nfs")


def get_models(
    use_refiner=False,
    use_turbo=False,
):
    import torch
    from diffusers import (
        AutoencoderKL,
        StableDiffusionXLPipeline,
        StableDiffusionXLImg2ImgPipeline,
    )
    from transformers import CLIPImageProcessor
    from diffusers.pipelines.stable_diffusion import StableDiffusionSafetyChecker

    t0 = time.time()

    if use_turbo:
        model_id = TURBO_ID
    else:
        model_id = MODEL_ID
    log.info(f"using {model_id}")

    extra_args = {}

    vae = AutoencoderKL.from_pretrained(
        VAE_FIX,
        torch_dtype=torch.float16,
        cache_dir=CACHE_DIR,
        local_files_only=True,
        device_map="auto",
    )
    pipe = StableDiffusionXLPipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float16,
        add_watermarker=False,
        variant="fp16",
        use_safetensors=True,
        cache_dir=CACHE_DIR,
        local_files_only=True,
        device_map="auto",
        vae=vae,
        **extra_args,
    )

    refiner = None
    if use_refiner and not use_turbo:
        log.info("using refiner")
        refiner = StableDiffusionXLImg2ImgPipeline.from_pretrained(
            REFINER_ID,
            text_encoder_2=pipe.text_encoder_2,
            vae=pipe.vae,
            torch_dtype=torch.float16,
            use_safetensors=True,
            cache_dir=CACHE_DIR,
            variant="fp16",
            local_files_only=True,
            device_map="auto",
        )
        refiner.watermark = None
        refiner.set_progress_bar_config(disable=True)

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
    return pipe, refiner, safety_checker, clip_features


@stub.cls(
    gpu=GPU_TYPE,
    secrets=[Secret.from_dict({"TRANSFORMERS_CACHE": CACHE_DIR})],
    container_idle_timeout=60 * 4,
    timeout=60 * 5,
    concurrency_limit=8,
    network_file_systems={OUT_PATH: assets_nfs},
)
class SDXL:
    def __init__(
        self,
        use_refiner=False,
        use_turbo=True,
    ):
        self.use_refiner = use_refiner
        self.use_turbo = use_turbo

        self.pipe, self.refiner, self.safety_checker, self.clip_features = get_models(
            use_refiner=self.use_refiner,
            use_turbo=self.use_turbo,
        )
        from compel import Compel, ReturnedEmbeddingsType

        self.compel = Compel(
            tokenizer=[self.pipe.tokenizer, self.pipe.tokenizer_2],
            text_encoder=[self.pipe.text_encoder, self.pipe.text_encoder_2],
            returned_embeddings_type=ReturnedEmbeddingsType.PENULTIMATE_HIDDEN_STATES_NON_NORMALIZED,
            requires_pooled=[False, True],
        )

        self.pipe(prompt="vase of flowers", num_inference_steps=5)

    @method()
    def generate(
        self,
        prompt: str,
        negative_prompt: Optional[str] = None,
        steps: Optional[int] = None,
        num_images: Optional[int] = None,
        store: Union[str, bool] = False,
        height: Optional[int] = None,
        width: Optional[int] = None,
        seeds: Optional[List[int]] = None,
        guidance_scale: Optional[float] = None,
        high_noise_frac: float = 0.8,
        run_safety_check: bool = False,
        req: Optional[SubstrateRequest] = None,
        use_ssd=False,  # legacy, substack still passing
    ) -> InferenceRun[List[StableDiffusionImage], BaseStableDiffusionUsage]:
        use_refiner = bool(self.refiner)

        if not steps:
            steps = 4 if self.use_turbo else 30
        if guidance_scale is None:
            guidance_scale = 0.0 if self.use_turbo else 5.0
        if width is None:
            width = 512 if self.use_turbo else 1024
        if height is None:
            height = 512 if self.use_turbo else 1024
        if num_images is None:
            num_images = 1

        t0 = time.time()
        generators = get_seed_generators(seeds, num_images)
        seeds = [s.initial_seed() for s in generators]

        log.info(f"PROMPT: {prompt}")
        conditioning, pooled = self.compel(prompt)
        extra_args = {"width": width, "height": height}
        pipe = self.pipe

        images = pipe(
            prompt_embeds=conditioning,
            pooled_prompt_embeds=pooled,
            negative_prompt=negative_prompt,
            num_inference_steps=steps,
            denoising_end=high_noise_frac if use_refiner else None,
            output_type="latent" if use_refiner else "pil",
            num_images_per_prompt=num_images if num_images else 1,
            generator=generators,
            guidance_scale=guidance_scale,
            **extra_args,
        ).images
        if use_refiner:
            log.info(f"Generated {num_images} latent(s) in {time.time() - t0:.2f}s")
            t1 = time.time()
            images = self.refiner(
                num_inference_steps=steps,
                denoising_start=high_noise_frac,
                num_images_per_prompt=num_images if num_images else 1,
                prompt=prompt,
                image=images,
                generator=generators,
                negative_prompt=negative_prompt,
            ).images
            log.info(f"Refined {num_images} image(s) in {time.time() - t1:.2f}s")

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
    import base64

    generation = SDXL(use_turbo=False).generate.remote(
        prompt="the futuristic ancient city of atlantis, fantasy, solarpunk, cyberpunk, at night lit by gas lamps",
        width=1024,
        height=1024,
        guidance_scale=7.5,
        # store="hosted",
        # seed=88888,
        steps=30,
        negative_prompt="blur, lowres, bad anatomy, bad hands, cropped, worst quality",
    )
    output_path = os.path.expanduser(f"~/Downloads/sdxl_output-{int(time.time())}.jpg")
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(generation.result[0].uri))
    try:
        os.system(f"open {output_path}")
    except Exception:
        pass
