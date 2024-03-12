from typing import Any, Dict, List, Union, Optional

from pydantic import ValidationError

from .models import ErrorOut
from .versions import ToIn, FromOut
from .deprecated_models import MistralIn


def mistral_in_2024_01_01(json: Dict[str, Any]) -> Dict[str, Any]:
    """
    # prompt, prompts -> nested
    """
    result = {}
    maybePrompt = json.get("prompt")
    if maybePrompt:
        result["prompts"] = [{"prompt": maybePrompt}]
    maybePrompts = json.get("prompts")
    if maybePrompts:
        result["prompts"] = list(map(lambda p: {"prompt": p}, maybePrompts))
    maybeInputPrompts = json.get("input_prompts")
    if maybeInputPrompts:
        result["prompts"] = list(map(lambda p: {"prompt": p}, maybeInputPrompts))

    result = {
        **result,
        **{k: v for k, v in json.items() if not k in ["prompt", "prompts", "input_prompts"]},
    }
    return result


class ToMistralIn(ToIn[MistralIn]):
    def from_version(self, version: Optional[str]) -> Union[MistralIn, ErrorOut]:
        versions = {
            "2024-01-01": (lambda x: mistral_in_2024_01_01(x)),
        }
        res = self.json
        for date, fn in sorted(versions.items(), key=lambda x: x[0]):
            if version and version < date:
                res = fn(res)

        # Schema-level validation
        model = None
        try:
            model = MistralIn(**res)
        except ValidationError as e:
            import json

            e_json_str = e.json()
            e_json = json.loads(e_json_str)[0]
            message = f"{e_json.get('msg')}: {e_json.get('loc')}"
            return ErrorOut(type="invalid_request_error", message=message)

        return model


def mistral_out_2024_01_01(res: Any) -> Any:
    if isinstance(res, List):
        old_completions = []
        for item in res:
            completions = item.get("completions")
            json_completions = item.get("json_completions")
            if json_completions:
                old_completions.extend([{"json": c} for c in json_completions])
            elif completions:
                old_completions.extend([{"text": c} for c in completions])
        return {
            "completions": old_completions,
        }
    else:
        return res  # unexpected, no-op


class FromMistralOut(FromOut[List[Dict[str, Any]]]):
    """
    input: list of serialized MistralResults
    """

    def to_version(self, version: Optional[str]) -> List[Any]:
        versions = {
            "2024-01-01": (lambda x: mistral_out_2024_01_01(x)),
        }
        res = self.data
        for date, fn in sorted(versions.items(), key=lambda x: x[0], reverse=True):
            if version and version < date:
                res = fn(res)
        return res
