"""
References: 
- https://github.com/danielgatis/rembg/blob/0dcdb080ae083de57084c38e93fb210534c5c693/USAGE.md
"""
import os
import time
from typing import Union, Optional

from modal import Stub, Image, Secret, NetworkFileSystem, gpu, method

from sb_models.logger import log
from sb_models.network import load_image, store_png_to_uri
from sb_models.usage_models import RemoveBackgroundUsage
from sb_models.types.outputs import InferenceRun
from sb_models.types.request import SubstrateRequest
from sb_models.substratecore.models import RemoveBackgroundOut

MODEL_ID = "isnet-general-use"
GPU_TYPE = gpu.A10G()
CACHE_DIR = "/cache"
OUT_PATH = "/root/outs"
MODEL_FOLDER = "isnet"
WRITE_PATH = os.path.join(OUT_PATH, MODEL_FOLDER)


def download_model():
    from rembg import new_session

    t0 = time.time()
    session = new_session(MODEL_ID)

    log.info(f"Downloaded model {MODEL_ID} in {time.time() - t0:.2f}s")


image = (
    Image.debian_slim(python_version="3.10")
    .pip_install(
        "pillow==10.2.0",
        "hf-transfer~=0.1",
        "huggingface_hub==0.20.3",
        "numpy",
        "rembg[gpu]==2.0.54",
        "requests==2.28.1",
        "boto3==1.34.47",
    )
    .env({"HF_HUB_ENABLE_HF_TRANSFER": "1"})
    .run_function(
        download_model,
        secrets=[
            Secret.from_name("huggingface-secret", environment_name="main"),
            Secret.from_dict({"TRANSFORMERS_CACHE": CACHE_DIR}),
        ],
        gpu="any",
        timeout=60 * 30,
    )
)

stub = Stub(name="isnet", image=image)
assets_nfs = NetworkFileSystem.persisted("assets-nfs")


def hex_to_rgba(hex_str):
    """
    Convert a hex string color to an RGBA tuple
    """
    # Remove the hash (#) symbol if it's there
    hex_str = hex_str.strip("#")

    # Convert the hex string to RGBA components
    if len(hex_str) == 6:  # If the hex string is in the form RRGGBB
        r, g, b = int(hex_str[0:2], 16), int(hex_str[2:4], 16), int(hex_str[4:6], 16)
        a = 255  # Assume full opacity if alpha is not provided
    elif len(hex_str) == 8:  # If the hex string is in the form RRGGBBAA
        r, g, b, a = int(hex_str[0:2], 16), int(hex_str[2:4], 16), int(hex_str[4:6], 16), int(hex_str[6:8], 16)
    else:
        raise ValueError("Invalid hex string format. Expected RRGGBB or RRGGBBAA.")

    return (r, g, b, a)


@stub.cls(
    gpu=GPU_TYPE,
    timeout=60 * 5,
    container_idle_timeout=60 * 3,
    network_file_systems={OUT_PATH: assets_nfs},
    secrets=[
        Secret.from_name("aws-file-storage-key", environment_name="main"),
    ],
)
class ISNet:
    def __enter__(self) -> None:
        from rembg import new_session

        t0 = time.time()
        self.session = new_session(MODEL_ID)

        log.info(f"Loaded rembg.session in {time.time() - t0:.2f}s")

    @method()
    async def generate(
        self,
        image_uri: str,
        return_mask: bool = False,
        background_color: Optional[str] = None,
        store: Union[str, bool] = False,
        req: Optional[SubstrateRequest] = None,
    ) -> InferenceRun[RemoveBackgroundOut, RemoveBackgroundUsage]:
        from PIL import Image as PILImage
        from rembg import remove

        t0 = time.time()

        execution_s = time.time() - t0
        input_image = load_image(image_uri, req=req)

        bg_tuple = None
        if background_color:
            bg_tuple = hex_to_rgba(background_color)
        output_image = remove(input_image, session=self.session, only_mask=return_mask, bgcolor=bg_tuple)
        image: PILImage.Image = output_image  # type: ignore
        width, height = image.size
        image_bytes = len(image.tobytes())
        log.info(f"Generated image in {execution_s:.2f}s")
        uri = store_png_to_uri(store, output_image, WRITE_PATH, MODEL_FOLDER, req=req)

        result = RemoveBackgroundOut(image_uri=uri)
        usage = RemoveBackgroundUsage(
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

    uri = "https://media.substrate.run/yoga.png"

    dis = ISNet()
    res = dis.generate.remote(
        image_uri=uri,
    )
    output_path = os.path.expanduser(f"~/Downloads/dis-{int(time.time())}.jpg")
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(res.result.image_uri))
