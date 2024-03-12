from copy import deepcopy
from typing import Any, Union, Optional

from pydantic import BaseModel


def _get_dynamic_value(data: Union[BaseModel, dict], path: str) -> Optional[Any]:
    elements = path.split(".")
    value = data

    for elem in elements:
        if "[" in elem and "]" in elem:
            # Handle list indexing
            attr, index = elem.split("[")
            index = int(index[:-1])  # remove the ']' and convert to int
            if isinstance(value, dict):
                value = value.get(attr, None)
            elif isinstance(value, BaseModel):
                value = getattr(value, attr, None)
            elif isinstance(value, list) and len(value) > index:
                value = value[index]
            else:
                return None
        else:
            # Handle attribute or key access
            if isinstance(value, dict):
                value = value.get(elem, None)
            elif isinstance(value, BaseModel):
                value = getattr(value, elem, None)
            else:
                return None

            if value is None:
                return None

    return value


class AdapterTransform:
    wrap_in_list = "wrap_in_list"
    get = "get"
    pick = "pick"
    concat = "concat"
    prepend = "prepend"
    wrap_in_dict = "wrap_in_dict"
    pop = "pop"


class Adapter:
    def __init__(
        self,
        source_key: Optional[str] = None,
        dest_key: Optional[str] = None,
        transform: Optional[str] = None,
        transform_args: Optional[dict] = None,
    ):
        if not source_key and not dest_key and not transform:
            raise ValueError("Must specify at least one of source_key, dest_key, transform")
        if transform_args and not transform:
            raise ValueError("Transform args specified but no transform")
        self.source_key = source_key
        self.dest_key = dest_key
        self.transform = transform
        self.transform_args = transform_args or {}

    def apply(self, data: Union[dict, BaseModel]) -> Optional[Any]:
        if isinstance(data, dict):
            data = deepcopy(data)
        elif isinstance(data, BaseModel):
            data = data.copy(deep=True)
        elif isinstance(data, list):
            data = {}
        else:
            raise ValueError(f"Unknown data type {type(data)}")

        # pick from data just like lodash pick
        if self.transform == AdapterTransform.pick:
            return {key: val for key, val in data.items() if key in self.transform_args["keys"]}
        if isinstance(data, dict):
            val = data.pop(self.source_key)
        elif isinstance(data, BaseModel):
            val = getattr(data, self.source_key)
        elif isinstance(data, list):
            val = data
        else:
            raise ValueError(f"Unknown data type {type(data)}")

        if self.transform == AdapterTransform.wrap_in_list:
            val = [val]
        elif self.transform == AdapterTransform.pop:
            val = val[0]
        elif self.transform == AdapterTransform.concat:
            val = val + self.transform_args["target"]
        elif self.transform == AdapterTransform.prepend:
            val = self.transform_args["target"] + val
        elif self.transform == AdapterTransform.wrap_in_dict:
            val = {self.transform_args["key"]: val}
        elif self.transform == AdapterTransform.get:
            if self.transform_args.get("map"):
                val = [_get_dynamic_value(i, self.transform_args["path"]) for i in val]
            else:
                val = _get_dynamic_value(val, self.transform_args["path"])
        elif self.transform is None:
            pass
        else:
            raise ValueError(f"Unknown transform {self.transform}")

        if self.dest_key:
            if isinstance(data, BaseModel):
                data = data.dict()
            data[self.dest_key] = val
        else:
            data[self.source_key] = val
        return data

    def to_dict(self):
        return {
            "source_key": self.source_key,
            "dest_key": self.dest_key,
            "transform": self.transform,
            "transform_args": self.transform_args,
        }


def pick(key: str):
    return Adapter(transform=AdapterTransform.pick, transform_args={"keys": [key]})


def concat(source_key: str, dest_key: str, target: str):
    return Adapter(
        source_key=source_key,
        dest_key=dest_key,
        transform=AdapterTransform.concat,
        transform_args={"target": target},
    )


def prepend(source_key: str, dest_key: str, target: str):
    return Adapter(
        source_key=source_key,
        dest_key=dest_key,
        transform=AdapterTransform.prepend,
        transform_args={"target": target},
    )


def to_list(source_key: str, dest_key: Optional[str] = None):
    return Adapter(
        source_key=source_key,
        transform=AdapterTransform.wrap_in_list,
        dest_key=dest_key,
    )


def get(source_key: str, path: str, dest_key: Optional[str] = None, map: bool = False):
    return Adapter(
        source_key=source_key,
        dest_key=dest_key,
        transform=AdapterTransform.get,
        transform_args={"path": path, "map": map},
    )
