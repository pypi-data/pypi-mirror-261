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

# from sb_models.network import store_gif_to_uri
from sb_models.types.outputs import InferenceRun
from sb_models.types.request import SubstrateRequest
from sb_models.substratecore.models import GenerateImageOut

MODEL_ID = "stabilityai/stable-diffusion-xl-base-1.0"
# MODEL_ID = "SG161222/Realistic_Vision_V5.1_noVAE"
# MODEL_ID = "Lykon/AbsoluteReality"
MOTION_ADAPTER = "guoyww/animatediff-motion-adapter-v1-5-2"
MOTION_ADAPTER = "a-r-r-o-w/animatediff-motion-adapter-sdxl-beta"
MODEL_DIR = "/model"
CACHE_DIR = "/cache"
OUT_PATH = "/root/outs"
MODEL_FOLDER = "sdxl"
WRITE_PATH = os.path.join(OUT_PATH, MODEL_FOLDER)
GPU_TYPE = gpu.A100()


def download_models():
    from huggingface_hub import snapshot_download

    log.info("downloading main model")
    snapshot_download(MODEL_ID, cache_dir=CACHE_DIR)

    log.info("downloading motionadapter model")
    snapshot_download(repo_id=MOTION_ADAPTER, local_dir=MODEL_DIR)


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
        # "torchvision==0.16.2",
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
)

stub = Stub("animatediff", image=image)
assets_nfs = NetworkFileSystem.persisted("assets-nfs")


def get_models():
    import torch
    from diffusers import (
        DDIMScheduler,
        MotionAdapter,
        AnimateDiffPipeline,
    )

    t0 = time.time()

    model_id = MODEL_ID
    log.info(f"using {model_id}")

    adapter = MotionAdapter.from_pretrained(
        MOTION_ADAPTER,
        torch_dtype=torch.float16,
        # local_files_only=True,
        # cache_dir=CACHE_DIR,
        # device_map="auto",
    )
    pipe = AnimateDiffPipeline.from_pretrained(
        model_id,
        motion_adapter=adapter,
        torch_dtype=torch.float16,
        local_files_only=True,
        cache_dir=CACHE_DIR,
        device_map="auto",
    )
    scheduler = DDIMScheduler.from_pretrained(
        model_id,
        subfolder="scheduler",
        clip_sample=False,
        timestep_spacing="linspace",
        beta_schedule="linear",
        steps_offset=1,
    )
    pipe.scheduler = scheduler
    pipe.enable_vae_slicing()
    pipe.enable_model_cpu_offload()
    pipe.watermark = None
    pipe.set_progress_bar_config(disable=True)

    t1 = time.time()
    log.info(f"PIPELINE LOADED: {t1 - t0:.2f}s")
    return pipe


@stub.cls(
    gpu=GPU_TYPE,
    secret=Secret.from_dict({"TRANSFORMERS_CACHE": CACHE_DIR}),
    container_idle_timeout=60 * 4,
    timeout=60 * 5,
    concurrency_limit=8,
    network_file_systems={OUT_PATH: assets_nfs},
)
class AnimateDiff:
    def __init__(
        self,
    ):
        self.pipe = get_models()
        # TODO: warmup pipeline

    @method()
    def generate(
        self,
        prompt: str,
        negative_prompt: Optional[str] = None,
        steps: Optional[int] = None,
        store: Union[str, bool] = False,
        height: Optional[int] = None,
        width: Optional[int] = None,
        seed: Optional[int] = None,
        guidance_scale: Optional[float] = None,
        req: Optional[SubstrateRequest] = None,
    ) -> InferenceRun[List[GenerateImageOut], None]:
        import io

        import torch

        if not steps:
            steps = 30
        if guidance_scale is None:
            guidance_scale = 5.0
        if width is None:
            width = 512
        if height is None:
            height = 512

        generator = None
        if seed:
            generator = torch.Generator(device="cuda").manual_seed(seed)
            generator.manual_seed(seed)

        log.info(f"PROMPT: {prompt}")
        t0 = time.time()

        pipe = self.pipe

        output = pipe(
            prompt=prompt,
            negative_prompt=negative_prompt,
            # num_inference_steps=steps,
            # num_images_per_prompt=num_images if num_images else 1,
            num_frames=16,
            guidance_scale=7.5,
            num_inference_steps=25,
            height=height,
            width=width,
            # generator=generator,
            # guidance_scale=guidance_scale,
        )
        frames = output.frames[0]
        log.info(f"Generated {len(frames)} frames in {time.time() - t0:.2f}s")
        gif_buffer = io.BytesIO()
        first_frame = frames[0]
        first_frame.save(
            gif_buffer,
            format="GIF",
            save_all=True,
            append_images=frames[1:],
            loop=0,
        )
        gif_buffer.seek(0)
        binary_data = gif_buffer.read()

        # Encode the binary data to base64
        base64_gif = base64.b64encode(binary_data)

        # Convert the base64 bytes to a string
        base64_gif_string = base64_gif.decode("utf-8")

        result = []
        uri = base64_gif_string
        # uri = store_gif_to_uri(store, Image.open(BytesIO(binary_data)), WRITE_PATH, MODEL_FOLDER, req=req)

        result.append(GenerateImageOut(image_uri=uri, seed=seed or 0))
        return InferenceRun(result=result, usage=None)


@stub.local_entrypoint()
async def local() -> None:
    prompt = (
        "RAW format masterpiece, bestquality, highlydetailed, ultradetailed, sunset, "
        "billowing clouds over a mountain range, mountain, mountains"
        "rays of sunlight, afternoon, bokeh "
    )
    negative_prompt = "(asymmetry, worst quality, low quality, illustration, 3d, 2d, painting, cartoons, sketch), open mouth, grayscale"
    sd = AnimateDiff()
    generation = sd.generate.remote(
        prompt=prompt,
        negative_prompt=negative_prompt,
        width=1024,
        height=1024,
        # seed=88888,
    )
    output_path = os.path.expanduser(f"~/Downloads/animatediff_-{int(time.time())}.gif")
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(generation.result[0].image_uri))
    try:
        os.system(f"open {output_path}")
    except Exception:
        pass
