"""
References: 
- https://huggingface.co/ai-forever/Real-ESRGAN
"""
import os
import time
from typing import Union, Optional

from modal import Stub, Image, Secret, NetworkFileSystem, gpu, method

from sb_models.logger import log
from sb_models.network import load_image, store_png_to_uri
from sb_models.usage_models import UpscaleImageUsage
from sb_models.types.outputs import InferenceRun
from sb_models.types.request import SubstrateRequest
from sb_models.substratecore.models import UpscaleImageOut

WEIGHTS_ID = "weights/RealESRGAN_x4.pth"
GPU_TYPE = gpu.A10G()
CACHE_DIR = "/cache"
OUT_PATH = "/root/outs"
MODEL_FOLDER = "esrgan"
MODEL_DIR = "/model"
WRITE_PATH = os.path.join(OUT_PATH, MODEL_FOLDER)


def download_model():
    import torch
    from RealESRGAN import RealESRGAN

    t0 = time.time()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = RealESRGAN(device, scale=4)
    model.load_weights(WEIGHTS_ID, download=True)

    log.info(f"Downloaded weights {WEIGHTS_ID} in {time.time() - t0:.2f}s")


image = (
    Image.debian_slim(python_version="3.10")
    .apt_install("git")
    .pip_install("git+https://github.com/sberbank-ai/Real-ESRGAN.git")
    .pip_install(
        "torch==2.2.0",
        "pillow==10.2.0",
        "numpy",
        "requests==2.28.1",
        "boto3==1.34.47",
    )
    .apt_install("libgl1-mesa-glx", "libglib2.0-0")
    .run_function(
        download_model,
        gpu="any",
        timeout=60 * 30,
    )
)

stub = Stub(name="esrgan", image=image)
assets_nfs = NetworkFileSystem.persisted("assets-nfs")


@stub.cls(
    gpu=GPU_TYPE,
    timeout=60 * 5,
    container_idle_timeout=60 * 3,
    network_file_systems={OUT_PATH: assets_nfs},
    secrets=[
        Secret.from_name("aws-file-storage-key", environment_name="main"),
    ],
)
class ESRGAN:
    def __enter__(self) -> None:
        import torch
        from RealESRGAN import RealESRGAN

        t0 = time.time()
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = RealESRGAN(self.device, scale=4)
        self.model.load_weights(WEIGHTS_ID, download=False)

        log.info(f"Loaded model in {time.time() - t0:.2f}s")

    @method()
    async def generate(
        self,
        image_uri: str,
        store: Union[str, bool] = False,
        req: Optional[SubstrateRequest] = None,
    ) -> InferenceRun[UpscaleImageOut, UpscaleImageUsage]:
        t0 = time.time()

        execution_s = time.time() - t0
        input_image = load_image(image_uri, req=req).convert("RGB")
        image = self.model.predict(input_image)

        width, height = image.size
        image_bytes = len(image.tobytes())
        log.info(f"Generated image in {execution_s:.2f}s")
        uri = store_png_to_uri(store, image, WRITE_PATH, MODEL_FOLDER, req=req)

        result = UpscaleImageOut(image_uri=uri)
        usage = UpscaleImageUsage(
            execution_seconds=execution_s,
            machine_config=str(GPU_TYPE),
            output_height=height,
            output_width=width,
            output_image_bytes=image_bytes,
        )
        return InferenceRun(result=result, usage=usage)


@stub.local_entrypoint()
async def main():
    import base64

    uri = "https://media.substrate.run/docs-shell-emoji.jpg"

    model = ESRGAN()
    res = model.generate.remote(
        image_uri=uri,
    )
    output_path = os.path.expanduser(f"~/Downloads/esrgan-{int(time.time())}.jpg")
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(res.result.image_uri))
