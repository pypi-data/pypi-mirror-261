import os
import time
import subprocess

from modal import Stub, Image

from sb_models.logger import log

# from .sdxl.sdxlonnx import stub, image, volume, MODEL_DIR

# from .flag_embedding.flag_embedding import stub, image
# from .sdxl.sd_trt import stub, image


i = Image.debian_slim("3.10").apt_install("postgresql").apt_install("postgresql-contrib")
stub = Stub("debugger", image=i)
debug_image = (
    i.apt_install("curl")
    .apt_install("build-essential")
    .run_commands("curl https://sh.rustup.rs -sSf | bash -s -- -y")
    .run_commands(". $HOME/.cargo/env && cargo install bore-cli")
    .pip_install("jupyter")
)

TIMEOUT = 60 * 180


@stub.function(
    image=debug_image,
    concurrency_limit=1,
    timeout=TIMEOUT,
    # gpu="A100",
    # volumes={MODEL_DIR: volume},
)
def run_jupyter(timeout: int):
    jupyter_process = subprocess.Popen(
        [
            "jupyter",
            "notebook",
            "--no-browser",
            "--allow-root",
            "--port=8888",
            "--NotebookApp.allow_origin='*'",
            "--NotebookApp.allow_remote_access=1",
        ],
        env={
            **os.environ,
            "JUPYTER_TOKEN": "Mccfgt8DzMpTLOee3fb2n0M+0DnpiZKjccPQ6Li6dyU=",
        },
    )

    bore_process = subprocess.Popen(
        ["/root/.cargo/bin/bore", "local", "8888", "--to", "bore.pub"],
    )

    try:
        end_time = time.time() + timeout
        while time.time() < end_time:
            time.sleep(5)
        log.info(f"Reached end of {timeout} second timeout period. Exiting...")
    except KeyboardInterrupt:
        log.info("Exiting...")
    finally:
        bore_process.kill()
        jupyter_process.kill()


@stub.local_entrypoint()
def jupyter(timeout: int = TIMEOUT):
    # print("hello")
    run_jupyter.remote(timeout=timeout)
