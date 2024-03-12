import os
import time
import base64
from typing import Dict, List, Union, Optional

from modal import Dict, Stub, Image, Secret, NetworkFileSystem, gpu, method

from sb_models.logger import log
from sb_models.network import load_image, store_jpg_to_uri
from sb_models.usage_models import SegmentAnythingUsage
from sb_models.types.outputs import InferenceRun
from sb_models.types.request import SubstrateRequest
from sb_models.substratecore.models import DetectSegmentsOut

GPU_TYPE = gpu.A10G()
MODEL_DIR = "/model"
WEIGHT_PATH = f"{MODEL_DIR}/FastSAM.pt"
OUT_PATH = "/root/outs"
MODEL_FOLDER = "sam"
WRITE_PATH = os.path.join(OUT_PATH, MODEL_FOLDER)


image = (
    Image.debian_slim("3.10")
    .apt_install("wget")
    .run_commands(
        f"mkdir -p {MODEL_DIR}",
        f"wget https://huggingface.co/spaces/An-619/FastSAM/resolve/main/weights/FastSAM.pt -P {MODEL_DIR}",
    )
    .apt_install("git")
    .pip_install(
        "git+https://github.com/SubstrateLabs/FastSAM.git@main#egg=fastsam",
        "git+https://github.com/openai/CLIP.git@a1d071733d7111c9c014f024669f959182114e33#egg=CLIP",
        "pillow",
        "requests==2.28.1",
        "boto3==1.34.47",
    )
    .apt_install("libgl1-mesa-glx", "libglib2.0-0")
    .pip_install("opencv-python")
)

stub = Stub("SAM", image=image)
stub.cache = Dict.new()
assets_nfs = NetworkFileSystem.persisted("assets-nfs")


@stub.cls(
    gpu=GPU_TYPE,
    container_idle_timeout=60 * 10,
    network_file_systems={OUT_PATH: assets_nfs},
    secrets=[Secret.from_name("aws-file-storage-key", environment_name="main")],
)
class SAM:
    def __enter__(self):
        from fastsam import FastSAM

        t0 = time.time()
        log.info(f"Starting FastSAM")
        self.model = FastSAM(WEIGHT_PATH)
        log.info(f"Loaded model in {time.time() - t0:.2f}s")

    @method()
    def segment(
        self,
        image_uri: str,
        detect_resolution: Optional[int] = None,
        point_prompts: Optional[List[List[int]]] = None,
        box_prompts: Optional[List[List[int]]] = None,
        confidence: Optional[float] = None,
        iou: Optional[float] = None,
        store: Union[str, bool] = False,
        req: Optional[SubstrateRequest] = None,
    ) -> InferenceRun[DetectSegmentsOut, SegmentAnythingUsage]:
        import torch
        from PIL import Image
        from fastsam import FastSAMPrompt

        t0 = time.time()

        if not detect_resolution:
            detect_resolution = 1024
        if not confidence:
            confidence = 0.4
        if not iou:
            iou = 0.9

        log.info(f"SEGMENT: points {point_prompts} boxes {box_prompts}")
        input_img = load_image(image_uri, req)
        input_width, input_height = input_img.size
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        everything_results = self.model.predict(
            input_img,
            device=device,
            retina_masks=True,
            imgsz=detect_resolution,
            conf=confidence,
            iou=iou,
        )

        prompt_process = FastSAMPrompt(input_img, everything_results, device=device)

        ann = prompt_process.everything_prompt()
        if point_prompts:
            # a list of x,y coordinates
            # e.g. point_prompt = [[200, 300]]
            # point_label default [0] [1,0] 0:background, 1:foreground
            ann = prompt_process.point_prompt(
                points=point_prompts,
                pointlabel=[1 for _ in point_prompts],  # NB assume foreground points
            )
        elif box_prompts:
            # [x1, y1, x2, y2]
            if len(box_prompts) > 1:
                ann = prompt_process.box_prompt(bboxes=box_prompts)
            else:
                ann = prompt_process.box_prompt(bbox=box_prompts)
        time_str = time.strftime("%Y%m%d-%H%M%S")
        output_path = "/tmp/" + time_str + image_uri.split("/")[-1] + ".jpeg"
        prompt_process.plot(
            annotations=ann,
            withContours=False,
            mask_random_color=False,
            output_path=output_path,
            better_quality=True,
        )
        execution_s = time.time() - t0
        log.info(f"Segmented image in {execution_s:.2f}s")
        # NOTE: Couldn't easily figure out how to return the path or bounding box of the mask.
        # For now, we'll just return a mask image URI (which is more useful for pipelining anyway)
        # We should eventually dig into what `.plot` does:
        # https://github.com/CASIA-IVA-Lab/FastSAM/blob/4d153e909f0ad9c8ecd7632566e5a24e21cf0071/fastsam/prompt.py#L4
        # results = [json.loads(r.tojson()) for r in everything_results]
        im = Image.open(output_path)
        uri = store_jpg_to_uri(store, im, WRITE_PATH, MODEL_FOLDER, req=req)
        out = DetectSegmentsOut(mask_image_uri=uri)
        usage = SegmentAnythingUsage(
            execution_seconds=execution_s,
            machine_config=str(GPU_TYPE),
            input_image_bytes=len(input_img.tobytes()),
            input_image_width=input_width,
            input_image_height=input_height,
        )
        return InferenceRun(result=out, usage=usage)


@stub.local_entrypoint()
def main():
    uri = "https://media.substrate.run/yoga.png"
    run: InferenceRun = SAM().segment.remote(image_uri=uri, point_prompts=[[1000, 1000]])
    result = run.result

    output_path = os.path.expanduser(f"~/Downloads/sam-output-{int(time.time())}.jpg")
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(result.image_uri))
    try:
        os.system(f"open {output_path}")
    except Exception:
        pass
