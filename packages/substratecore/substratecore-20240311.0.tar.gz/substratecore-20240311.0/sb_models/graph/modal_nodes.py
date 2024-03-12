import os
import inspect
import dataclasses
from typing import Any, Dict, List, Tuple, Union, Optional

from modal import Cls, Function
from pydantic import BaseModel

from sb_models.logger import log
from sb_models.graph.node import Node
from sb_models.types.outputs import InferenceRun, InferenceError
from sb_models.types.request import SubstrateRequest
from sb_models.fallback.anyscale import execute_anyscale_fallback
from sb_models.substratecore.models import ErrorOut
from sb_models.substratecore.jina_versions import ToJinaIn, FromJinaOut
from sb_models.substratecore.mistral_versions import ToMistralIn, FromMistralOut

# NOTE: Legacy internal model versioning, for Substack
from sb_models.substratecore.stablediffusion_versions import (
    ToStableDiffusionXLIn,
    FromStableDiffusionOut,
)


@dataclasses.dataclass
class ModalConfig:
    name: str
    """
    the name of the model
    """
    remote_handle: Tuple[str, str]
    """
    the remote function path
    """
    orb_event_name: Optional[str] = None
    """
    the event name, used for reporting usage to orb
    NOTE: This is only used to override using `name` as the event name.
    TODO: Remove this entirely
    """
    version_transforms: Optional[Tuple[Any, Any]] = None
    """
    Version transforms for the model.
    NOTE: LEGACY – This is to support API changes we made for Substack, which
    uses raw model nodes. This won't be supported in the future.
    """

    def __hash__(self):
        return hash((self.name, self.orb_event_name))


class ModalHandle:
    """
    NOTE: Naming convention:
    - Use hyphens for the main model name
    - Only use underscores when there are multiple variants, e.g. _controlnet, _large
    """

    stablediffusionxl = ModalConfig(
        name="sdxl",  # TODO: rename to stablediffusion-xl
        orb_event_name="stablediffusion-xl",  # TODO: remove name override
        remote_handle=("sdxl", "SDXL.generate"),
        version_transforms=(ToStableDiffusionXLIn, FromStableDiffusionOut),
    )
    mistral7b_instruct = ModalConfig(
        name="mistral-7b-instruct",  # TODO: rename to mistral-7b_instruct
        orb_event_name="mistral-7b",  # TODO: remove name override
        remote_handle=("mistral-7b-instruct", "Mistral.generate"),
        version_transforms=(ToMistralIn, FromMistralOut),
    )
    jinav2 = ModalConfig(
        name="jina-base-v2",  # TODO: rename to jina-v2
        orb_event_name="jina-v2",  # TODO: remove name override
        remote_handle=("jina-base-v2", "Embeddings.run_embed"),
        version_transforms=(ToJinaIn, FromJinaOut),
    )
    firellava = ModalConfig(
        name="firellava",  # TODO: rename to firellava-13b
        orb_event_name="firellava-13b",  # TODO: remove name override
        remote_handle=("firellava", "Firellava.generate"),
    )
    stablediffusionxl_lightning = ModalConfig(
        name="stablediffusion-xl_lightning",
        remote_handle=("sdxl_lightning", "SDXL.generate"),
    )
    stablediffusionxl_controlnet_depth = ModalConfig(
        name="stablediffusion-xl_controlnet_depth",
        remote_handle=("sdxl_controlnet_depth", "SDXL.generate"),
    )
    stablediffusionxl_controlnet_edge = ModalConfig(
        name="stablediffusion-xl_controlnet_edge",
        remote_handle=("sdxl_controlnet_edge", "SDXL.generate"),
    )
    stablediffusionxl_controlnet_qr = ModalConfig(
        name="stablediffusion-xl_controlnet_qr",
        remote_handle=("sdxl_controlnet_qr", "SDXL.generate"),
    )
    stablediffusion1_5_controlnet_qr = ModalConfig(
        name="stablediffusion-1.5_controlnet_qr",
        remote_handle=("sd1_5_controlnet_qr", "SD.generate"),
    )
    stablediffusion1_5_controlnet_tile = ModalConfig(
        name="stablediffusion-1.5_controlnet_tile",
        remote_handle=("sd1_5_controlnet_tile", "SD.generate"),
    )
    stablediffusionxl_inpaint = ModalConfig(
        name="stablediffusion-xl_inpaint",
        remote_handle=("sdxl_inpaint", "SDXL.generate"),
    )
    stablediffusionxl_ipadapter = ModalConfig(
        name="stablediffusion-xl_ipadapter",
        remote_handle=("sdxl_ipadapter", "SDXL.generate"),
    )
    stablediffusionxl_inpaint_ipadapter = ModalConfig(
        name="stablediffusion-xl_inpaint_ipadapter",
        remote_handle=("sdxl_inpaint_ipadapter", "SDXL.generate"),
    )
    mistral8x7b_instruct = ModalConfig(
        name="mistral-8x7b_instruct",
        remote_handle=("mistral-8x7b-instruct", "Mixtral.generate"),
    )
    clip = ModalConfig(
        name="clip",
        remote_handle=("clip", "CLIP.embed"),
    )
    whisper = ModalConfig(  # TranscribeMedia
        name="whisper-v3",
        remote_handle=("whisper", "Transcriber.transcribe"),
    )
    segment_anything = ModalConfig(  # DetectSegments
        name="segmentanything",
        remote_handle=("SAM", "SAM.segment"),
    )
    grounding_dino_base = ModalConfig(  # DetectObjects
        name="groundingdino-base",
        remote_handle=("grounding_dino_base", "GD.detect"),
    )
    grounding_dino_tiny = ModalConfig(  # DetectObjects
        name="groundingdino-tiny",
        remote_handle=("grounding_dino_tiny", "GD.detect"),
    )
    xtts = ModalConfig(  # GenerateSpeech
        name="xtts-v2",
        remote_handle=("xtts", "XTTS.generate"),
    )
    lama = ModalConfig(  # FillMask
        name="biglama",
        remote_handle=("lama", "Lama.generate"),
    )
    isnet = ModalConfig(  # RemoveBackground
        name="isnet",
        remote_handle=("isnet", "ISNet.generate"),
    )
    esrgan = ModalConfig(  # UpscaleImage
        name="realesrgan",
        remote_handle=("esrgan", "ESRGAN.generate"),
    )
    svd = ModalConfig(  # AnimateImage
        name="stablevideodiffusion-xt",
        remote_handle=("svd", "SVD.generate"),
    )
    # Private models
    bakllava = ModalConfig(
        name="bakllava-1",
        remote_handle=("bakllava-1", "Bakllava.generate"),
    )
    seamless = ModalConfig(
        name="seamless",
        remote_handle=("seamless", "Seamless.run"),
    )
    bark = ModalConfig(
        name="bark",
        remote_handle=("bark", "tts"),
    )


def _serialize_result(result: Any) -> Any:
    if isinstance(result, List):
        # List[List[BaseModel]]
        if all(isinstance(sublist, List) for sublist in result):
            return [[x.dict() if isinstance(x, BaseModel) else x for x in sublist] for sublist in result]
        # List[BaseModel]
        else:
            return [x.dict() if isinstance(x, BaseModel) else x for x in result]
    # BaseModel
    elif isinstance(result, BaseModel):
        return result.dict()
    return result


class ModalNode(Node):
    _modal_handles = []

    @property
    def modal_handles(self):
        if len(self._modal_handles) == 0:
            self._modal_handles = [
                getattr(ModalHandle, attr)
                for attr in dir(ModalHandle)
                if not inspect.isroutine(getattr(ModalHandle, attr)) and not attr.startswith("__")
            ]
        return self._modal_handles

    def __init__(
        self,
        model: Union[ModalConfig, str],
        variant_args=None,
        environment=None,
        **attr,
    ):
        self.environment = environment
        model_arg = model or attr.get("model")
        if isinstance(model_arg, str):
            self.modal_handle = next((m for m in self.modal_handles if m.name == model_arg), None)
        else:
            self.modal_handle = model_arg
        if not isinstance(self.modal_handle, ModalConfig):
            raise ValueError(f"model not found: {model}")
        self.ss_path = self.modal_handle.orb_event_name or self.modal_handle.name
        self.variant_args = variant_args
        if "model" in attr:
            del attr["model"]

        super().__init__(**attr)

    def to_dict(self):
        super_dict = super().to_dict()
        return {
            **super_dict,
            "extra_args": {
                "model": self.modal_handle,
                "variant_args": self.variant_args,
            },
        }

    def _get_fn(self):
        stub, handle = self.modal_handle.remote_handle
        # if handle has a period in it, it's a class lookup
        if "." in handle and self.variant_args:
            clazz, fname = handle.split(".")
            Model = Cls.lookup(
                stub,
                clazz,
                environment_name=self.environment if self.environment else None,
            )
            fn = Model(**self.variant_args).__getattr__(fname)
        else:
            fn = Function.lookup(
                stub,
                handle,
                environment_name=self.environment if self.environment else None,
            )
        return fn

    async def _execute_fn(self, fn, args, req):
        error_dict = None
        try:
            res = None
            if self.modal_handle == ModalHandle.mistral7b_instruct:
                res = await execute_anyscale_fallback(fn, args, req)
                if not res:
                    log.info("anyscale mistral path aborted")
            if not res:
                res = await fn.remote.aio(**args, req=req)
            if isinstance(res, InferenceError):
                message = res.error_message or "Unexpected Error"
                error = ErrorOut(type="api_error", message=message)
                error_dict = {"error": error.dict()}
            elif res:
                return res, None
            else:
                error = ErrorOut(type="api_error", message="Unexpected error")
                error_dict = {"error": error.dict()}
        except Exception as e:
            error = ErrorOut(type="api_error", message="Unexpected error")
            log.error("exception", str(e))
            datadog = Function.lookup("datadog", "log")
            datadog.spawn(error={**error.dict(), "exception": str(e)}, req=req)
            error_dict = {"error": error.dict()}

        return None, error_dict

    async def run(self, req: Optional[SubstrateRequest] = None, **args) -> Union[Dict, List, BaseModel]:
        x_substrate_version = None
        if req and req.request:
            x_substrate_version = req.request.headers.get("x-substrate-version")

        res = {}
        usage = None
        fn = self._get_fn()
        # NOTE: Legacy ModelNodes used by Substack have version transforms: Mistral, Jina, SDXL
        if self.modal_handle and self.modal_handle.version_transforms:
            versioned_in = args
            in_transform = self.modal_handle.version_transforms[0]
            if in_transform:
                versioned_in = in_transform(args).from_version(x_substrate_version)
            if isinstance(versioned_in, ErrorOut):
                return {"error": versioned_in.dict()}
            elif isinstance(versioned_in, BaseModel):
                excluded_args = versioned_in.dict(exclude=set(self.variant_args or {}), exclude_none=True)
                res, error = await self._execute_fn(fn, excluded_args, req)
                if error:
                    return error
            inf_run: InferenceRun = res
            usage = inf_run.usage

            # Legacy versioning transforms
            # TODO: Remove once Substack moves to higher-order nodes
            data = _serialize_result(inf_run.result)
            out_transform = self.modal_handle.version_transforms[1]
            if out_transform:
                data = out_transform(data).to_version(x_substrate_version)
            # Final transforms
            # TODO: rethink this with higher-order nodes
            if x_substrate_version and x_substrate_version < "2023-12-26":
                res = data
            else:
                # wrap in `data`
                if isinstance(data, list) or isinstance(data, List):
                    res = {"data": {"items": data}}
                else:
                    res = {"data": data}
        else:
            res, error = await self._execute_fn(fn, args, req)
            if error:
                return error
            if isinstance(res, InferenceRun):
                usage = res.usage
                res = _serialize_result(res.result)
            else:
                res = _serialize_result(res)

        if usage is not None and req is not None and os.environ.get("MODAL_ENVIRONMENT") == "main":
            notify_usage = Function.lookup("substrate-usage", "notify_usage")
            metadata = usage.dict()
            if req.graph_id:
                metadata["graph_id"] = req.graph_id
            notify_usage.spawn(
                user_id=req.user_id,
                organization_id=req.organization_id,
                path=self.ss_path,
                metadata=metadata,
                req=req,
            )

        return res
