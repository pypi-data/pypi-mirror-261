"""
Deprecated – leaving this as a reference implementation but this is no longer used
-ben
"""
import os
from typing import Any, Dict, Union, Optional

from modal import Stub, Image as ModalImage, Secret, NetworkFileSystem, gpu, method

from sb_models.network import load_image, store_jpg_to_uri
from sb_models.types.outputs import InferenceRun
from sb_models.types.request import SubstrateRequest

OUT_PATH = "/root/outs"
MODEL_FOLDER = "control_aux"
WRITE_PATH = os.path.join(OUT_PATH, MODEL_FOLDER)
GPU_TYPE = gpu.A100()
CACHE_DIR = "/cache"


def download_models():
    from huggingface_hub import snapshot_download

    snapshot_download("valhalla/t2iadapter-aux-models", cache_dir=CACHE_DIR)
    snapshot_download("lllyasviel/Annotators", cache_dir=CACHE_DIR)
    snapshot_download("LiheYoung/depth-anything-large-hf", cache_dir=CACHE_DIR)


stub_image = (
    ModalImage.debian_slim("3.11")
    .apt_install("libgl1-mesa-glx", "libglib2.0-0", "git")
    .pip_install(
        "opencv-python==4.9.0.80",
        "pillow==10.2.0",
        "requests==2.28.1",
        "boto3==1.34.47",
        "controlnet-aux==0.0.7",
        # "transformers==4.37.1", # depth_anything in transformers is brand new
        "torch==2.0.1",  # see https://github.com/invoke-ai/InvokeAI/issues/5083
        "timm==0.6.7",
        "hf-transfer~=0.1",
    )
    .run_commands(
        "pip install git+https://github.com/huggingface/transformers.git",
        gpu="any",
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
stub = Stub("control_aux", image=stub_image)
assets_nfs = NetworkFileSystem.persisted("assets-nfs")


def process(
    detector,
    image_uri: str,
    detect_resolution: int = 100,
    output_resolution: int = 200,
    store: Union[str, bool] = False,
    req: Optional[SubstrateRequest] = None,
) -> Dict[str, Any]:
    image = load_image(image_uri, req=req)
    result_image = detector(image, detect_resolution=detect_resolution, image_resolution=output_resolution)
    data_uri = store_jpg_to_uri(store, result_image, WRITE_PATH, MODEL_FOLDER, req=req)
    return {"image_uri": data_uri}


# TODO: move ControlAux into ControlNet nodes
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
class ControlAux:
    def __init__(self):
        from transformers import pipeline
        from controlnet_aux import (
            HEDdetector,
            MLSDdetector,
            CannyDetector,
            MidasDetector,
            PidiNetDetector,
            OpenposeDetector,
        )

        self.detectors = {}
        self.detectors["depth_midas"] = MidasDetector.from_pretrained(
            "valhalla/t2iadapter-aux-models",
            filename="dpt_large_384.pt",
            model_type="dpt_large",
            cache_dir=CACHE_DIR,
        ).to("cuda")
        self.detectors["open_pose"] = OpenposeDetector.from_pretrained(
            "lllyasviel/Annotators",
            cache_dir=CACHE_DIR,
        ).to("cuda")
        self.detectors["edge_canny"] = CannyDetector()
        self.detectors["edge_pidi"] = PidiNetDetector.from_pretrained(
            "lllyasviel/Annotators",
            cache_dir=CACHE_DIR,
        ).to("cuda")
        self.detectors["edge_hed"] = HEDdetector.from_pretrained(
            "lllyasviel/Annotators",
            cache_dir=CACHE_DIR,
        ).to("cuda")
        self.detectors["line_mlsd"] = MLSDdetector.from_pretrained(
            "lllyasviel/Annotators",
            cache_dir=CACHE_DIR,
        ).to("cuda")
        self.pipe = pipeline(
            task="depth-estimation",
            model="LiheYoung/depth-anything-large-hf",
            cache_dir=CACHE_DIR,
        )

    @method()
    def generate(
        self,
        model: str,
        image_uri: str,
        detect_resolution: int = 512,  # TODO: get defaults from the openapi spec
        output_resolution: int = 1024,
        store: Union[str, bool] = False,
        req: Optional[SubstrateRequest] = None,
    ) -> InferenceRun[Dict[str, Any], None]:
        if model == "depth_anything":
            image = load_image(image_uri, req=req)
            inference = self.pipe(image)
            depth = inference["depth"]
            data_uri = store_jpg_to_uri(store, depth, WRITE_PATH, MODEL_FOLDER, req=req)
            result = {"image_uri": data_uri}
        else:
            detector = self.detectors[model]
            result = process(
                detector,
                image_uri=image_uri,
                detect_resolution=detect_resolution,
                output_resolution=output_resolution,
                store=store,
                req=req,
            )
        return InferenceRun(result=result, usage=None)


@stub.local_entrypoint()
def run() -> None:
    import time
    import base64

    from sb_models.logger import log

    c = ControlAux()
    output = c.generate.remote(
        model="depth_midas",
        image_uri="https://media.substrate.run/yoga.png",
    )
    output_path = os.path.expanduser(f"~/Downloads/control_aux-{int(time.time())}.jpg")
    log.info(f"Saving {output_path}")
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(output.result["image_uri"]))
    try:
        os.system(f"open {output_path}")
    except Exception:
        pass
