import json
import unittest

import pytest

from sb_models.substratecore.corenode import CoreNode
from sb_models.substratecore.base_future import FUTURE_ID_PLACEHOLDER
from sb_models.substratecore.client.graph import Graph


@pytest.mark.unit
class TestClientGraph:
    def test_1_node(self):
        a = CoreNode(num=1)
        a.id = "a_id"
        g = Graph()
        assert "graph_" in g.id
        g.add_node(a)
        d = g.to_dict()
        print(json.dumps(d, indent=2))
        assert len(d["nodes"]) == 1
        d_a = d["nodes"][0]
        assert d_a["id"] == "a_id"
        assert d_a["args"]["num"] == 1

    def test_2_nodes_ref(self):
        a = CoreNode(num=1)
        a.id = "a_id"
        b = CoreNode(num=a.future.num, str="b_str")
        b.id = "b_id"
        g = Graph()
        g.add_node(a).add_node(b)
        d = g.to_dict()
        assert len(d["nodes"]) == 2
        d_b = d["nodes"][1]
        assert d_b["id"] == "b_id"
        assert d_b["args"]["str"] == "b_str"
        assert FUTURE_ID_PLACEHOLDER in d_b["args"]["num"]
        assert len(d["futures"]) == 1
        op = d["futures"][0]["directive"]
        assert op["origin_node_id"] == "a_id"
        op_stack = op["op_stack"]
        assert op["type"] == "trace"
        assert op_stack[0]["key"] == "num"
        assert op_stack[0]["accessor"] == "attr"

    def test_4_nodes_nested_index_ref(self):
        a = CoreNode(prompt="foo")
        a.id = "a"
        b = CoreNode(foo="bar")
        b.id = "b"
        c = CoreNode(hello="bar")
        c.id = "c"
        d = CoreNode(qux={"foo": b.future.results[a.future.results[c.future.idx]]})
        d.id = "d"
        cg = Graph().add_nodes(a, b, c, d)
        serialized = cg.to_dict()
        print(json.dumps(serialized, indent=2))
        print(serialized["futures"])
        assert len(serialized["futures"]) == 3

    def test_to_dict_with_refs(self):
        """
        Basic serialization test
        """
        a = CoreNode(ax=1)
        a.id = "a"

        ay = a.future.y
        ay.id = "ay"

        b = CoreNode(bx=ay)
        b.id = "b"

        byay = b.future.y[ay]
        byay.id = "byay"

        c = CoreNode(cx=byay)
        c.id = "c"

        g = Graph().add_nodes(a, b, c)
        d = g.to_dict()

        assert d == {
            "id": g.id,
            "nodes": [
                {"id": "a", "args": {"ax": 1}},
                {"id": "b", "args": {"bx": {FUTURE_ID_PLACEHOLDER: "ay"}}},
                {"id": "c", "args": {"cx": {FUTURE_ID_PLACEHOLDER: "byay"}}},
            ],
            "edges": [],
            "initial_args": {},
            "futures": [
                {
                    "id": "ay",
                    "directive": {
                        "type": "trace",
                        "op_stack": [
                            {"key": "y", "accessor": "attr", "future_id": None},
                        ],
                        "origin_node_id": "a",
                    },
                },
                {
                    "id": "byay",
                    "directive": {
                        "type": "trace",
                        "op_stack": [
                            {"key": "y", "accessor": "attr", "future_id": None},
                            {"future_id": "ay", "accessor": "item", "key": None},
                        ],
                        "origin_node_id": "b",
                    },
                },
            ],
        }


if __name__ == "__main__":
    unittest.main()
