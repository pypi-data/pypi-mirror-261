from copy import deepcopy
from typing import Dict, List, Union, Optional

import networkx as nx
from pydantic import BaseModel

from sb_models.graph.util import node_instance
from sb_models.types.outputs import InferenceRun
from sb_models.types.request import SubstrateRequest
from sb_models.graph.adapters import Adapter
from sb_models.substratecore.corenode import CoreNode


class Node(CoreNode):
    is_multi_input = False

    def __init__(self, **attr):
        self._to_adapters: List[Adapter] = []
        self._from_adapters: List[Adapter] = []
        super().__init__(**attr)

    def pipe(self, to_nodes):
        """
        TODO: remove this, not actually used by clients
        Need to remove adapter first so we can nix some tests.
        """
        if isinstance(to_nodes, Node):
            to_nodes = (to_nodes,)
        for to_node in to_nodes:
            if isinstance(to_node, Node):
                self.SG = nx.compose(self.SG, to_node.SG)
                self.SG.add_edge(self, to_node)
            else:
                raise ValueError(f"Cannot pipe to {to_node}")
        return self

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id})"

    def __hash__(self):
        return Node.hash(self.id)

    def __eq__(self, other):
        return isinstance(other, Node) and self.id == other.id

    @classmethod
    def hash(cls, id: str):
        return hash(id)

    def to_dict(self):
        return {
            "id": self.id,
            "args": self.args,
            **({"_should_output_globally": self._should_output_globally} if self._should_output_globally else {}),
            **({"_global_output_keys": self._global_output_keys} if self._global_output_keys else {}),
            **({"_to_adapters": [a.to_dict() for a in self._to_adapters]} if self._to_adapters else {}),
            **({"_from_adapters": [a.to_dict() for a in self._from_adapters]} if self._from_adapters else {}),
        }

    @classmethod
    def from_dict(cls, node_dict: Dict):
        node = node_instance(node_dict)
        if node_dict.get("id"):
            node.id = node_dict["id"]

        if node_dict.get("_global_output_keys"):
            node.output(pick_keys=node_dict["_global_output_keys"])
        elif node_dict.get("_should_output_globally"):
            node.output()
        if node_dict.get("_to_adapters"):
            node.adapt_to(*[Adapter(**ad) for ad in node_dict["_to_adapters"]])
        if node_dict.get("_from_adapters"):
            node.adapt_from(*[Adapter(**ad) for ad in node_dict["_from_adapters"]])
        return node

    def adapt_to(self, *adapters: Union[Adapter, List[Adapter]]):
        if isinstance(adapters, list):
            self._to_adapters.extend(*adapters)
        else:
            self._to_adapters.extend(adapters)
        return self

    def adapt_from(self, *adapters: Union[Adapter, List[Adapter]]):
        if isinstance(adapters, list):
            self._from_adapters.extend(*adapters)
        else:
            self._from_adapters.extend(adapters)
        return self

    async def run(self, req: Optional[SubstrateRequest] = None, **args) -> Union[Dict, BaseModel]:
        raise NotImplementedError

    async def _run(self, req: Optional[SubstrateRequest] = None, **args):
        if self._from_adapters:
            for adapter in self._from_adapters:
                args = adapter.apply(args)

        usage = None
        inf_run = await self.run(req=req, **args)
        if isinstance(inf_run, InferenceRun):
            usage = inf_run.usage
            local_result = inf_run.result
        else:
            local_result = inf_run

        global_outs = None

        if self._should_output_globally:
            if self._global_output_keys:
                global_outs = {
                    key: deepcopy(val) for key, val in local_result.items() if key in self._global_output_keys
                }
            else:
                global_outs = deepcopy(local_result)

        if self._to_adapters:
            for adapter in self._to_adapters:
                local_result = adapter.apply(local_result)
        return local_result, global_outs, usage
