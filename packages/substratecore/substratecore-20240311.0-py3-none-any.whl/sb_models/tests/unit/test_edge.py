import unittest

import pytest

from sb_models.graph.edge import EdgesProcessor
from sb_models.graph.node import Node
from sb_models.graph.server_graph import GraphResult, ServerGraph
from sb_models.graph.server_future import ServerFuture
from sb_models.substratecore.base_future import TraceDirective
from sb_models.substratecore.client.future import TraceOperation


class FooNode(Node):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    async def run(self, **kwargs):
        return {}

    def __repr__(self):
        return f"FooNode(id={self.id}, args={self.args})"


@pytest.mark.unit
class TestEdge:
    def test_get_args(self):
        # Example where there are 2 edges coming into node3 from node1 and node2 when we're NOT
        # using Futures to determine the args. This is the current/live approach as of Jan 22, 2024.
        #
        #   node1 --> node3
        #   node2 --> node3
        #
        graph = ServerGraph()
        graph_result = GraphResult()

        node1 = FooNode()
        node1.id = "node1"
        node2 = FooNode()
        node2.id = "node2"
        node3 = FooNode()
        node3.id = "node3"

        graph.add_node(node1)
        graph.add_node(node2)
        graph.add_node(node3)
        graph.DAG.add_edge(node1, node3, **{})
        graph.DAG.add_edge(node2, node3, **{})

        graph_result.set_local(node1, {"node1_output": 123})
        graph_result.set_local(node2, {"node2_output": 456})

        edges_processor = EdgesProcessor(graph, node3, graph_result)
        result = edges_processor.resolve_args_explicit()

        # result should be the combined output of node1 and node2
        assert result == {"node1_output": 123, "node2_output": 456}

    @pytest.mark.skip(reason="Legacy test, doesn't go through the e2e lifecycle enough to hydrate op sets")
    def test_get_args_with_futures(self):
        # Example where there are 2 edges coming into node3 from node1 and node2 when we are
        # using Futures to determine the args. This is the new/experimental approach.
        #
        #   node1 --> node3
        #   node2 --> node3
        #
        graph = ServerGraph()
        graph_result = GraphResult()

        node1 = FooNode()
        node1.id = "node1"
        node2 = FooNode()
        node2.id = "node2"

        from_node1_future = ServerFuture(
            id="op1",
            directive=TraceDirective(
                origin_node_id="node1",
                op_stack=[TraceOperation(key="node1_output_a", accessor="attr", future_id=None)],
            ),
        )
        from_node2_future = ServerFuture(
            id="op2",
            directive=TraceDirective(
                origin_node_id="node1",
                op_stack=[TraceOperation(key="node2_output_c", accessor="attr", future_id=None)],
            ),
        )

        node3 = FooNode(x=[{"a": from_node1_future}], y=from_node2_future, z="literal string")
        node3.id = "node3"

        graph.add_node(node1)
        graph.add_node(node2)
        graph.add_node(node3)
        graph.DAG.add_edge(node1, node3, **{})
        graph.DAG.add_edge(node2, node3, **{})

        graph_result.set_local(node1, {"node1_output_a": 123, "node1_output_b": 888})
        graph_result.set_local(node2, {"node2_output_c": 456, "node2_output_d": 888})

        edges_processor = EdgesProcessor(graph, node3, graph_result)
        result = edges_processor.resolve_args_with_futures()

        # result should be the selected values from the output of node1 and node2 (plus a static value)
        assert result == {"x": [{"a": 123}], "y": 456, "z": "literal string"}


if __name__ == "__main__":
    unittest.main()
