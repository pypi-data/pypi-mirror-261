import os
from pathlib import Path
from dataclasses import dataclass

from modal import (
    Stub,
    Image,
    Secret,
    Volume,
    method,
)

from sb_models.logger import log

stub = Stub(name="dreambooth")


image = (
    Image.debian_slim(python_version="3.10")
    .pip_install(
        "accelerate",
        "datasets~=2.13",
        "ftfy",
        "smart_open",
        "transformers",
        "torch",
        "torchvision",
        "triton",
    )
    .apt_install("git")
    .run_commands(
        "cd /root && git clone https://github.com/huggingface/diffusers",
        "cd /root/diffusers && pip install -e .",
    )
    .env({"MODEL_NAME": "stabilityai/stable-diffusion-xl-base-1.0"})
)
volume = Volume.persisted("vol-dreambooth")
MODEL_DIR = Path("/lora-trained")
stub.volume = volume


@dataclass
class SharedConfig:
    instance_name: str = "rsc"
    class_name: str = "person"


@dataclass
class TrainConfig(SharedConfig):
    # training prompt looks like `{PREFIX} {INSTANCE_NAME} the {CLASS_NAME} {POSTFIX}`
    prefix: str = "a photo of"
    postfix: str = ""

    # locator for plaintext file with urls for images of target instance
    instance_example_urls_file: str = str(Path(__file__).parent / "instance_example_urls.txt")

    model_name: str = "stabilityai/stable-diffusion-xl-base-1.0"

    resolution: int = 1024
    train_batch_size: int = 1
    gradient_accumulation_steps: int = 4
    learning_rate: float = 2e-5
    lr_scheduler: str = "constant"
    lr_warmup_steps: int = 0
    max_train_steps: int = 500  # maybe up to 650
    checkpointing_steps: int = 1000
    # validation_epochs: int = 25


@dataclass
class AppConfig(SharedConfig):
    num_inference_steps: int = 50
    guidance_scale: float = 7.5  # todo higher?


IMG_PATH = Path("/img")


def load_images(image_urls):
    import PIL.Image
    from smart_open import open

    os.makedirs(IMG_PATH, exist_ok=True)
    for ii, url in enumerate(image_urls):
        with open(url, "rb") as f:
            image = PIL.Image.open(f)
            image.save(IMG_PATH / f"{ii}.png")
    log.info("Images loaded.")
    return IMG_PATH


@stub.function(
    image=image,
    gpu="A100",
    volumes={str(MODEL_DIR): stub.volume},
    timeout=60 * 50,
    secrets=[Secret.from_name("huggingface-secret", environment_name="main")],
)
def train(instance_example_urls):
    import subprocess

    import huggingface_hub
    from accelerate.utils import write_basic_config

    config = TrainConfig()
    img_path = load_images(instance_example_urls)
    os.makedirs(MODEL_DIR, exist_ok=True)
    write_basic_config(mixed_precision="fp16")
    hf_key = os.environ["HUGGINGFACE_TOKEN"]
    huggingface_hub.login(hf_key)

    instance_phrase = f"{config.instance_name} {config.class_name}"
    prompt = f"{config.prefix} {instance_phrase} {config.postfix}".strip()

    try:
        subprocess.run(
            [
                "accelerate",
                "launch",
                "diffusers/examples/dreambooth/train_dreambooth_lora_sdxl.py",
                "--train_text_encoder",
                f"--pretrained_model_name_or_path={config.model_name}",
                f"--instance_data_dir={img_path}",
                f"--output_dir={MODEL_DIR}",
                f"--mixed_precision=fp16",
                f"--instance_prompt='{prompt}'",
                f"--resolution={config.resolution}",
                f"--train_batch_size={config.train_batch_size}",
                f"--gradient_accumulation_steps={config.gradient_accumulation_steps}",
                f"--learning_rate={config.learning_rate}",
                f"--lr_scheduler={config.lr_scheduler}",
                f"--lr_warmup_steps={config.lr_warmup_steps}",
                f"--max_train_steps={config.max_train_steps}",
                f"--checkpointing_steps={config.checkpointing_steps}",
            ],
            check=True,
            capture_output=True,
        )
    except subprocess.CalledProcessError as exc:
        log.error(exc.stdout.decode())
        log.error(exc.stderr.decode())
        raise

    stub.volume.commit()


@stub.cls(
    gpu="A100",
    image=image,
    volumes={str(MODEL_DIR): stub.volume},
)
class Model:
    def __enter__(self):
        import torch
        from diffusers import StableDiffusionXLPipeline

        stub.volume.reload()
        pipe = StableDiffusionXLPipeline.from_pretrained(
            MODEL_DIR,
            torch_dtype=torch.float16,
            safety_checker=None,
        ).to("cuda")
        self.pipe = pipe

    @method()
    def inference(self, text):
        im = self.pipe(
            text,
            num_inference_steps=50,
            guidance_scale=7.5,
        ).images[0]
        return im


@stub.local_entrypoint()
def run():
    with open(TrainConfig().instance_example_urls_file) as f:
        instance_example_urls = [line.strip() for line in f.readlines()]
    train.remote(instance_example_urls)
