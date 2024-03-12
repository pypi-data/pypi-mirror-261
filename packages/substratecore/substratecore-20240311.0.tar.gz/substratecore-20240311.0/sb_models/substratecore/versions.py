from abc import ABC, abstractmethod
from typing import Any, Dict, Union, Generic, TypeVar

from .deprecated_models import ErrorOut

M = TypeVar("M")


class ToIn(Generic[M], ABC):
    def __init__(self, json: Dict[str, Any]):
        self.json = json

    @abstractmethod
    def from_version(self, version: str) -> Union[M, ErrorOut]:
        """
        Translate a JSON request from a past version to the current model shape.
        """
        raise NotImplementedError()


class FromOut(Generic[M], ABC):
    def __init__(self, data: M):
        self.data = data

    @abstractmethod
    def to_version(self, version: str) -> Any:
        """
        Translate a response in the current model shape to a past version.
        """
        raise NotImplementedError()
