# Download the full-precision weights of the Falcon-40B LLM but load it in 4-bit using
# Tim Dettmer's [`bitsandbytes`](https://github.com/TimDettmers/bitsandbytes) library. This enables it to fit
# into a single GPU (A100 40GB).
import os

from modal import Stub, Image, Secret, gpu, method, web_endpoint
from fastapi import Header
from pydantic import BaseModel


# Spec for an image where falcon-40b-instruct is cached locally
def download_falcon_40b():
    from huggingface_hub import snapshot_download

    model_name = "tiiuae/falcon-40b-instruct"
    snapshot_download(model_name)


image = (
    Image.micromamba()
    .micromamba_install(
        "cudatoolkit=11.7",
        "cudnn=8.1.0",
        "cuda-nvcc",
        "scipy",
        channels=["conda-forge", "nvidia"],
    )
    .apt_install("git")
    .pip_install(
        "bitsandbytes==0.39.0",
        "bitsandbytes-cuda117==0.26.0.post2",
        "peft @ git+https://github.com/huggingface/peft.git",
        "transformers @ git+https://github.com/huggingface/transformers.git",
        "accelerate @ git+https://github.com/huggingface/accelerate.git",
        "hf-transfer~=0.1",
        "torch",
        "torchvision",
        "sentencepiece==0.1.97",
        "huggingface_hub==0.16.4",
        "einops==0.6.1",
    )
    .env({"HF_HUB_ENABLE_HF_TRANSFER": "1"})
    .run_function(download_falcon_40b)
)

stub = Stub(image=image, name="falcon-40b")


@stub.cls(
    gpu=gpu.A100(),
    timeout=60 * 10,
    container_idle_timeout=60 * 5,
)
class Falcon40B:
    def __enter__(self):
        import torch
        from transformers import (
            AutoTokenizer,
            BitsAndBytesConfig,
            AutoModelForCausalLM,
        )

        model_name = "tiiuae/falcon-40b-instruct"

        nf4_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=False,
            bnb_4bit_compute_dtype=torch.bfloat16,
        )

        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            trust_remote_code=True,
            local_files_only=True,
            device_map="auto",
            quantization_config=nf4_config,
        )
        model.eval()

        tokenizer = AutoTokenizer.from_pretrained(
            model_name,
            trust_remote_code=True,
            local_files_only=True,
            device_map="auto",
        )
        tokenizer.bos_token_id = 1

        self.model = torch.compile(model)
        self.tokenizer = tokenizer

    @method()
    def generate(self, prompt: str):
        from threading import Thread

        from transformers import GenerationConfig, TextIteratorStreamer

        tokenized = self.tokenizer(prompt, return_tensors="pt")
        input_ids = tokenized.input_ids
        input_ids = input_ids.to(self.model.device)

        generation_config = GenerationConfig(
            do_sample=True,
            temperature=0.1,
            max_new_tokens=512,
        )

        streamer = TextIteratorStreamer(self.tokenizer, skip_special_tokens=True)
        generate_kwargs = dict(
            input_ids=input_ids,
            generation_config=generation_config,
            return_dict_in_generate=True,
            eos_token_id=self.tokenizer.eos_token_id,
            pad_token_id=self.tokenizer.eos_token_id,
            bos_token_id=self.tokenizer.bos_token_id,
            attention_mask=tokenized.attention_mask,
            output_scores=True,
            streamer=streamer,
        )

        thread = Thread(target=self.model.generate, kwargs=generate_kwargs)
        thread.start()
        for new_text in streamer:
            print(new_text, end="")  # noqa: T201
            yield new_text

        thread.join()


prompt_template = (
    "A chat between a curious human user and an artificial intelligence assistant. The assistant give a helpful, detailed, and accurate answer to the user's question."
    "\n\nUser:\n{}\n\nAssistant:\n"
)


@stub.local_entrypoint()
def cli(prompt: str = None):
    question = prompt or "What are the main differences between Python and JavaScript programming languages?"
    model = Falcon40B()
    for text in model.generate.call(prompt_template.format(question)):
        print(text, end="", flush=True)  # noqa: T201


class APIArgs(BaseModel):
    q: str


@stub.function(
    timeout=60 * 10,
    secrets=[Secret.from_name("api-secret-key", environment_name="main")],
)
@web_endpoint(method="POST")
def api(
    args: APIArgs,
    x_modal_secret: str = Header(None),
):
    from itertools import chain

    from fastapi.responses import StreamingResponse

    secret = os.environ["API_SECRET_KEY"]
    if secret and x_modal_secret != secret:
        return {"error": "Not authorized"}

    model = Falcon40B()
    return StreamingResponse(
        chain(
            (args.q + "\n\n"),
            ("Loading model...\n\n"),
            model.generate.call(prompt_template.format(args.q)),
        ),
        media_type="text/event-stream",
    )
