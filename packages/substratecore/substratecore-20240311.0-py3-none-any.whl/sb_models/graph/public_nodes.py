import json
from typing import Any, Dict, Type, Union, TypeVar, Optional

from pydantic import BaseModel, ValidationError

from sb_models.logger import log
from sb_models.graph.node import Node
from sb_models.types.outputs import FirellavaOut
from sb_models.types.request import SubstrateRequest
from sb_models.graph.modal_nodes import ModalNode, ModalConfig, ModalHandle
from sb_models.substratecore.models import (
    ErrorOut,
    FillMaskIn as FillMaskInPD,
    EmbedTextIn as EmbedTextInPD,
    FillMaskOut,
    EmbedImageIn as EmbedImageInPD,
    EmbedTextOut,
    EmbedImageOut,
    GenerateTextIn as GenerateTextInPD,
    ResponseFormat,
    UpscaleImageIn as UpscaleImageInPD,
    GenerateImageIn as GenerateImageInPD,
    GenerateTextOut,
    UpscaleImageOut,
    DetectSegmentsIn as DetectSegmentsInPD,
    GenerateImageOut,
    GenerateSpeechIn as GenerateSpeechInPD,
    MultiEmbedTextIn as MultiEmbedTextInPD,
    DetectSegmentsOut,
    GenerateSpeechOut,
    MultiEmbedImageIn as MultiEmbedImageInPD,
    MultiEmbedTextOut,
    TranscribeMediaIn as TranscribeMediaInPD,
    MultiEmbedImageOut,
    RemoveBackgroundIn as RemoveBackgroundInPD,
    TranscribeMediaOut,
    MultiGenerateTextIn as MultiGenerateTextInPD,
    RemoveBackgroundOut,
    GenerateTextVisionIn as GenerateTextVisionInPD,
    MultiGenerateImageIn as MultiGenerateImageInPD,
    MultiGenerateTextOut,
    GenerateTextVisionOut,
    GenerativeEditImageIn as GenerativeEditImageInPD,
    MultiGenerateImageOut,
    GenerativeEditImageOut,
    ControlledGenerateImageIn as ControlledGenerateImageInPD,
    ControlledGenerateImageOut,
    MultiGenerativeEditImageIn as MultiGenerativeEditImageInPD,
    MultiGenerativeEditImageOut,
    MultiControlledGenerateImageIn as MultiControlledGenerateImageInPD,
    MultiControlledGenerateImageOut,
)
from sb_models.substratecore.deprecated_models import (
    MistralResult,
)

T = TypeVar("T", bound=BaseModel)


class PublicNode(Node):
    def construct_in_model(self, in_model_type: Type[T], req: Optional[SubstrateRequest], **args) -> Union[T, ErrorOut]:
        full_args = {**self.args, **args}
        # TODO implement versioning
        in_model = None
        try:
            in_model = in_model_type(**full_args)
        except ValidationError as e:
            e_json_str = e.json()
            e_json = json.loads(e_json_str)[0]
            message = f"{e_json.get('msg')}: {e_json.get('loc')}"
            error = ErrorOut(type="invalid_request_error", message=message)
            return error
        return in_model

    def to_dict(self):
        super_dict = super().to_dict()
        return {
            **super_dict,
            "node": self.__class__.__name__,
        }

    def construct_out_model(self, out_model: BaseModel, req: Optional[SubstrateRequest]) -> Dict[str, Any]:
        # TODO implement versioning – this is either an ErrorOut or BaseModel
        return out_model.dict()

    async def run(self, req: Optional[SubstrateRequest] = None, **args) -> Dict:
        raise NotImplementedError


def unexpected_error() -> ErrorOut:
    return ErrorOut(type="api_error", message="Unexpected error")


def temperature_to_temperature(temperature: Union[int, None]) -> Union[float, None]:
    """
    Poorly named conversion from [1,10] temperature to mistral's (assumed) [0,2] temperature
    TODO: validate this is the correct range
    """
    if temperature is None:
        return None
    return (temperature / 10) * 2.0


def response_format_to_json_schema(response_format: Union[ResponseFormat, None]) -> Union[str, None]:
    json_schema_str = None
    if response_format and response_format == ResponseFormat.json:
        json_schema_str = json.dumps(response_format.json_schema)
    return json_schema_str


class GenerateText(PublicNode):
    async def run(self, req: Optional[SubstrateRequest] = None, **args) -> Dict[str, Any]:
        in_model = self.construct_in_model(GenerateTextInPD, req, **args)
        if isinstance(in_model, ErrorOut):
            return self.construct_out_model(in_model, req)

        node = ModalNode(model=ModalHandle.mistral7b_instruct)
        try:
            res = await node.run(
                req=req,
                prompts=[{"prompt": in_model.prompt}],
                temperature=temperature_to_temperature(in_model.temperature),
                max_tokens=in_model.max_tokens,
                json_schema=response_format_to_json_schema(in_model.response_format),
                num_completions=1,
            )
            result_dict = res["data"]["items"][0]
            result = MistralResult(**result_dict)
            if result.completions:
                text = result.completions[0]
                out = GenerateTextOut(text=text)
                return self.construct_out_model(out, req)
            elif result.json_completions:
                json_object = result.json_completions[0]
                out = GenerateTextOut(json_object=json_object)
                return self.construct_out_model(out, req)
            else:
                return self.construct_out_model(unexpected_error(), req)
        except Exception as e:
            return self.construct_out_model(unexpected_error(), req)


class MultiGenerateText(PublicNode):
    async def run(self, req: Optional[SubstrateRequest] = None, **args) -> Dict[str, Any]:
        in_model = self.construct_in_model(MultiGenerateTextInPD, req, **args)
        if isinstance(in_model, ErrorOut):
            return self.construct_out_model(in_model, req)

        node = ModalNode(model=ModalHandle.mistral7b_instruct)
        try:
            res = await node.run(
                req=req,
                prompts=[{"prompt": in_model.prompt}],
                temperature=temperature_to_temperature(in_model.temperature),
                max_tokens=in_model.max_tokens,
                json_schema=response_format_to_json_schema(in_model.response_format),
                num_completions=in_model.num_choices,
            )
            result_dict = res["data"]["items"][0]
            result = MistralResult(**result_dict)
            if result.completions:
                out = MultiGenerateTextOut(choices=[GenerateTextOut(text=c) for c in result.completions])
                return self.construct_out_model(out, req)
            elif result.json_completions:
                out = MultiGenerateTextOut(choices=[GenerateTextOut(json_object=c) for c in result.json_completions])
                return self.construct_out_model(out, req)
            else:
                return self.construct_out_model(unexpected_error(), req)
        except Exception as e:
            log.error(e)
            return self.construct_out_model(unexpected_error(), req)


class GenerateTextVision(PublicNode):
    async def run(self, req: Optional[SubstrateRequest] = None, **args) -> Union[Dict[str, Any], ErrorOut]:
        in_model = self.construct_in_model(GenerateTextVisionInPD, req, **args)
        if isinstance(in_model, ErrorOut):
            return in_model

        node = ModalNode(model=ModalHandle.firellava)
        try:
            res_dict = await node.run(
                req=req,
                prompt=in_model.prompt,
                image_url_batch=in_model.image_uris,
                max_tokens=in_model.max_tokens,
            )
            res = FirellavaOut(**res_dict)
            item = res.result[0]
            out = GenerateTextVisionOut(text=item.generated_text)
            return self.construct_out_model(out, req)
        except Exception as e:
            log.error(e)
            return self.construct_out_model(unexpected_error(), req)


def image_influence_to_ip_adapter_scale(image_influence: Union[float, None]) -> Union[float, None]:
    if image_influence is None:
        return None
    return (image_influence / 10) * 1.0


class GenerateImage(PublicNode):
    async def run(self, req: Optional[SubstrateRequest] = None, **args) -> Dict[str, Any]:
        in_model = self.construct_in_model(GenerateImageInPD, req, **args)
        if isinstance(in_model, ErrorOut):
            return self.construct_out_model(in_model, req)

        args = {
            "req": req,
            "prompt": in_model.prompt,
            "negative_prompt": in_model.negative_prompt,
            "width": in_model.width,
            "height": in_model.height,
            "seeds": [in_model.seed] if in_model.seed else None,
            "store": in_model.store,
            "num_images": 1,
        }
        node = ModalNode(model=ModalHandle.stablediffusionxl_lightning)
        if in_model.image_prompt_uri:
            node = ModalNode(model=ModalHandle.stablediffusionxl_ipadapter)
            args["image_prompt_uri"] = in_model.image_prompt_uri
            args["ip_adapter_scale"] = image_influence_to_ip_adapter_scale(in_model.image_influence)

        try:
            res = await node.run(**args)
            image_dict = res[0]
            res = GenerateImageOut(**image_dict)
            return self.construct_out_model(res, req)
        except Exception as e:
            log.error(e)
            return self.construct_out_model(unexpected_error(), req)


class MultiGenerateImage(PublicNode):
    async def run(self, req: Optional[SubstrateRequest] = None, **args) -> Dict[str, Any]:
        in_model = self.construct_in_model(MultiGenerateImageInPD, req, **args)
        if isinstance(in_model, ErrorOut):
            return self.construct_out_model(in_model, req)

        args = {
            "req": req,
            "prompt": in_model.prompt,
            "num_images": in_model.num_images,
            "negative_prompt": in_model.negative_prompt,
            "width": in_model.width,
            "height": in_model.height,
            "seeds": in_model.seeds,
            "store": in_model.store,
        }
        node = ModalNode(model=ModalHandle.stablediffusionxl_lightning)
        if in_model.image_prompt_uri:
            node = ModalNode(model=ModalHandle.stablediffusionxl_ipadapter)
            args["image_prompt_uri"] = in_model.image_prompt_uri
            args["ip_adapter_scale"] = image_influence_to_ip_adapter_scale(in_model.image_influence)

        try:
            res = await node.run(**args)
            items = res["data"]["items"]
            res = MultiGenerateImageOut(
                outputs=[
                    GenerateImageOut(image_uri=r.uri, seed=r.seed) for r in [StableDiffusionImage(**d) for d in items]
                ]
            )
            return self.construct_out_model(res, req)
        except Exception as e:
            log.error(e)
            return self.construct_out_model(unexpected_error(), req)


def control_method_to_model(method: str) -> Union[ErrorOut, ModalConfig]:
    methods = {
        "edge": ModalHandle.stablediffusionxl_controlnet_edge,
        "depth": ModalHandle.stablediffusionxl_controlnet_depth,
        "illusion": ModalHandle.stablediffusion1_5_controlnet_qr,
    }
    config = methods.get(method)
    if config is None:
        return unexpected_error()
    return config


def image_influence_to_conditioning_scale(image_influence: Union[float, None]) -> Union[float, None]:
    if image_influence is None:
        return None
    return (image_influence / 10) * 1.0


class ControlledGenerateImage(PublicNode):
    async def run(self, req: Optional[SubstrateRequest] = None, **args) -> Dict[str, Any]:
        in_model = self.construct_in_model(ControlledGenerateImageInPD, req, **args)
        if isinstance(in_model, ErrorOut):
            return self.construct_out_model(in_model, req)
        model = control_method_to_model(in_model.control_method)
        if isinstance(model, ErrorOut):
            return self.construct_out_model(model, req)

        args = {
            "req": req,
            "image_uri": in_model.image_uri,
            "prompt": in_model.prompt,
            "negative_prompt": in_model.negative_prompt,
            "conditioning_scale": image_influence_to_conditioning_scale(in_model.image_influence),
            "output_resolution": in_model.output_resolution,
            "seeds": [in_model.seed] if in_model.seed else None,
            "store": in_model.store,
            "num_images": 1,
        }
        node = ModalNode(model=model)
        try:
            res = await node.run(**args)
            image_dict = res[0]
            res = ControlledGenerateImageOut(**image_dict)
            return self.construct_out_model(res, req)
        except Exception as e:
            log.error(e)
            return self.construct_out_model(unexpected_error(), req)


class MultiControlledGenerateImage(PublicNode):
    async def run(self, req: Optional[SubstrateRequest] = None, **args) -> Dict[str, Any]:
        in_model = self.construct_in_model(MultiControlledGenerateImageInPD, req, **args)
        if isinstance(in_model, ErrorOut):
            return self.construct_out_model(in_model, req)
        model = control_method_to_model(in_model.control_method)
        if isinstance(model, ErrorOut):
            return self.construct_out_model(model, req)

        args = {
            "req": req,
            "image_uri": in_model.image_uri,
            "prompt": in_model.prompt,
            "negative_prompt": in_model.negative_prompt,
            "conditioning_scale": image_influence_to_conditioning_scale(in_model.image_influence),
            "output_resolution": in_model.output_resolution,
            "seeds": in_model.seeds,
            "store": in_model.store,
            "num_images": in_model.num_images,
        }
        node = ModalNode(model=model)
        try:
            results = await node.run(**args)
            res = MultiControlledGenerateImageOut(outputs=[GenerateImageOut(**r) for r in results])
            return self.construct_out_model(res, req)
        except Exception as e:
            log.error(e)
            return self.construct_out_model(unexpected_error(), req)


def strength_to_strength(strength: Union[float, None]) -> Union[float, None]:
    if strength is None:
        return None
    return (strength / 10) * 1.0


class GenerativeEditImage(PublicNode):
    async def run(self, req: Optional[SubstrateRequest] = None, **args) -> Dict[str, Any]:
        in_model = self.construct_in_model(GenerativeEditImageInPD, req, **args)
        if isinstance(in_model, ErrorOut):
            return self.construct_out_model(in_model, req)

        args = {
            "req": req,
            "image_uri": in_model.image_uri,
            "mask_image_uri": in_model.mask_image_uri,
            "prompt": in_model.prompt,
            "strength": strength_to_strength(in_model.strength),
            "negative_prompt": in_model.negative_prompt,
            "output_resolution": in_model.output_resolution,
            "seeds": [in_model.seed] if in_model.seed else None,
            "store": in_model.store,
            "num_images": 1,
        }
        node = ModalNode(model=ModalHandle.stablediffusionxl_inpaint)
        if in_model.image_prompt_uri:
            node = ModalNode(model=ModalHandle.stablediffusionxl_inpaint_ipadapter)
            args["image_prompt_uri"] = in_model.image_prompt_uri
            args["ip_adapter_scale"] = image_influence_to_ip_adapter_scale(in_model.image_prompt_influence)

        try:
            res = await node.run(**args)
            image_dict = res[0]
            res = GenerativeEditImageOut(**image_dict)
            return self.construct_out_model(res, req)
        except Exception as e:
            log.error(e)
            return self.construct_out_model(unexpected_error(), req)


class MultiGenerativeEditImage(PublicNode):
    async def run(self, req: Optional[SubstrateRequest] = None, **args) -> Dict[str, Any]:
        in_model = self.construct_in_model(MultiGenerativeEditImageInPD, req, **args)
        if isinstance(in_model, ErrorOut):
            return self.construct_out_model(in_model, req)

        args = {
            "req": req,
            "image_uri": in_model.image_uri,
            "mask_image_uri": in_model.mask_image_uri,
            "prompt": in_model.prompt,
            "strength": strength_to_strength(in_model.strength),
            "negative_prompt": in_model.negative_prompt,
            "output_resolution": in_model.output_resolution,
            "seeds": in_model.seeds,
            "store": in_model.store,
            "num_images": in_model.num_images,
        }
        node = ModalNode(model=ModalHandle.stablediffusionxl_inpaint)
        if in_model.image_prompt_uri:
            node = ModalNode(model=ModalHandle.stablediffusionxl_inpaint_ipadapter)
            args["image_prompt_uri"] = in_model.image_prompt_uri

        try:
            results = await node.run(**args)
            res = MultiGenerativeEditImageOut(outputs=[GenerativeEditImageOut(**r) for r in results])
            return self.construct_out_model(res, req)
        except Exception as e:
            log.error(e)
            return self.construct_out_model(unexpected_error(), req)


def motion_to_motion_bucket_id(strength: Union[float, None]) -> Union[float, None]:
    if strength is None:
        return None
    return (strength / 10) * 1.0


def strength_to_noise_aug_strength(strength: Union[float, None]) -> Union[float, None]:
    if strength is None:
        return None
    return (strength / 10) * 1.0


class FillMask(PublicNode):
    async def run(self, req: Optional[SubstrateRequest] = None, **args) -> Dict[str, Any]:
        in_model = self.construct_in_model(FillMaskInPD, req, **args)
        if isinstance(in_model, ErrorOut):
            return self.construct_out_model(in_model, req)

        args = {
            "req": req,
            "image_uri": in_model.image_uri,
            "mask_image_uri": in_model.mask_image_uri,
            "store": in_model.store,
        }
        node = ModalNode(model=ModalHandle.lama)
        try:
            res = await node.run(**args)
            res = FillMaskOut(**res)
            return self.construct_out_model(res, req)
        except Exception as e:
            log.error(e)
            return self.construct_out_model(unexpected_error(), req)


class DetectSegments(PublicNode):
    async def run(self, req: Optional[SubstrateRequest] = None, **args) -> Dict[str, Any]:
        in_model = self.construct_in_model(DetectSegmentsInPD, req, **args)
        if isinstance(in_model, ErrorOut):
            return self.construct_out_model(in_model, req)

        if not in_model.point_prompts and not in_model.box_prompts:
            error = ErrorOut(
                type="invalid_request_error", message="One of `point_prompts` or `box_prompts` must be set."
            )
            return self.construct_out_model(error, req)

        point_prompts = None
        box_prompts = None
        if in_model.point_prompts:
            point_prompts = [[p.x, p.y] for p in in_model.point_prompts]
        if in_model.box_prompts:
            box_prompts = [[p.x1, p.x2, p.y1, p.y2] for p in in_model.box_prompts]

        args = {
            "req": req,
            "image_uri": in_model.image_uri,
            "point_prompts": point_prompts,
            "box_prompts": box_prompts,
            "store": in_model.store,
        }
        node = ModalNode(model=ModalHandle.segment_anything)
        try:
            res_dict = await node.run(**args)
            res = DetectSegmentsOut(**res_dict)
            return self.construct_out_model(res, req)
        except Exception as e:
            log.error(e)
            return self.construct_out_model(unexpected_error(), req)


class RemoveBackground(PublicNode):
    async def run(self, req: Optional[SubstrateRequest] = None, **args) -> Dict[str, Any]:
        in_model = self.construct_in_model(RemoveBackgroundInPD, req, **args)
        if isinstance(in_model, ErrorOut):
            return self.construct_out_model(in_model, req)

        args = {
            "req": req,
            "image_uri": in_model.image_uri,
            "return_mask": in_model.return_mask,
            "background_color": in_model.background_color,
            "store": in_model.store,
        }
        node = ModalNode(model=ModalHandle.isnet)
        try:
            res_dict = await node.run(**args)
            res = RemoveBackgroundOut(**res_dict)
            return self.construct_out_model(res, req)
        except Exception as e:
            return self.construct_out_model(unexpected_error(), req)


class UpscaleImage(PublicNode):
    async def run(self, req: Optional[SubstrateRequest] = None, **args) -> Dict[str, Any]:
        in_model = self.construct_in_model(UpscaleImageInPD, req, **args)
        if isinstance(in_model, ErrorOut):
            return self.construct_out_model(in_model, req)

        args = {
            "req": req,
            "image_uri": in_model.image_uri,
            "store": in_model.store,
        }
        node = ModalNode(model=ModalHandle.esrgan)

        try:
            res_dict = await node.run(**args)
            res = UpscaleImageOut(**res_dict)
            return self.construct_out_model(res, req)
        except Exception as e:
            log.error(e)
            return self.construct_out_model(unexpected_error(), req)


class TranscribeMedia(PublicNode):
    async def run(self, req: Optional[SubstrateRequest] = None, **args) -> Dict[str, Any]:
        in_model = self.construct_in_model(TranscribeMediaInPD, req, **args)
        if isinstance(in_model, ErrorOut):
            return self.construct_out_model(in_model, req)

        args = {
            "req": req,
            "audio_url": in_model.audio_uri,
            "prompt": in_model.prompt,
            "language": in_model.language,
            "return_segments": in_model.segment,
            "align": in_model.align,
            "diarize": in_model.diarize,
            "suggest_chapters": in_model.suggest_chapters,
        }
        node = ModalNode(model=ModalHandle.whisper)
        try:
            res_dict = await node.run(**args)
            res = TranscribeMediaOut(**res_dict)
            return self.construct_out_model(res, req)
        except Exception as e:
            log.error(e)
            return self.construct_out_model(unexpected_error(), req)


class GenerateSpeech(PublicNode):
    async def run(self, req: Optional[SubstrateRequest] = None, **args) -> Dict[str, Any]:
        in_model = self.construct_in_model(GenerateSpeechInPD, req, **args)
        if isinstance(in_model, ErrorOut):
            return self.construct_out_model(in_model, req)

        node = ModalNode(model=ModalHandle.xtts)
        try:
            res_dict = await node.run(
                req=req,
                text=in_model.text,
                audio_uri=in_model.audio_uri,
                language=in_model.language,
                store=in_model.store,
            )
            res = GenerateSpeechOut(**res_dict)
            return self.construct_out_model(res, req)
        except Exception as e:
            log.error(e)
            return self.construct_out_model(unexpected_error(), req)


class EmbedText(PublicNode):
    async def run(self, req: Optional[SubstrateRequest] = None, **args) -> Dict[str, Any]:
        in_model = self.construct_in_model(EmbedTextInPD, req, **args)
        if isinstance(in_model, ErrorOut):
            return self.construct_out_model(in_model, req)

        res_dict = {}
        # TODO: implement
        # node = ModalNode(model=ModalHandle.create_mask_image)
        # res_dict = await node.run(
        # )
        res = EmbedTextOut(**res_dict)
        return self.construct_out_model(res, req)


class MultiEmbedText(PublicNode):
    async def run(self, req: Optional[SubstrateRequest] = None, **args) -> Dict[str, Any]:
        in_model = self.construct_in_model(MultiEmbedTextInPD, req, **args)
        if isinstance(in_model, ErrorOut):
            return self.construct_out_model(in_model, req)

        res_dict = {}
        # TODO: implement
        # node = ModalNode(model=ModalHandle.create_mask_image)
        # res_dict = await node.run(
        # )
        res = MultiEmbedTextOut(**res_dict)
        return self.construct_out_model(res, req)


class EmbedImage(PublicNode):
    async def run(self, req: Optional[SubstrateRequest] = None, **args) -> Dict[str, Any]:
        in_model = self.construct_in_model(EmbedImageInPD, req, **args)
        if isinstance(in_model, ErrorOut):
            return self.construct_out_model(in_model, req)

        res_dict = {}
        # TODO: implement
        # node = ModalNode(model=ModalHandle.create_mask_image)
        # res_dict = await node.run(
        # )
        res = EmbedImageOut(**res_dict)
        return self.construct_out_model(res, req)


class MultiEmbedImage(PublicNode):
    async def run(self, req: Optional[SubstrateRequest] = None, **args) -> Dict[str, Any]:
        in_model = self.construct_in_model(MultiEmbedImageInPD, req, **args)
        if isinstance(in_model, ErrorOut):
            return self.construct_out_model(in_model, req)

        res_dict = {}
        # TODO: implement
        # node = ModalNode(model=ModalHandle.create_mask_image)
        # res_dict = await node.run(
        # )
        res = MultiEmbedImageOut(**res_dict)
        return self.construct_out_model(res, req)


def get_all_subclasses(cls):
    all_subclasses = []
    for subclass in cls.__subclasses__():
        all_subclasses.append(subclass)
        all_subclasses.extend(get_all_subclasses(subclass))
    return all_subclasses


ALL_PUBLIC_NODES = {
    **{cls.__name__: cls for cls in get_all_subclasses(PublicNode)},
}
