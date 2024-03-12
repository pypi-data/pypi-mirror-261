"""
Reference
- https://huggingface.co/docs/diffusers/main/en/using-diffusers/svd
"""
import os
import time
from typing import Union, Optional

from modal import Stub, Image as ModalImage, Secret, NetworkFileSystem, gpu, method

from sb_models.logger import log
from sb_models.network import store_file_to_uri
from sb_models.usage_models import AnimateImageUsage
from sb_models.types.outputs import InferenceRun
from sb_models.types.request import SubstrateRequest
from sb_models.substratecore.models import AnimateImageOut

# MODEL_ID = "stabilityai/stable-video-diffusion-img2vid-xt"
MODEL_ID = "stabilityai/stable-video-diffusion-img2vid-xt-1-1"
CACHE_DIR = "/cache"
OUT_PATH = "/root/outs"
MODEL_FOLDER = "sdxl"
WRITE_PATH = os.path.join(OUT_PATH, MODEL_FOLDER)
GPU_TYPE = gpu.A100()


def download_models():
    from huggingface_hub import snapshot_download

    log.info(f"downloading model")
    snapshot_download(MODEL_ID, cache_dir=CACHE_DIR)


image = (
    ModalImage.debian_slim(python_version="3.10")
    .apt_install("git")
    .pip_install(
        "accelerate~=0.25",
        "safetensors~=0.4",
        "pillow==10.2.0",
        "hf-transfer~=0.1",
        "pytorch-lightning==1.9.5",
        "transformers==4.27.1",
        "diffusers~=0.26.3",
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
stub = Stub("svd", image=image)
assets_nfs = NetworkFileSystem.persisted("assets-nfs")


@stub.cls(
    gpu=GPU_TYPE,
    secrets=[Secret.from_name("huggingface-secret", environment_name="main")],
)
class SVD:
    def __init__(self):
        import torch
        from diffusers import StableVideoDiffusionPipeline

        log.info("LOADING PIPELINE")
        t0 = time.time()
        hf_token = os.environ["HUGGINGFACE_TOKEN"]
        pipe = StableVideoDiffusionPipeline.from_pretrained(
            MODEL_ID,
            use_auth_token=hf_token,
            torch_dtype=torch.float16,
            variant="fp16",
            use_safetensors=True,
        )
        pipe.to("cuda")
        pipe.enable_model_cpu_offload()
        self.pipe = pipe
        t1 = time.time()
        log.info(f"PIPELINE LOADED: {t1 - t0:.2f}s")
        # TODO: warmup?

    @method()
    def generate(
        self,
        image_uri: str,
        seed: Optional[int] = None,
        store: Union[str, bool] = False,
        motion_bucket_id: Optional[int] = None,
        noise_aug_strength: Optional[float] = None,
        req: Optional[SubstrateRequest] = None,
    ) -> InferenceRun[AnimateImageOut, AnimateImageUsage]:
        import io

        from diffusers import StableVideoDiffusionPipeline

        from sb_models.network import load_image
        from sb_models.image_utils import crop_to_dimensions
        from sb_models.stablediffusion_utils import get_seed_generator

        if motion_bucket_id is None:
            motion_bucket_id = 127
        if noise_aug_strength is None:
            noise_aug_strength = 0.02

        t0 = time.time()
        # Model can only output these dims
        WIDTH = 1024
        HEIGHT = 576
        image = load_image(image_uri)
        image = crop_to_dimensions(image, WIDTH, HEIGHT)
        generator = get_seed_generator(seed)
        seed = generator.initial_seed()
        pipe: StableVideoDiffusionPipeline = self.pipe
        output = pipe(
            image,
            generator=generator,
            decode_chunk_size=5,
            motion_bucket_id=motion_bucket_id,
            noise_aug_strength=noise_aug_strength,
        )
        frames = output.frames[0]

        execution_s = time.time() - t0
        log.info(f"Generated {len(frames)} frames in {execution_s}s")

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

        uri = store_file_to_uri(store, binary_data, "gif", WRITE_PATH, MODEL_FOLDER, req=req)

        usage = AnimateImageUsage(
            execution_seconds=execution_s,
            machine_config=str(GPU_TYPE),
            output_frames=len(frames),
            output_width=WIDTH,
            output_height=HEIGHT,
            input_image_bytes=len(image.tobytes()),
        )

        return InferenceRun(result=AnimateImageOut(image_uri=uri, seed=seed), usage=usage)


@stub.local_entrypoint()
async def local() -> None:
    import base64

    # uri = "https://media.substrate.run/yoga.png"
    # uri = "http://images.cocodataset.org/val2017/000000039769.jpg"
    # uri = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/svd/rocket.png"
    # uri = "https://media.substrate.run/docs-atlantis-spiral-1.jpg"
    # uri = "https://media.substrate.run/yoga.png"
    uri = "https://media.substrate.run/docs-hokusai.jpg"
    svd = SVD()
    gen = svd.generate.remote(
        image_uri=uri,
    )
    output_path = os.path.expanduser(f"~/Downloads/svd-{int(time.time())}.gif")
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(gen.result["uri"]))
    try:
        os.system(f"open {output_path}")
    except Exception:
        pass
    # for i, result in enumerate(res.result):
    #     output_path = os.path.expanduser(f"~/Downloads/sd15_output-{i}_{int(time.time())}.jpg")
    #     with open(output_path, "wb") as f:
    #         f.write(base64.b64decode(result.image_uri))
    #     try:
    #         os.system(f"open {output_path}")
    #     except Exception:
    #         pass
