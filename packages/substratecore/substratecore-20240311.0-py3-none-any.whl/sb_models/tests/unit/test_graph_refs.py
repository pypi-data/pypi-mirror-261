import os
import json
import unittest
from typing import Any, Dict

import pytest

from sb_models.graph.server_graph import ServerGraph

pytest_plugins = ("pytest_asyncio",)

from sb_models.graph.node import Node
from sb_models.substratecore.sb import sb
from sb_models.substratecore.client.graph import Graph
from sb_models.substratecore.client.future import Future


def load_fixture(name: str) -> Dict[str, Any]:
    root = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(root, f"fixtures/{name}.json")
    with open(path, "r") as f:
        data = json.load(f)
        return data


class FakeNode(Node):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    async def run(self, **kwargs):
        num = kwargs.get("num", self.args.get("num", 1))
        s = kwargs.get("str", self.args.get("str", None))
        nest = kwargs.get("nested", self.args.get("nested", None))
        return {"num": num, "str": s, "nested": nest}

    def __repr__(self):
        num_init = self.args.get("num")
        str_init = self.args.get("str")
        nest_init = self.args.get("nested")
        return f"FN(id: {self.id}, num:{num_init}, str:{str_init}, nested:{nest_init})"


@pytest.mark.unit
class TestGraphRefs:
    """
    Test graph ref deserialization and _make_implicit_dag.
    The truly e2e deser test is to load the graph from JSON.
    Sometimes we construct the nodes & graphs with classes -
    but that's syntactic sugar and never actually happens this way server-side.
    """

    @pytest.mark.asyncio
    async def test_text2text(self):
        """
        GenerateText -> GenerateText
        """
        d = load_fixture("text2text")
        g = ServerGraph.from_dict(d)
        implicit_dag = g._make_implicit_dag()
        implicit_nodes = implicit_dag.nodes()
        implicit_edges = implicit_dag.edges()
        assert list(implicit_nodes) == ["node_1", "node_2"]
        assert list(implicit_edges) == [("node_1", "node_2")]

    def test_setup_2_nodes(self):
        """
        NOTE: This test doesn't go through ser/de
        """
        a = Node(prompt="foo")
        a.id = "node_1"
        b = Node(prompt=a.future.text)
        b.id = "node_2"
        cg = Graph().add_node(a).add_node(b)
        g = ServerGraph.from_dict(cg.to_dict())
        implicit_dag = g._make_implicit_dag()
        implicit_edges = implicit_dag.edges()
        assert list(implicit_edges) == [(a.id, b.id)]

    def test_setup_2_nodes_deserialized(self):
        a = Node(prompt="foo")
        a.id = "node_1"
        b = Node(prompt=a.future.text)
        b.id = "node_2"
        cg = Graph().add_node(a).add_node(b)
        g = ServerGraph.from_dict(cg.to_dict())
        implicit_dag = g._make_implicit_dag()
        implicit_edges = implicit_dag.edges()
        assert list(implicit_edges) == [(a.id, b.id)]

    def test_setup_2_nodes_nested_refs(self):
        a = Node(prompt="foo")
        a.id = "node_1"
        b = Node(foo={"bar": [{"baz": a.future.text}]})
        b.id = "node_2"
        cg = Graph().add_node(a).add_node(b)
        g = ServerGraph.from_dict(cg.to_dict())
        implicit_dag = g._make_implicit_dag()
        implicit_edges = implicit_dag.edges()
        assert list(implicit_edges) == [(a.id, b.id)]

    def test_3_nodes_multiple_refs(self):
        a = Node(prompt="foo")
        a.id = "a"
        b = Node(foo={"bar": [{"baz": a.future.text}]})
        b.id = "b"
        c = Node(qux={"foo": b.future.results, "bar": a.future.text})
        c.id = "c"
        cg = Graph().add_node(a).add_node(b).add_node(c)
        g = ServerGraph.from_dict(cg.to_dict())
        serialized = g.to_dict()
        print(json.dumps(serialized, indent=2))
        implicit_dag = g._make_implicit_dag()
        implicit_edges = implicit_dag.edges()
        assert list(implicit_edges) == [(a.id, b.id), (a.id, c.id), (b.id, c.id)]

    def test_4_nodes_nested_index_ref(self):
        a = Node(prompt="foo")
        a.id = "a"
        b = Node(foo="bar")
        b.id = "b"
        c = Node(hello="bar")
        c.id = "c"
        d = Node(qux={"foo": b.future.results[a.future.results[c.future.idx]]})
        d.id = "d"
        cg = Graph().add_node(a).add_node(b).add_node(c).add_node(d)
        g = ServerGraph.from_dict(cg.to_dict())
        serialized = g.to_dict()
        print(json.dumps(serialized, indent=2))
        implicit_dag = g._make_implicit_dag()
        implicit_edges = implicit_dag.edges()
        assert {(c.id, a.id), (a.id, b.id), (b.id, d.id)} == set(implicit_edges)

    def test_5_nodes_nested_index_ref(self):
        z = Node(blue=1)
        z.id = "z_id"

        a = Node(num=1)
        a.id = "a_id"
        b = Node(str="b_str").output()
        b.id = "b_id"
        c = Node(num=3).output()
        c.id = "c_id"
        d = Node(qux={"foo": b.future.blahb[a.future.lsdijf[c.future.idx]]})
        d.id = "d_id"
        e = Node(boo=sb.concat("boo", d.future.baa[a.future.bee[z.future.fafa]]))
        e.id = "e_id"
        G = Graph().add_nodes(a, b, c, d, e, z)
        client_dict = G.to_dict()
        g = ServerGraph.from_dict(client_dict)
        serialized = g.to_dict()
        print(json.dumps(serialized, indent=2))
        implicit_dag = g._make_implicit_dag()
        implicit_edges = implicit_dag.edges()
        assert set(implicit_edges) == {
            (a.id, b.id),
            (c.id, a.id),
            (b.id, d.id),
            (d.id, e.id),
            (a.id, d.id),
            (z.id, a.id),
        }

    def test_3_nodes_static_index_ref(self):
        a = Node(prompt="foo")
        a.id = "a"
        b = Node(foo={"bar": [{"baz": a.future.text}]})
        b.id = "b"
        c = Node(qux={"foo": b.future.results[1]})
        c.id = "c"
        cg = Graph().add_node(a).add_node(b).add_node(c)
        g = ServerGraph.from_dict(cg.to_dict())
        serialized = g.to_dict()
        print(json.dumps(serialized, indent=2))
        implicit_dag = g._make_implicit_dag()
        implicit_edges = implicit_dag.edges()
        assert set(implicit_edges) == {(a.id, b.id), (b.id, c.id)}

    def test_invalid_future_access(self):
        """
        Invalid access patterns on a Future
        """
        a = Node(prompt="foo")
        ref: Future = sb.concat(a.future.text, "bar")  # type: ignore
        with pytest.raises(AttributeError):
            invalid_ref = ref.foo

    @pytest.mark.asyncio
    async def test_concat_unsupported_types(self):
        """
        Unsupported operands. We're not supporting most operations for now.
        """
        a = FakeNode(num=1, str="foo")
        with pytest.raises(TypeError):
            b = FakeNode(str="foo" + a.future.str).output()  # type: ignore
        with pytest.raises(TypeError):
            b = FakeNode(num=2 + a.future.num).output()  # type: ignore
        with pytest.raises(TypeError):
            b = FakeNode(num=a.future.num + 2).output()  # type: ignore
        with pytest.raises(TypeError):
            b = FakeNode(num=True + a.future.num).output()  # type: ignore
        with pytest.raises(TypeError):
            b = FakeNode(num=1 > a.future.num).output()  # type: ignore
        with pytest.raises(TypeError):
            b = FakeNode(num=1 - a.future.num).output()  # type: ignore
        with pytest.raises(TypeError):
            b = FakeNode(num=float(a.future.str)).output()  # type: ignore


if __name__ == "__main__":
    unittest.main()
