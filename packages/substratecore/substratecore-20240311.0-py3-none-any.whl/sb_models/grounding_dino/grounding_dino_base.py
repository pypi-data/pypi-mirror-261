import os
import time
from typing import List, Optional

from modal import Stub, Image as ModalImage, Secret, NetworkFileSystem, gpu, method

from sb_models.logger import log
from sb_models.network import load_image
from sb_models.usage_models import GroundingDINOUsage
from sb_models.types.outputs import InferenceRun
from sb_models.types.request import SubstrateRequest
from sb_models.substratecore.models import BoundingBox, DetectedObject, DetectObjectsOut

# MODEL_ID = "IDEA-Research/grounding-dino-tiny"
MODEL_ID = "IDEA-Research/grounding-dino-base"
CACHE_DIR = "/cache"
OUT_PATH = "/root/outs"
GPU_TYPE = gpu.A100()
MODEL_FOLDER = "gdino"
WRITE_PATH = os.path.join(OUT_PATH, MODEL_FOLDER)


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
        "pytorch-lightning==1.9.5",
        "hf-transfer~=0.1",
    )
    .run_commands(
        "pip install git+https://github.com/EduardoPach/transformers.git@adding-grounding-dino",
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
stub = Stub("grounding_dino_base", image=image)
assets_nfs = NetworkFileSystem.persisted("assets-nfs")


@stub.cls(gpu=GPU_TYPE)
class GD:
    def __init__(self):
        t0 = time.time()
        from transformers import GroundingDinoProcessor, GroundingDinoForObjectDetection

        self.processor = GroundingDinoProcessor.from_pretrained(
            MODEL_ID,
            device_map="auto",
            local_files_only=True,
            cache_dir=CACHE_DIR,
        )
        self.model = GroundingDinoForObjectDetection.from_pretrained(
            MODEL_ID,
            local_files_only=True,
            cache_dir=CACHE_DIR,
        ).to("cuda")
        t1 = time.time()
        log.info(f"PIPELINE LOADED: {t1 - t0:.2f}s")
        # TODO: warmup?

    @method()
    def detect(
        self,
        input_labels: List[str],
        image_uri: str,
        req: Optional[SubstrateRequest] = None,
    ) -> InferenceRun[DetectObjectsOut, GroundingDINOUsage]:
        import torch
        from transformers import GroundingDinoProcessor, GroundingDinoForObjectDetection

        t0 = time.time()

        image = load_image(image_uri)
        input_width, input_height = image.size

        text = " . ".join(input_labels)
        log.info(f"DETECTING: {text}")
        processor: GroundingDinoProcessor = self.processor
        model: GroundingDinoForObjectDetection = self.model
        inputs = processor(images=image, text=text, return_tensors="pt").to("cuda")
        with torch.no_grad():
            outputs = model(**inputs)

        res = processor.post_process_grounded_object_detection(
            outputs,
            inputs.input_ids,
            # box_threshold=0.1,
            # text_threshold=0.3,
            # target_sizes=[image.size[::-1]],
        )[0]
        labels = res["labels"]
        scores = res["scores"].cpu().numpy().tolist()
        boxes = res["boxes"].cpu().numpy().tolist()

        execution_s = time.time() - t0
        log.info(f"Detected in {execution_s:.2f}s")

        usage = GroundingDINOUsage(
            execution_seconds=execution_s,
            machine_config=str(GPU_TYPE),
            input_image_bytes=len(image.tobytes()),
            input_image_width=input_width,
            input_image_height=input_height,
        )
        objects = []
        for i, l in enumerate(labels):
            box = boxes[i]
            bbox = BoundingBox(x1=box[0], y1=box[1], x2=box[2], y2=box[3])
            o = DetectedObject(label=l, bounding_box=bbox)
            objects.append(o)

        return InferenceRun(
            result=DetectObjectsOut(objects=objects),
            usage=usage,
        )


@stub.local_entrypoint()
async def local() -> None:
    uri = "https://media.substrate.run/yoga.png"
    # uri = "http://images.cocodataset.org/val2017/000000039769.jpg"
    gd = GD()
    res = gd.generate.remote(
        prompts=["pipe", "chair"],
        image_uri=uri,
    )
    log.info(res)
    # for i, result in enumerate(res.result):
    #     output_path = os.path.expanduser(f"~/Downloads/sd15_output-{i}_{int(time.time())}.jpg")
    #     with open(output_path, "wb") as f:
    #         f.write(base64.b64decode(result.image_uri))
    #     try:
    #         os.system(f"open {output_path}")
    #     except Exception:
    #         pass
