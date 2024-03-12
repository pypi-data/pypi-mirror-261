import os

from modal import Stub, Image, gpu, build, enter, method

from sb_models.logger import log

GPU_TYPE = gpu.H100()
CACHE_DIR = "/cache"
MODEL_ID = "stabilityai/sdxl-turbo"
ENGINE_DIR = "engine-sdxl-turbo"

image = (
    Image.from_registry("nvcr.io/nvidia/pytorch:23.11-py3")
    .apt_install("libsm6", "libxext6", "ffmpeg")
    .pip_install(
        "tensorrt==9.3.0.post12.dev1",
        extra_index_url="https://pypi.nvidia.com",
    )
    .pip_install(
        "accelerate",
        "colored",
        "ftfy",
        "nvtx",
        "opencv-python==4.8.0.74",
        "scipy",
        "transformers==4.31.0",
        "onnxruntime==1.16.1",
        "onnx==1.14.0",
        "safetensors",
        "hf_transfer",
        "diffusers==0.23.1",
        "invisible-watermark>=0.2.0",
    )
    .pip_install("polygraphy==0.49.0")
)


stub = Stub("sdxltrt-turbo", image=image)

with stub.image.imports():
    import time
    import base64
    from io import BytesIO
    from typing import Any

    import torch
    import tensorrt as trt
    from PIL import Image
    from cuda import cudart
    from diffusers import AutoencoderKL, DiffusionPipeline, DPMSolverMultistepScheduler
    from huggingface_hub import snapshot_download

    from sb_models.sdxl.sdtrt.trtclip import TRTClip
    from sb_models.sdxl.sdtrt.trtunet import TRTUnet

    torch.backends.cuda.matmul.allow_tf32 = True


@stub.cls(
    gpu=GPU_TYPE,
    concurrency_limit=1,
)
class SDXLTRT:
    @build()
    def build(self):
        snapshot_download(repo_id="substrate-labs/sdxl-turbo-trt-9.3.0.post12.dev1", local_dir=CACHE_DIR)
        vae = AutoencoderKL.from_pretrained(
            "madebyollin/sdxl-vae-fp16-fix", torch_dtype=torch.float16, cache_dir=CACHE_DIR
        )
        self.pipe = DiffusionPipeline.from_pretrained(
            MODEL_ID,
            vae=vae,
            torch_dtype=torch.float16,
            variant="fp16",
            use_safetensors=True,
            cache_dir=CACHE_DIR,
        )

        cuda_stream = cudart.cudaStreamCreate()[1]
        self.pipe.unet.to(memory_format=torch.channels_last)
        self.pipe.to("cuda")
        self.pipe.unet = _wrap_in_tunet(self.pipe.unet, ENGINE_DIR, cuda_stream)
        self.pipe.text_encoder = _wrap_in_trtclip(self.pipe.text_encoder, ENGINE_DIR, cuda_stream)
        self.pipe.text_encoder_2 = _wrap_in_trtclip2(self.pipe.text_encoder_2, ENGINE_DIR, cuda_stream)

    @enter()
    def load(self):
        start_time = time.time()
        vae = AutoencoderKL.from_pretrained(
            "madebyollin/sdxl-vae-fp16-fix", torch_dtype=torch.float16, cache_dir=CACHE_DIR, local_files_only=True
        )
        self.pipe = DiffusionPipeline.from_pretrained(
            MODEL_ID,
            vae=vae,
            torch_dtype=torch.float16,
            variant="fp16",
            use_safetensors=True,
            cache_dir=CACHE_DIR,
            local_files_only=True,
        )

        cuda_stream = cudart.cudaStreamCreate()[1]
        self.pipe.unet.to(memory_format=torch.channels_last)
        self.pipe.to("cuda")
        self.pipe.unet = _wrap_in_tunet(self.pipe.unet, ENGINE_DIR, cuda_stream)
        self.pipe.text_encoder = _wrap_in_trtclip(self.pipe.text_encoder, ENGINE_DIR, cuda_stream)
        self.pipe.text_encoder_2 = _wrap_in_trtclip2(self.pipe.text_encoder_2, ENGINE_DIR, cuda_stream)
        end_time = time.time() - start_time
        log.info(f"loaded engine: {end_time:.2f} seconds")

        start_time = time.time()
        self.pipe(
            prompt="don quixote",
            num_inference_steps=3,
            guidance_scale=0,
            output_type="pil",
        )
        end_time = time.time() - start_time
        log.info(f"warm up: {end_time:.2f} seconds")

    def convert_to_b64(self, image: Image) -> str:
        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        img_b64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
        return img_b64

    @method()
    def generate(self, model_input: Any) -> Any:
        prompt = model_input.pop("prompt")
        negative_prompt = model_input.pop("negative_prompt", None)
        num_inference_steps = model_input.pop("num_inference_steps", 4)
        guidance_scale = model_input.pop("guidance_scale", 0)
        seed = model_input.pop("seed", None)

        scheduler = model_input.pop("scheduler", None)  # Default: EulerDiscreteScheduler

        # See schedulers: https://huggingface.co/docs/diffusers/api/schedulers/overview
        if scheduler == "DPM++ 2M":
            self.pipe.scheduler = DPMSolverMultistepScheduler.from_config(self.pipe.scheduler.config)
        elif scheduler == "DPM++ 2M Karras":
            # DPM++ 2M Karras (for < 30 steps, when speed matters)
            self.pipe.scheduler = DPMSolverMultistepScheduler.from_config(
                self.pipe.scheduler.config, use_karras_sigmas=True
            )
        elif scheduler == "DPM++ 2M SDE Karras":
            # DPM++ 2M SDE Karras (for 30+ steps, when speed doesn't matter)
            self.pipe.scheduler = DPMSolverMultistepScheduler.from_config(
                self.pipe.scheduler.config,
                algorithm_type="sde-dpmsolver++",
                use_karras_sigmas=True,
            )

        generator = None
        if seed is not None:
            torch.manual_seed(seed)
            generator = [torch.Generator(device="cuda").manual_seed(seed)]

        start_time = time.time()
        im = self.pipe(
            prompt=prompt,
            negative_prompt=negative_prompt,
            generator=generator,
            num_inference_steps=num_inference_steps,
            guidance_scale=guidance_scale,
            output_type="pil",
        ).images[0]
        end_time = time.time() - start_time

        log.info(f"gen time: {end_time:.3f} seconds")

        b64_results = self.convert_to_b64(im)

        return {"status": "success", "data": b64_results, "time": end_time}


def _wrap_in_tunet(unet, engine_dir_name, stream):
    return _wrap_in_trt(unet, engine_dir_name, "unetxl", TRTUnet, stream)


def _wrap_in_trtclip(clip, engine_dir_name, stream):
    return _wrap_in_trt(clip, engine_dir_name, "clip", TRTClip, stream, is_clip2=False)


def _wrap_in_trtclip2(clip, engine_dir_name, stream):
    return _wrap_in_trt(clip, engine_dir_name, "clip2", TRTClip, stream, is_clip2=True)


def _wrap_in_trt(model, engine_dir_name, engine_name, trt_class, stream, **kwargs):
    model.to("cpu")
    torch.cuda.empty_cache()
    trt_model = trt_class(
        model,
        stream=stream,
        engine_path=f"{CACHE_DIR}/{engine_dir_name}/{engine_name}.trt{trt.__version__}.plan",
        **kwargs,
    )
    trt_model.load()
    return trt_model


@stub.local_entrypoint()
def sample(prompt: str = "high quality, lion in the desert, photo"):
    img = SDXLTRT().generate.remote({"prompt": prompt, "num_inference_steps": 2})

    import time
    import hashlib

    file_hash = hashlib.md5(f"{prompt}-{int(time.time())}".encode("utf-8")).hexdigest()
    im = base64.b64decode(img["data"])
    output_path = os.path.expanduser(f"~/Downloads/sdxl_{file_hash}.png")
    log.info(f"Saving {output_path}")
    with open(output_path, "wb") as f:
        f.write(im)
    os.system(f"open {output_path}")
