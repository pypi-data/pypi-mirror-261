import unittest

import pytest

from sb_models.graph.node import Node
from sb_models.graph.server_graph import GraphResult, ServerGraph
from sb_models.graph.server_future import ServerFuture


class FooNode(Node):
    pass


@pytest.mark.unit
class TestFuture:
    def test_serialize_deserialize(self):
        d = {
            "id": "bc293b613d2845c9bf6287e9aa28780f",
            "directive": {
                "type": "trace",
                "op_stack": [
                    {"key": "nested", "accessor": "attr", "future_id": None},
                    {
                        "future_id": "69f38d0e88f84ac49ed35593591b5ea2",
                        "accessor": "item",
                        "key": None,
                    },
                    {"key": "nest_id", "accessor": "attr", "future_id": None},
                ],
                "origin_node_id": "06821f48-c070-44cb-bcf4-120ef92ff28f",
            },
        }

        os = ServerFuture.from_dict(d)
        td = os.to_dict()
        assert td == d

    def test_to_dict_via_ref_constructor(self):
        a = FooNode(ax=1)
        a.id = "a"
        ay = a.future.y
        ay.id = "ay"

        b = FooNode(bx=ay)
        b.id = "b"
        by = b.future.y
        by.id = "by"
        byay = by[ay]
        byay.id = "byay"

        c = FooNode(cx=by[ay])
        c.id = "c"

        assert ay.to_dict() == {
            "id": "ay",
            "directive": {
                "type": "trace",
                "origin_node_id": "a",
                "op_stack": [{"accessor": "attr", "key": "y", "future_id": None}],
            },
        }

        assert by.to_dict() == {
            "id": "by",
            "directive": {
                "type": "trace",
                "op_stack": [{"accessor": "attr", "key": "y", "future_id": None}],
                "origin_node_id": "b",
            },
        }

        assert byay.to_dict() == {
            "id": "byay",
            "directive": {
                "type": "trace",
                "op_stack": [
                    {"key": "y", "accessor": "attr", "future_id": None},
                    {"future_id": "ay", "accessor": "item", "key": None},
                ],
                "origin_node_id": "b",
            },
        }

    def test_evaluate_get_attr(self):
        node = FooNode()
        d = {
            "id": "op1",
            "directive": {
                "type": "trace",
                "op_stack": [
                    {"key": "key_a", "accessor": "attr", "future_id": None},
                    {"key": "key_b", "accessor": "attr", "future_id": None},
                ],
                "origin_node_id": node.id,
            },
        }
        future = ServerFuture.from_dict(d)

        graph = ServerGraph()
        graph.add_node(node)
        graph_result = GraphResult()
        graph_result.set_local(node, {"key_a": {"key_b": 123}})

        result = future.evaluate(node, graph, graph_result)
        assert result == 123

    def test_evaluate_get_index(self):
        node = FooNode()
        d = {
            "id": "op1",
            "directive": {
                "type": "trace",
                "op_stack": [
                    {"key": "key_a", "accessor": "attr", "future_id": None},
                    {"key": 0, "accessor": "attr", "future_id": None},
                ],
                "origin_node_id": node.id,
            },
        }
        future = ServerFuture.from_dict(d)
        graph = ServerGraph(futures=[future])
        graph.add_node(node)
        graph_result = GraphResult()
        graph_result.set_local(node, {"key_a": [456]})
        result = future.evaluate(node, graph, graph_result)
        assert result == 456

    def test_evaluate_get_item(self):
        node1 = FooNode()
        node2 = FooNode()

        op1 = {
            "id": "op1",
            "directive": {
                "type": "trace",
                "op_stack": [{"key": "key_b", "accessor": "attr", "future_id": None}],
                "origin_node_id": node1.id,
            },
        }
        op2 = {
            "id": "op2",
            "directive": {
                "type": "trace",
                "op_stack": [
                    {"key": "key_a", "accessor": "attr", "future_id": None},
                    {"future_id": "op1", "accessor": "item", "key": None},
                    {"key": "key_c", "accessor": "attr", "future_id": None},
                ],
                "origin_node_id": node2.id,
            },
        }

        future1 = ServerFuture.from_dict(op1)
        future2 = ServerFuture.from_dict(op2)

        graph = ServerGraph(futures=[future1, future2])
        graph.add_node(node1)
        graph.add_node(node2)

        graph_result = GraphResult()
        graph_result.set_local(node1, {"key_b": "foobarbaz"})
        graph_result.set_local(node2, {"key_a": {"foobarbaz": {"key_c": 789}}})

        result = future2.evaluate(node2, graph, graph_result)
        assert result == 789


if __name__ == "__main__":
    unittest.main()
