"""
References: 
- https://github.com/enesmsahin/simple-lama-inpainting/blob/main/simple_lama_inpainting/models/model.py
- https://github.com/advimman/lama
"""
import os
import time
from typing import Union, Optional

from modal import Stub, Image, Secret, NetworkFileSystem, gpu, method

from sb_models.logger import log
from sb_models.network import load_image, store_jpg_to_uri
from sb_models.usage_models import LamaUsage
from sb_models.types.outputs import InferenceRun
from sb_models.types.request import SubstrateRequest
from sb_models.substratecore.models import FillMaskOut

REPO_ID = "gaspardbruno/BigLama"
GPU_TYPE = gpu.A10G()
CACHE_DIR = "/cache"
OUT_PATH = "/root/outs"
MODEL_FOLDER = "lama"
MODEL_DIR = "/model"
MODEL_PATH = f"{MODEL_DIR}/big-lama.pt"
WRITE_PATH = os.path.join(OUT_PATH, MODEL_FOLDER)


def download_model():
    from huggingface_hub import snapshot_download

    t0 = time.time()
    snapshot_download(repo_id=REPO_ID, cache_dir=CACHE_DIR, local_dir=MODEL_DIR)

    log.info(f"Downloaded {REPO_ID} in {time.time() - t0:.2f}s")


image = (
    Image.debian_slim(python_version="3.10")
    .apt_install("libgl1-mesa-glx", "libglib2.0-0")
    .pip_install(
        "torch==2.2.0",
        "pillow==10.2.0",
        "hf-transfer~=0.1",
        "huggingface_hub==0.20.3",
        "numpy",
        "opencv-python==4.9.0.80",
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

stub = Stub(name="lama", image=image)
assets_nfs = NetworkFileSystem.persisted("assets-nfs")


def ceil_modulo(x, mod):
    if x % mod == 0:
        return x
    return (x // mod + 1) * mod


def pad_img_to_modulo(img, mod):
    import numpy as np

    channels, height, width = img.shape
    out_height = ceil_modulo(height, mod)
    out_width = ceil_modulo(width, mod)
    return np.pad(
        img,
        ((0, 0), (0, out_height - height), (0, out_width - width)),
        mode="symmetric",
    )


def load_image_to_np(image_uri: str, is_mask: bool, req: Optional[SubstrateRequest] = None) -> "np.ndarray":
    import cv2
    import numpy as np

    img = load_image(image_uri, req=req)  # PIL
    img = np.array(img)

    # https://github.com/enesmsahin/simple-lama-inpainting/pull/7
    if is_mask and img.ndim != 1:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if img.ndim == 3:
        img = np.transpose(img, (2, 0, 1))  # chw
    elif img.ndim == 2:
        img = img[np.newaxis, ...]

    img = img.astype(np.float32) / 255
    pad_modulo = 8
    img = pad_img_to_modulo(img, pad_modulo)
    return img


@stub.cls(
    gpu=GPU_TYPE,
    timeout=60 * 5,
    container_idle_timeout=60 * 3,
    network_file_systems={OUT_PATH: assets_nfs},
    secrets=[
        Secret.from_name("aws-file-storage-key", environment_name="main"),
    ],
)
class Lama:
    def __enter__(self) -> None:
        import torch

        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = torch.jit.load(MODEL_PATH, map_location=self.device)
        self.model.eval()
        self.model.to(self.device)

    @method()
    async def generate(
        self,
        image_uri: str,
        mask_image_uri: str,
        store: Union[str, bool] = False,
        req: Optional[SubstrateRequest] = None,
    ) -> InferenceRun[FillMaskOut, LamaUsage]:
        import numpy as np
        import torch
        import PIL.Image as Image

        t0 = time.time()
        image = load_image_to_np(image_uri, False, req=req)
        mask_image = load_image_to_np(mask_image_uri, True, req=req)

        ts_image = torch.from_numpy(image).unsqueeze(0).to(self.device)
        ts_mask = torch.from_numpy(mask_image).unsqueeze(0).to(self.device)

        ts_mask = (ts_mask > 0) * 1

        with torch.inference_mode():
            inpainted = self.model(ts_image, ts_mask)

            res = inpainted[0].permute(1, 2, 0).detach().cpu().numpy()
            res = np.clip(res * 255, 0, 255).astype(np.uint8)

            image = Image.fromarray(res)
            width, height = image.size
            image_bytes = len(image.tobytes())
            uri = store_jpg_to_uri(store, image, WRITE_PATH, MODEL_FOLDER, req=req)

        execution_s = time.time() - t0
        log.info(f"Generated image in {execution_s:.2f}s")

        result = FillMaskOut(image_uri=uri)
        usage = LamaUsage(
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
    mask_uri = "https://media.substrate.run/yoga_floor.jpg"

    lama = Lama()
    res = lama.generate.remote(
        image_uri=uri,
        mask_image_uri=mask_uri,
    )
    output_path = os.path.expanduser(f"~/Downloads/lama-{int(time.time())}.jpg")
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(res.result.image_uri))
