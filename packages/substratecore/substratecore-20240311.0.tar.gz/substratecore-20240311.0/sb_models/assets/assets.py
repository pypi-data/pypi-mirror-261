import os
from os.path import isfile
from pathlib import Path

from modal import Stub, Image, NetworkFileSystem, web_endpoint
from fastapi import Request
from fastapi.responses import Response, FileResponse

from sb_models.logger import log

image = Image.debian_slim()
stub = Stub("assets", image=image)
assets_nfs = NetworkFileSystem.persisted("assets-nfs")

ROOT_PATH = Path("/assets")


@stub.function(
    network_file_systems={ROOT_PATH: assets_nfs},
    keep_warm=1 if os.environ.get("MODAL_ENVIRONMENT", "main") == "main" else None,
)
@web_endpoint(label="ss-assets")
def assets(request: Request):
    key = request.query_params["file_key"]
    model = request.query_params["model"]
    pth = ROOT_PATH / model / key
    if isfile(pth):
        return FileResponse(pth)
    else:
        log.warning(f"File not found: {pth}")
        return Response("Not found", status_code=404)
