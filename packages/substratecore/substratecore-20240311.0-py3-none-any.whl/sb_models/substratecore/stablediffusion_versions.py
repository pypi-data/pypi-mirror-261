from typing import Any, Dict, List, Union, Optional

from pydantic import ValidationError

from .versions import ToIn, FromOut
from .deprecated_models import (
    ErrorOut,
    StableDiffusionXLIn,
)


def sdxl_in_2024_01_01(json: Dict[str, Any]) -> Dict[str, Any]:
    # use_hosted_url -> store
    # return_base64 -> store
    result = {
        **{k: v for k, v in json.items() if not k in ["use_hosted_url", "return_base64", "n"]},
    }
    if json.get("use_hosted_url") != None:
        result["store"] = json.get("use_hosted_url")
    if json.get("return_base64") != None:
        result["store"] = not json.get("return_base64")
    if json.get("n") != None:
        result["num_images"] = json.get("n")
    return result


class ToStableDiffusionXLIn(ToIn[StableDiffusionXLIn]):
    def from_version(self, version: Optional[str]) -> Union[StableDiffusionXLIn, ErrorOut]:
        versions = {
            "2024-01-01": (lambda x: sdxl_in_2024_01_01(x)),
        }
        res = self.json
        for date, fn in sorted(versions.items(), key=lambda x: x[0]):
            if version and version < date:
                res = fn(res)

        # Schema-level validation
        model = None
        try:
            model = StableDiffusionXLIn(**res)
        except ValidationError as e:
            import json

            e_json_str = e.json()
            e_json = json.loads(e_json_str)[0]
            message = f"{e_json.get('msg')}: {e_json.get('loc')}"
            return ErrorOut(type="invalid_request_error", message=message)

        return model


class FromStableDiffusionOut(FromOut[List[Dict[str, Any]]]):
    """
    input: list of serialized StableDiffusionImages
    """

    def to_version(self, version: Optional[str]) -> List[Any]:
        versions = {}
        res = self.data
        for date, fn in sorted(versions.items(), key=lambda x: x[0], reverse=True):
            if version and version < date:
                res = fn(res)
        return res
