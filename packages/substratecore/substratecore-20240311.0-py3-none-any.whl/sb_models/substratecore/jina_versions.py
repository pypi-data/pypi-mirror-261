from typing import Any, Dict, List, Union, Optional

from pydantic import ValidationError

from .models import ErrorOut
from .versions import ToIn, FromOut
from .deprecated_models import JinaIn


def jina_in_2023_12_26(json: Dict[str, Any]) -> Dict[str, Any]:
    """
    provider_ids -> ids
    """
    docs = []
    store_info = json.get("store_info")
    for i in range(0, len(json.get("texts", []))):
        doc = {"text": json.get("texts", [])[i]}
        if len(json.get("ids", [])) > i:
            doc["id"] = json.get("ids", [])[i]
        if len(json.get("provider_ids", [])) > i:
            doc["id"] = json.get("provider_ids", [])[i]
        if len(json.get("metadatas", [])) > i:
            doc["metadata"] = json.get("metadatas", [])[i]
        if store_info and store_info.get("full_metadata"):
            doc["metadata"] = store_info.get("full_metadata", [])[i]
        if json.get("embed_metadata_keys"):
            doc["embed_metadata_keys"] = json.get("embed_metadata_keys")
        docs.append(doc)
    result = {}
    if len(docs) > 0:
        result["docs"] = docs
    if json.get("collection"):
        result["store"] = json.get("collection")
    if store_info and store_info.get("collection"):
        result["store"] = store_info.get("collection")
    # ignore the `split` param, Substack always passes False
    if json.get("split") is not None:
        pass
    return result


class ToJinaIn(ToIn[JinaIn]):
    def from_version(self, version: Optional[str]) -> Union[JinaIn, ErrorOut]:
        versions = {
            "2023-12-26": (lambda x: jina_in_2023_12_26(x)),
        }
        res = self.json
        for date, fn in sorted(versions.items(), key=lambda x: x[0]):
            if version and version < date:
                res = fn(res)

        # Schema-level validation
        model = None
        try:
            model = JinaIn(**res)
        except ValidationError as e:
            import json

            e_json_str = e.json()
            e_json = json.loads(e_json_str)[0]
            message = f"{e_json.get('msg')}: {e_json.get('loc')}"
            return ErrorOut(type="invalid_request_error", message=message)

        # Additional validation
        ids = [doc.id for doc in model.docs if doc.id]
        metadatas = [doc.metadata for doc in model.docs if doc.metadata]
        embed_metadata_keys_list = [doc.embed_metadata_keys for doc in model.docs if doc.embed_metadata_keys]
        texts = [doc.text for doc in model.docs if doc.text]
        if len(model.docs) > 2048:
            return ErrorOut(
                type="invalid_request_error",
                message="Max embedding batch size is 2048 documents.",
            )
        if model.store and (len(ids) != len(set(ids))):
            dupes = set([i for i in ids if ids.count(i) > 1])
            return ErrorOut(
                type="invalid_request_error",
                message=f"Can't store documents with duplicate ids: {dupes}",
            )

        if len(metadatas) > 0:
            if len(metadatas) != len(texts):
                return ErrorOut(
                    type="invalid_request_error",
                    message=f"When using metadata all docs must include metadata",
                )

        if len(embed_metadata_keys_list) > 0 and (len(embed_metadata_keys_list) != len(texts)):
            return ErrorOut(
                type="invalid_request_error",
                message=f"When using embed_metadata_keys all docs must include embed_metadata_keys",
            )

        return model


def jina_out_2023_12_26(res: List[Dict[str, Any]]) -> Any:
    """
    substack
    """
    # convert key names
    new_res = [
        {
            "meta": x.get("metadata", None),
            "vec": x.get("vector", None),
            **{k: v for k, v in x.items() if k not in ["metadata", "vector"]},
        }
        for x in res
    ]
    # wrap each item in a list
    return [[item] for item in new_res]


class FromJinaOut(FromOut[List[Dict[str, Any]]]):
    """
    input: list of serialized JinaEmbeddings
    """

    def to_version(self, version: Optional[str]) -> Any:
        versions = {
            "2023-12-26": (lambda x: jina_out_2023_12_26(x)),
        }
        res = self.data
        for date, fn in sorted(versions.items(), key=lambda x: x[0], reverse=True):
            if version and version < date:
                res = fn(res)
        return res
