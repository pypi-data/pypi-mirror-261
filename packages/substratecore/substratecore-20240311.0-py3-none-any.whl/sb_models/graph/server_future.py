import logging
from copy import deepcopy
from typing import (
    Any,
    Dict,
)

from sb_models.graph.graph_result import GraphResult
from sb_models.substratecore.base_future import BaseFuture, Concatable, TraceDirective, TraceOperation, ConcatDirective

log = logging.getLogger(__name__)


class ServerFuture(BaseFuture):
    def evaluate(self, current_node, graph, graph_result: GraphResult) -> Any:
        """
        Renders the Future into an evaluated result, using evaluated dependencies
        """
        DAG = graph.DAG
        futures_by_id = {future.id: future for future in graph.futures}

        if isinstance(self.directive, TraceDirective):
            result = {}
            if self.directive.origin_node_id:
                origin_node = next(node for node in DAG.nodes() if node.id == self.directive.origin_node_id)
                result = deepcopy(graph_result.locals[origin_node])

            for op in self.directive.op_stack:
                if op.future_id:
                    future_item = futures_by_id[op.future_id]
                    if future_item:
                        key = future_item.evaluate(current_node, graph, graph_result)
                        result = result[key]
                    else:
                        log.error(f"Expected to find Future, but didn't. future_id={op.future_id}")
                else:
                    result = result[op.key]
            return result

        elif isinstance(self.directive, ConcatDirective):
            result_str = ""
            for op in self.directive.items:
                if op.val:
                    result_str = result_str + op.val
                else:
                    future_id = op.future_id
                    future_item = futures_by_id[future_id]
                    if future_item:
                        result_str = result_str + future_item.evaluate(current_node, graph, graph_result)
                    else:
                        log.error(f"Expected to find Future, but didn't. future_id={future_id}")
            return result_str
        else:
            raise ValueError(f"Unknown directive type: {self.directive.type}")

    @classmethod
    def from_dict(cls, d: Dict):
        id = d["id"]
        directive_json = d["directive"]
        if directive_json["type"] == "trace":
            op_stack_json = directive_json.get("op_stack")
            origin_node_id = directive_json.get("origin_node_id")
            directive = TraceDirective(
                origin_node_id=origin_node_id, op_stack=[TraceOperation(**item) for item in op_stack_json]
            )
        elif directive_json["type"] == "string-concat":
            items = directive_json.get("items")
            directive = ConcatDirective(items=[Concatable(**item) for item in items])
        else:
            raise ValueError(f"Unknown directive type: {directive_json['type']}")
        return ServerFuture(id=id, directive=directive)
