from typing import Any, Dict

from sb_models.graph.node import Node


class GraphResult:
    def __init__(self):
        self.local_outs: Dict[Node, Any] = {}
        self.global_outs: Dict[Node, Any] = {}
        self.usage = {}

    @property
    def locals(self) -> Dict[Node, Any]:
        return self.local_outs

    @property
    def globals(self) -> Dict[Node, Any]:
        return self.global_outs

    def set_local(self, node, res):
        self.local_outs[node] = res

    def set_global(self, node, res):
        self.global_outs[node] = res

    def first(self):
        return next(iter(self.global_outs.values()))

    def __iter__(self):
        return iter(self.global_outs)

    def keys(self):
        return self.global_outs.keys()

    def values(self):
        return self.global_outs.values()

    def items(self):
        return self.global_outs.items()

    def get(self, key, default=None):
        return self.global_outs.get(key, default)

    def __contains__(self, item):
        return item in self.global_outs

    def __len__(self):
        return len(self.global_outs)

    def __getitem__(self, item):
        return self.global_outs[item]

    def __repr__(self):
        return f"GraphResult({self.global_outs})"

    def __str__(self):
        return self.__repr__()

    def to_dict(self):
        return {node.id: v for node, v in self.global_outs.items()}
