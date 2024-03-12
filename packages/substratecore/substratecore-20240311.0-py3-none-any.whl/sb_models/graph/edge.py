from copy import deepcopy

from pydantic import BaseModel

from sb_models.substratecore.base_future import FUTURE_ID_PLACEHOLDER


class EdgesProcessor:
    """EdgesProcessor produces args for a node from previous results and incoming edges"""

    def __init__(self, graph, node, graph_result):
        self.graph = graph
        self.node = node
        self.graph_result = graph_result

    def edges(self):
        return self.graph.DAG.in_edges(self.node, data=True)

    def resolve_args(self, use_futures: bool = False):
        if use_futures:
            return self.resolve_args_with_futures()
        return self.resolve_args_explicit()

    def resolve_args_with_futures(self):
        """
        Returns the input for a ready node by building the concrete input kwargs for that node.
        <future_id> placeholders will be replaced with real results from previous node executions.

        The assumption at this point is that the node is being prepared for run, so every dependency that it
        needs has already been resolved.
        """
        initial_args = deepcopy(self.node.args)
        futures_by_id = {future.id: future for future in self.graph.futures}

        def hydrate_placeholders(mutable_dict):
            for k, v in mutable_dict.items():
                if isinstance(v, dict):
                    if FUTURE_ID_PLACEHOLDER in v:
                        future_id = v[FUTURE_ID_PLACEHOLDER]
                        future = futures_by_id.get(future_id)
                        if future:
                            mutable_dict[k] = future.evaluate(self.node, self.graph, self.graph_result)
                    else:
                        hydrate_placeholders(v)
                elif isinstance(v, list):
                    for item in v:
                        hydrate_placeholders(item)

        hydrate_placeholders(initial_args)
        return initial_args

    def resolve_args_explicit(self):
        result_dict = {}
        for u, _, _ in self.edges():
            incoming_results = self.graph_result.locals[u]
            edge_dict = deepcopy(
                incoming_results.dict() if isinstance(incoming_results, BaseModel) else incoming_results
            )
            result_dict.update(edge_dict)
        return result_dict
