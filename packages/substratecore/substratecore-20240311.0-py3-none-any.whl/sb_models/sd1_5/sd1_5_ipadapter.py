import os
import time
import random
from typing import List, Union, Optional

from modal import Stub, Image as ModalImage, Secret, NetworkFileSystem, gpu, method

from sb_models.logger import log
from sb_models.network import load_image, multi_store_jpg_to_uri
from sb_models.usage_models import BaseStableDiffusionUsage
from sb_models.types.outputs import InferenceRun
from sb_models.types.request import SubstrateRequest
from sb_models.substratecore.models import GenerateImageOut
from sb_models.stablediffusion_utils import set_scheduler, get_seed_generators

random.seed(None)


MODEL_ID = "Lykon/AbsoluteReality"
CACHE_DIR = "/cache"
OUT_PATH = "/root/outs"
MODEL_FOLDER = "sd15"
WRITE_PATH = os.path.join(OUT_PATH, MODEL_FOLDER)
GPU_TYPE = gpu.A100()
MODEL_DIR = "/model"
IPADAPTER_ID = "h94/IP-Adapter"
IP_FOLDER = "models"
IP_WEIGHTS = "ip-adapter_sd15.bin"
IP_PATH = f"{MODEL_DIR}/{IP_FOLDER}/{IP_WEIGHTS}"


def download_models():
    from huggingface_hub import snapshot_download

    log.info(f"downloading main model: {MODEL_ID}")
    snapshot_download(MODEL_ID, cache_dir=CACHE_DIR)

    log.info(f"downloading ip-adapter: {IPADAPTER_ID}")
    snapshot_download(IPADAPTER_ID, local_dir=MODEL_DIR)


image = (
    ModalImage.debian_slim(python_version="3.10")
    .pip_install(
        "accelerate~=0.25",
        "transformers~=4.35",
        "safetensors~=0.4",
        "diffusers~=0.25.1",
        "pillow==10.2.0",
        "pytorch-lightning==1.9.5",
        "hf-transfer~=0.1",
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
stub = Stub("sd1_5_ipadapter", image=image)
assets_nfs = NetworkFileSystem.persisted("assets-nfs")


def load_stable_diffusion(**kwargs):
    import torch
    from diffusers.pipelines.stable_diffusion.pipeline_stable_diffusion import (
        StableDiffusionPipeline,
    )

    from sb_models.disk_utils import print_dir

    pipe = StableDiffusionPipeline.from_pretrained(
        MODEL_ID,
        torch_dtype=torch.float16,
        local_files_only=True,
        cache_dir=CACHE_DIR,
        device_map="auto",
        **kwargs,
    )
    # TODO Fix this, for some reason can't load these weights
    print_dir(MODEL_DIR)
    pipe.load_ip_adapter(
        IP_PATH,
        subfolder=IP_FOLDER,
        weight_name=IP_WEIGHTS,
        local_files_only=True,
    )
    pipe.set_ip_adapter_scale(0.6)

    return pipe


def get_models(scheduler: Optional[str] = None):
    import torch

    t0 = time.time()
    if scheduler is None:
        # speed up diffusion process with faster scheduler and memory optimization
        scheduler = "UniPCMultistep"
    torch.backends.cuda.matmul.allow_tf32 = True

    stable_diffusion = load_stable_diffusion()

    set_scheduler(stable_diffusion, scheduler)
    stable_diffusion.enable_model_cpu_offload()
    pipe = stable_diffusion

    t1 = time.time()
    log.info(f"PIPELINE LOADED: {t1 - t0:.2f}s")
    return pipe


@stub.cls(gpu=GPU_TYPE, secrets=[Secret.from_name("aws-file-storage-key", environment_name="main")])
class SD1_5_IPAdapter:
    def __init__(self):
        self.pipe = get_models()

    @method()
    def generate(
        self,
        prompt: str,
        image_prompt_uri: str,
        negative_prompt: Optional[str] = None,
        steps: Optional[int] = None,
        num_images: Optional[int] = None,
        store: Union[str, bool] = False,
        height: Optional[int] = None,
        width: Optional[int] = None,
        seeds: Optional[List[int]] = None,
        guidance_scale: Optional[float] = None,
        req: Optional[SubstrateRequest] = None,
    ) -> InferenceRun[List[GenerateImageOut], BaseStableDiffusionUsage]:
        if guidance_scale is None:
            guidance_scale = 7.5
        if steps is None:
            steps = 30
        if num_images is None:
            num_images = 1
        if width is None:
            width = 512
        if height is None:
            height = 512

        t0 = time.time()
        generators = get_seed_generators(seeds, num_images)
        seeds = [s.initial_seed() for s in generators]

        image = load_image(image_prompt_uri, req)
        # generate image
        images = self.pipe(
            prompt=prompt,
            negative_prompt=negative_prompt,
            ip_adapter_image=image,
            num_inference_steps=steps,
            guidance_scale=guidance_scale,
            num_images_per_prompt=num_images,
            width=width,
            height=height,
            generator=generators,
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

    # image_url = "https://github.com/tencent-ailab/IP-Adapter/blob/main/assets/images/girl.png?raw=true"
    # close-up face
    image_url = "https://github.com/tencent-ailab/IP-Adapter/blob/main/assets/images/river.png?raw=true"
    # image_url = "https://github.com/tencent-ailab/IP-Adapter/blob/main/assets/images/ai_face.png?raw=true"
    sd = SD1_5_IPAdapter()
    generation = sd.generate.remote(
        image_prompt_uri=image_url,
        prompt="a beautiful girl wearing a casual shirt in a garden",
        # seeds=[123, 456],
        num_images=2,
        # store="hosted",
    )
    # print(generation)
    for i, result in enumerate(generation.result):
        output_path = os.path.expanduser(f"~/Downloads/sd15_ip_output-{i}_{int(time.time())}.jpg")
        with open(output_path, "wb") as f:
            f.write(base64.b64decode(result.image_uri))
        try:
            os.system(f"open {output_path}")
        except Exception:
            pass
