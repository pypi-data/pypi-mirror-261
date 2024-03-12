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
from sb_models.network import load_video
from sb_models.types.outputs import InferenceRun
from sb_models.types.request import SubstrateRequest
from sb_models.substratecore.models import GenerateImageOut
from sb_models.stablediffusion_utils import get_seed_generators

# TODO: update this to use sdxl https://linear.app/substrate-labs/issue/FDN-20/animatediff-spike-text-to-gif
# MODEL_ID = "stabilityai/stable-diffusion-xl-base-1.0"
# MODEL_ID = "SG161222/Realistic_Vision_V5.1_noVAE"
# MODEL_ID = "SG161222/Realistic_Vision_V5.1_noVAE"
MODEL_ID = "stablediffusionapi/nuke-colormax-anime"
# MODEL_ID = "ckpt/cardos-anime" # this one seems good but it's just a safetensors
# MODEL_ID = "nitrosocke/Ghibli-Diffusion"
MODEL_DIR = "/model"
CACHE_DIR = "/cache"
OUT_PATH = "/root/outs"
MODEL_FOLDER = "animatediff"
WRITE_PATH = os.path.join(OUT_PATH, MODEL_FOLDER)
GPU_TYPE = gpu.A100()


def download_models():
    from huggingface_hub import snapshot_download

    log.info("downloading main model")
    snapshot_download(MODEL_ID, cache_dir=CACHE_DIR)

    log.info("downloading motionadapter model")
    snapshot_download(repo_id="guoyww/animatediff-motion-adapter-v1-5-2", cache_dir=CACHE_DIR)


image = (
    Image.debian_slim("3.10")
    .apt_install("libgl1-mesa-glx", "libglib2.0-0", "git")
    .pip_install(
        "accelerate~=0.25",
        "transformers~=4.35",
        "safetensors~=0.4",
        "diffusers~=0.26.3",
        "invisible-watermark>=0.2.0",
        "torch==2.1.2",
        "imageio==2.34.0",
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

stub = Stub("animatediff_video", image=image)
assets_nfs = NetworkFileSystem.persisted("assets-nfs")


def get_models():
    import torch
    from diffusers import (
        DDIMScheduler,
        MotionAdapter,
        AnimateDiffVideoToVideoPipeline,
    )

    t0 = time.time()

    model_id = MODEL_ID
    log.info(f"using {model_id}")

    adapter = MotionAdapter.from_pretrained(
        "guoyww/animatediff-motion-adapter-v1-5-2",
        torch_dtype=torch.float16,
        local_files_only=True,
        cache_dir=CACHE_DIR,
        device_map="auto",
    )
    pipe = AnimateDiffVideoToVideoPipeline.from_pretrained(
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
        video_uri: str,
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

        if not steps:
            steps = 30
        if guidance_scale is None:
            guidance_scale = 7.5
        if width is None:
            width = 512
        if height is None:
            height = 512

        generators = get_seed_generators([seed] if seed else None, 1)
        seeds = [s.initial_seed() for s in generators]

        log.info(f"PROMPT: {prompt}")
        t0 = time.time()

        pipe = self.pipe

        video = load_video(video_uri)

        output = pipe(
            video=video,
            prompt=prompt,
            negative_prompt=negative_prompt,
            guidance_scale=guidance_scale,
            strength=0.2,  # TODO: parameterize
            num_inference_steps=steps,
            height=height,
            width=width,
            generator=generators,
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

        result.append(GenerateImageOut(image_uri=uri, seed=seeds[0]))
        return InferenceRun(result=result, usage=None)


@stub.local_entrypoint()
async def local() -> None:
    # uri = "https://storage.googleapis.com/falserverless/model_tests/animatediff_v2v/rocket.mp4"
    uri = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/animatediff-vid2vid-input-1.gif"
    prompt = "cartoon man playing a guitar on a boat rays of sunlight, bokeh"
    ad = AnimateDiff()
    generation = ad.generate.remote(
        video_uri=uri,
        prompt=prompt,
        # negative_prompt=negative_prompt,
        width=512,
        height=512,
        # seed=88888,
    )
    output_path = os.path.expanduser(f"~/Downloads/animatediff_-{int(time.time())}.gif")
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(generation.result[0].image_uri))
    try:
        os.system(f"open {output_path}")
    except Exception:
        pass
