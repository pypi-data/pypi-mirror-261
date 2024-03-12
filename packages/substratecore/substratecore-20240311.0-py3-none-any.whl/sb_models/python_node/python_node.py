import json
from typing import Dict, List
from pathlib import Path
from tempfile import TemporaryDirectory

from modal import Stub, Image, Mount

image = Image.debian_slim("3.10")
stub = Stub("python-runner", image=image)


@stub.function()
def run(
    code_str: str,
    python_version: str = None,
    apt_deps: List = None,
    pip_deps: List = None,
    **args,
):
    local_dir = Path(TemporaryDirectory().name)
    _write_files({"main.py": code_str}, local_dir)
    sandbox = stub.spawn_sandbox(
        "bash",
        "-c",
        f"python -m main --kwargs '{json.dumps(args)}'",
        image=_get_image(python_version, apt_deps, pip_deps),
        mounts=[Mount.from_local_dir(local_dir, remote_path="/sb")],
        secrets=[],
        timeout=60,
        workdir="/sb",
    )
    sandbox.wait()
    output = sandbox.stdout.read()
    loaded = json.loads(output)
    return {"output": loaded["__ss_result__"]}


def _get_image(python_version: str = None, apt_deps: List = None, pip_deps: List = None):
    if not apt_deps and not pip_deps:
        return Image.debian_slim(python_version or "3.10")
    if not apt_deps:
        return Image.debian_slim(python_version or "3.10").pip_install(pip_deps)
    if not pip_deps:
        return Image.debian_slim(python_version or "3.10").apt_install(apt_deps)
    return Image.debian_slim(python_version or "3.10").apt_install(apt_deps).pip_install(pip_deps)


def _write_files(code: Dict[str, str], to_dir: Path):
    for file_path, contents in code.items():
        p = to_dir / file_path
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "w") as f:
            f.write(contents)
