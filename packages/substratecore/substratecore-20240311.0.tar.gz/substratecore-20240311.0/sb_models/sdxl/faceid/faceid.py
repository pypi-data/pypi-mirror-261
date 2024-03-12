"""
References:
- https://huggingface.co/h94/IP-Adapter-FaceID
- https://huggingface.co/spaces/multimodalart/Ip-Adapter-FaceID/blob/main/app.py

NOTE: Haven't gotten this running, paused because it's non-commercial, and relatively low priority
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
MODEL_DIR = "/model"
CACHE_DIR = "/cache"
OUT_PATH = "/root/outs"
MODEL_FOLDER = "sdxl"
WRITE_PATH = os.path.join(OUT_PATH, MODEL_FOLDER)
GPU_TYPE = gpu.A100()

IPADAPTER_ID = "h94/IP-Adapter-FaceID"
IP_FOLDER = "sdxl_models"
IP_WEIGHTS = "ip-adapter_sdxl_vit-h.bin"
IP_FACE_WEIGHTS = "ip-adapter-plus-face_sdxl_vit-h.bin"
IP_PATH = f"{MODEL_DIR}/{IP_FOLDER}/{IP_WEIGHTS}"
IP_FACE_PATH = f"{MODEL_DIR}/{IP_FOLDER}/{IP_FACE_WEIGHTS}"


ip_ckpt = "ip-adapter-faceid_sdxl.bin"
ip_plus_ckpt = "ip-adapter-faceid-plusv2_sdxl.bin"


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

    hf_hub_download(repo_id="h94/IP-Adapter-FaceID", filename=ip_ckpt, repo_type="model")
    hf_hub_download(repo_id="h94/IP-Adapter-FaceID", filename=ip_plus_ckpt, repo_type="model")

    # log.info("downloading lightning")
    # hf_hub_download(LIGHT_REPO, LIGHT_CKPT, local_dir=MODEL_DIR)


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
        "insightface~=0.7.3",
        "onnxruntime==1.16.1",
        "onnx==1.14.0",
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

stub = Stub("sdxl_ipadapter_faceid", image=image)
assets_nfs = NetworkFileSystem.persisted("assets-nfs")


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
        import torch
        from diffusers import (
            DDIMScheduler,
            StableDiffusionXLPipeline,
        )
        from insightface.app import FaceAnalysis

        from sb_models.sdxl.faceid.ip_adapter_faceid import IPAdapterFaceIDXL

        # TODO: download models ahead of time

        # load insightface
        app = FaceAnalysis(name="buffalo_l", providers=["CUDAExecutionProvider", "CPUExecutionProvider"])
        app.prepare(ctx_id=0, det_size=(640, 640))
        self.app = app

        base_model_path = "SG161222/RealVisXL_V3.0"
        # vae_model_path = "stabilityai/sd-vae-ft-mse"
        # image_encoder_path = "laion/CLIP-ViT-H-14-laion2B-s32B-b79K"

        device = "cuda"

        noise_scheduler = DDIMScheduler(
            num_train_timesteps=1000,
            beta_start=0.00085,
            beta_end=0.012,
            beta_schedule="scaled_linear",
            clip_sample=False,
            set_alpha_to_one=False,
            steps_offset=1,
        )
        # vae = AutoencoderKL.from_pretrained(vae_model_path).to(dtype=torch.float16)
        pipe = StableDiffusionXLPipeline.from_pretrained(
            base_model_path,
            torch_dtype=torch.float16,
            scheduler=noise_scheduler,
            # vae=vae,
        )
        ip_model = IPAdapterFaceIDXL(pipe, ip_ckpt, device)
        self.pipe = pipe
        self.ip_model = ip_model

        t1 = time.time()
        log.info(f"LOADED MODELS IN: {t1 - t0:.2f}s")
        # TODO: warmup?

    @method()
    def generate(
        self,
        prompt: str,
        image_prompt_uri: str,
        negative_prompt: Optional[str] = None,
        height: Optional[int] = None,
        width: Optional[int] = None,
        ip_adapter_scale: Optional[float] = None,
        num_images: Optional[int] = None,
        store: Union[str, bool] = False,
        seeds: Optional[List[int]] = None,
        req: Optional[SubstrateRequest] = None,
    ) -> InferenceRun[List[GenerateImageOut], StableDiffusionWithImageUsage]:
        import torch

        if num_images is None:
            num_images = 1
        if width is None:
            width = 1024
        if height is None:
            height = 1024
        if ip_adapter_scale is None:
            ip_adapter_scale = 0.5

        image = load_image(image_prompt_uri, req)

        generators = get_seed_generators(seeds, num_images)
        seeds = [s.initial_seed() for s in generators]

        log.info(f"PROMPT: {prompt}")
        t0 = time.time()

        # generate image
        prompt = "A closeup shot of a beautiful Asian teenage girl in a white dress wearing small silver earrings in the garden, under the soft morning light"
        negative_prompt = "monochrome, lowres, bad anatomy, worst quality, low quality, blurry"

        faces = self.app.get(image)

        faceid_embeds = torch.from_numpy(faces[0].normed_embedding).unsqueeze(0)

        images = self.ip_model.generate(
            prompt=prompt,
            negative_prompt=negative_prompt,
            faceid_embeds=faceid_embeds,
            num_samples=2,
            width=1024,
            height=1024,
            num_inference_steps=30,
            guidance_scale=7.5,
            seed=2023,
        )

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

        usage = StableDiffusionWithImageUsage(  # TODO: rename
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
    # image_url = "https://github.com/tencent-ailab/IP-Adapter/blob/main/assets/images/girl.png?raw=true"
    image_url = "https://github.com/tencent-ailab/IP-Adapter/blob/main/assets/images/ai_face.png?raw=true"
    sd = SDXL()
    generation = sd.generate.remote(
        use_face_model=True,
        image_prompt_uri=image_url,
        prompt="a beautiful girl wearing a casual shirt in a garden",
        num_images=2,
    )
    output_path = os.path.expanduser(f"~/Downloads/sdxl_ip_output-{int(time.time())}.jpg")
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(generation.result[0].image_uri))
    try:
        os.system(f"open {output_path}")
    except Exception:
        pass
