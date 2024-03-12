import os
import time
import base64
from typing import Any, Dict, List, Union

import modal
from modal import (
    Secret,
    Function,
    web_endpoint,
)
from fastapi import Header, Depends, status
from fastapi.responses import Response, JSONResponse

from sb_models.logger import log
from sb_models.network import api_req
from sb_models.types.request import SubstrateRequest
from sb_models.compose.compose import image
from sb_models.graph.public_nodes import (
    ALL_PUBLIC_NODES,
)
from sb_models.substratecore.models import ErrorOut

# TODO(ben): replace with new public .models (carefully! in use)
from sb_models.substratecore.deprecated_models import StableDiffusionXLIn
from sb_models.substratecore.stablediffusion_versions import ToStableDiffusionXLIn

stub = modal.Stub("api", image=image)


# TODO: This whole path is deprecated – remove once Substack stops calling
# NB This needs everything that compose.py has (secrets, dependencies, etc) because it basically does the same thing
@stub.function(
    secrets=[
        Secret.from_name("api-secret-key", environment_name="main"),
        Secret.from_name("anyscale-secret", environment_name="main"),
    ],
    image=image,
    allow_concurrent_inputs=15,
    keep_warm=2 if os.environ.get("MODAL_ENVIRONMENT", "main") == "main" else None,
    timeout=60,
    _experimental_boost=True,
)
@web_endpoint(method="POST")
async def api(
    args: Dict[str, Any],
    accept: str = Header(None),
    req: SubstrateRequest = Depends(api_req),  # noqa: B008
) -> Union[JSONResponse, Response]:
    from sb_models.graph.modal_nodes import ModalNode, ModalHandle

    t0 = time.time()
    x_substrate_version = None
    model_id = None
    if req and req.request:
        x_substrate_version = req.request.headers.get("x-substrate-version")
        model_id = req.request.headers.get("x-model-id")
    remote_models = {
        "sdxl": ModalHandle.stablediffusionxl,  # TODO: add aliases/rename
        "mistral-7b-instruct": ModalHandle.mistral7b_instruct,
        "jina-base-v2": ModalHandle.jinav2,
        "firellava": ModalHandle.firellava,
        "seamless": ModalHandle.seamless,
        "whisper": ModalHandle.whisper,
    }
    if model_id is None:
        error = ErrorOut(type="api_error", message="missing x-model-id")
        datadog = Function.lookup("datadog", "log")
        datadog.spawn(error={**error.dict(), "exception": error.dict()}, req=req)
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=error.dict())
    remote_model = remote_models.get(model_id)
    if remote_model is None:
        try:
            Klazz = ALL_PUBLIC_NODES[model_id]
            node = Klazz(**args)
            result = await node.run(req=req)
            return JSONResponse(status_code=status.HTTP_200_OK, content=result)
        except NameError:
            error = ErrorOut(type="api_error", message=f"could not find model {model_id}")
            datadog = Function.lookup("datadog", "log")
            datadog.spawn(error={**error.dict(), "exception": error.dict()}, req=req)
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=error.dict())

    variant_args = {}
    if model_id == "sdxl":
        if args.get("use_refiner") is not None:
            variant_args["use_refiner"] = args.get("use_refiner")
        if args.get("use_turbo") is not None:
            variant_args["use_turbo"] = args.get("use_turbo")

    model_node = ModalNode(model=remote_model, variant_args=variant_args)
    log.info(f"Loaded model in {time.time() - t0:.2f}s")
    result = None
    try:
        t1 = time.time()
        result = await model_node.run(req=req, **args)
        log.info(f"Ran API model in {time.time() - t1:.2f}s")
    except Exception as e:
        error = ErrorOut(type="api_error", message="unexpected error")
        datadog = Function.lookup("datadog", "log")
        datadog.spawn(error={**error.dict(), "exception": str(e)}, req=req)
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=error.dict())
    t2 = time.time()

    if isinstance(result, Dict) and "error" in result:
        datadog = Function.lookup("datadog", "log")
        datadog.spawn(error=result["error"], req=req)
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=result)

    # return base64 image data if accept header is image/*
    if model_id == "sdxl":
        data = None
        if isinstance(result, List):
            data = result
        elif isinstance(result, Dict) and "data" in result:
            data = result["data"]
        sdin = ToStableDiffusionXLIn(args).from_version(x_substrate_version)
        mime_types = [mime.strip() for mime in (accept or "").split(",")]
        if (
            data is not None
            and isinstance(sdin, StableDiffusionXLIn)
            and not sdin.store
            and any(mime.startswith("image/") for mime in mime_types)
        ):
            bytes_list = base64.b64decode(data[0].get("uri"))
            return Response(bytes_list, media_type="image/jpeg")

    log.info(f"Finish API model in {time.time() - t2:.2f}s")
    return JSONResponse(status_code=status.HTTP_200_OK, content={"data": result})
