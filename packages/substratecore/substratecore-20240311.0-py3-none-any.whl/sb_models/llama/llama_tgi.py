import os
from pathlib import Path

from modal import Stub, Image, Mount, Secret, gpu, method, asgi_app
from fastapi import Header
from pydantic import BaseModel

from sb_models.logger import log

GPU_CONFIG = gpu.A100(memory=80, count=2)
MODEL_ID = "meta-llama/Llama-2-70b-chat-hf"
# Add `["--quantize", "gptq"]` for TheBloke GPTQ models.
LAUNCH_FLAGS = ["--model-id", MODEL_ID]


def download_model():
    from huggingface_hub import snapshot_download

    snapshot_download(MODEL_ID, ignore_patterns="*.bin")


image = (
    Image.from_registry("ghcr.io/huggingface/text-generation-inference:sha-e605c2a")
    .dockerfile_commands("ENTRYPOINT []")
    .run_function(
        download_model,
        secret=Secret.from_name("huggingface-secret", environment_name="main"),
        timeout=60 * 30,
    )
    .pip_install("text-generation")
)

stub = Stub("llama-2-70b", image=image)


@stub.cls(
    secret=Secret.from_name("huggingface-secret", environment_name="main"),
    gpu=GPU_CONFIG,
    allow_concurrent_inputs=10,
    container_idle_timeout=60 * 10,
    timeout=60 * 60,
)
class Model:
    def __enter__(self):
        import time
        import socket
        import subprocess

        from text_generation import AsyncClient

        self.launcher = subprocess.Popen(["text-generation-launcher"] + LAUNCH_FLAGS)
        self.client = AsyncClient("http://0.0.0.0:80", timeout=60)
        self.template = """<s>[INST] <<SYS>>
{system}
<</SYS>>

{user} [/INST] """

        # Poll until webserver at 0.0.0.0:80 accepts connections before running inputs.
        def webserver_ready():
            try:
                socket.create_connection(("0.0.0.0", 80), timeout=1).close()
                return True
            except (socket.timeout, ConnectionRefusedError):
                return False

        while not webserver_ready():
            time.sleep(1.0)

        log.info("Webserver ready!")

    def __exit__(self, _exc_type, _exc_value, _traceback):
        self.launcher.terminate()

    @method()
    async def generate(self, question: str):
        prompt = self.template.format(system="", user=question)
        result = await self.client.generate(prompt, max_new_tokens=1024)

        return result.generated_text

    @method()
    async def generate_stream(self, question: str):
        prompt = self.template.format(system="", user=question)

        async for response in self.client.generate_stream(prompt, max_new_tokens=1024):
            if not response.token.special:
                yield response.token.text


@stub.local_entrypoint()
def main():
    log.info(Model().generate.remote("Implement a Python function to compute the Fibonacci numbers."))


frontend_path = Path(__file__).parent / "llm-frontend"


class APIArgs(BaseModel):
    q: str


@stub.function(
    mounts=[
        Mount.from_local_dir(frontend_path, remote_path="/assets"),
    ],
    secrets=[Secret.from_name("api-secret-key", environment_name="main")],
    allow_concurrent_inputs=10,
    timeout=60 * 10,
)
@asgi_app()
def api():
    import json

    import fastapi.staticfiles
    from fastapi.responses import StreamingResponse

    web_app = fastapi.FastAPI()

    @web_app.get("/stats")
    async def stats():
        stats = await Model().generate_stream.get_current_stats().aio()
        return {
            "backlog": stats.backlog,
            "num_total_runners": stats.num_total_runners,
        }

    @web_app.post("/")
    async def completion(
        args: APIArgs,
        x_modal_secret: str = Header(None),
    ):
        from urllib.parse import unquote

        secret = os.environ["API_SECRET_KEY"]
        if secret and x_modal_secret != secret:
            return {"error": "Not authorized"}

        response = await Model().generate.remote(unquote(args.q))
        return {"completion": response}

    @web_app.get("/completion/{question}")
    async def completion(question: str):
        from urllib.parse import unquote

        def generate():
            for text in Model().generate_stream.remote_gen.aio(unquote(question)):
                yield f"data: {json.dumps(dict(text=text), ensure_ascii=False)}\n\n"

        return StreamingResponse(generate(), media_type="text/event-stream")

    web_app.mount("/", fastapi.staticfiles.StaticFiles(directory="/assets", html=True))
    return web_app
