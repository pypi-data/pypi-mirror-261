import json
import unittest
from typing import Optional
from unittest.mock import patch

import pytest

pytest_plugins = ("pytest_asyncio",)

from sb_models.graph.node import Node
from sb_models.types.request import SubstrateRequest
from sb_models.substratecore.sb import sb
from sb_models.graph.server_graph import ServerGraph
from sb_models.substratecore.client.graph import Graph


class FakeNode(Node):
    def __init__(self, **attr):
        super().__init__(**attr)

    async def run(self, req: Optional[SubstrateRequest] = None, **kwargs):
        num = kwargs.get("num", self.args.get("num", None))
        s = kwargs.get("str", self.args.get("str", None))
        nest = kwargs.get("nested", self.args.get("nested", None))
        return {"num": num, "str": s, "nested": nest}

    def __repr__(self):
        num_init = self.args.get("num")
        str_init = self.args.get("str")
        nest_init = self.args.get("nested")
        return f"FN(id: {self.id}, num:{num_init}, str:{str_init}, nested:{nest_init})"


def mock_node_init(attr):
    args = attr["args"]
    id = attr["id"]
    node = FakeNode(**args)
    node.id = id
    return node


@pytest.mark.unit
class TestGraphRun:
    """
    Test mocked run of graphs with refs
    """

    @pytest.mark.asyncio
    @patch("sb_models.graph.node.node_instance")
    async def test_sb_concat_right(self, mock_node_instance):
        mock_node_instance.side_effect = mock_node_init
        a = FakeNode(str="a_str")
        a.id = "a_id"
        concat_ref = sb.concat(a.future.str, "b_str")
        b = FakeNode(str=concat_ref).output()
        b.id = "b_id"
        G0 = Graph().add_node(a).add_node(b)
        dict = G0.to_dict()
        print(json.dumps(dict, indent=2))
        G = ServerGraph.from_dict(dict)
        assert G.DAG.number_of_nodes() == 2
        implicit_dag = G._make_implicit_dag()
        implicit_edges = implicit_dag.edges()
        assert list(implicit_edges) == [(a.id, b.id)]
        res = await G.run(verbose=False)
        assert [b] == list(res.keys())
        assert res[b] == {"str": "a_strb_str", "num": None, "nested": None}

    @pytest.mark.asyncio
    @patch("sb_models.graph.node.node_instance")
    async def test_sb_concat_left(self, mock_node_instance):
        mock_node_instance.side_effect = mock_node_init
        a = FakeNode(str="a_str")
        a.id = "a_id"
        b = FakeNode(str=sb.concat("b_str", a.future.str)).output()
        b.id = "b_id"
        G0 = Graph().add_node(a).add_node(b)
        d = G0.to_dict()
        G = ServerGraph.from_dict(d)
        assert G.DAG.number_of_nodes() == 2
        implicit_dag = G._make_implicit_dag()
        implicit_nodes = implicit_dag.nodes()
        implicit_edges = implicit_dag.edges()
        assert list(implicit_nodes) == [a.id, b.id]
        assert list(implicit_edges) == [(a.id, b.id)]
        res = await G.run(verbose=False)
        assert [b] == list(res.keys())
        assert res[b] == {
            "str": "b_stra_str",
            "num": None,
            "nested": None,
        }

    @pytest.mark.asyncio
    @patch("sb_models.graph.node.node_instance")
    async def test_sb_concat_2_futures(self, mock_node_instance):
        mock_node_instance.side_effect = mock_node_init
        a = FakeNode(str="a_str")
        a.id = "a_id"
        b = FakeNode(str="b_str")
        b.id = "b_id"
        c = FakeNode(str=sb.concat(a.future.str, b.future.str)).output()
        c.id = "c_id"
        G0 = Graph().add_node(a).add_node(b).add_node(c)
        d = G0.to_dict()
        G = ServerGraph.from_dict(d)
        assert G.DAG.number_of_nodes() == 3
        implicit_dag = G._make_implicit_dag()
        implicit_nodes = implicit_dag.nodes()
        implicit_edges = implicit_dag.edges()
        assert set(implicit_nodes) == {b.id, c.id, a.id}
        assert set(implicit_edges) == {(b.id, c.id), (a.id, c.id)}
        res = await G.run(verbose=False)
        assert [c] == list(res.keys())
        assert res[c] == {"str": "a_strb_str", "num": None, "nested": None}

    @pytest.mark.asyncio
    @patch("sb_models.graph.node.node_instance")
    async def test_sb_concat_multiple(self, mock_node_instance):
        mock_node_instance.side_effect = mock_node_init
        a = FakeNode(str="a_str")
        a.id = "a_id"
        b = FakeNode(str="b_str")
        b.id = "b_id"
        c = FakeNode(str=sb.concat("(", a.future.str, ",", b.future.str, ")")).output()
        c.id = "c_id"
        G0 = Graph().add_node(a).add_node(b).add_node(c)
        d = G0.to_dict()
        G = ServerGraph.from_dict(d)
        assert G.DAG.number_of_nodes() == 3
        implicit_dag = G._make_implicit_dag()
        implicit_nodes = implicit_dag.nodes()
        implicit_edges = implicit_dag.edges()
        assert set(implicit_nodes) == {b.id, c.id, a.id}
        assert set(implicit_edges) == {(b.id, c.id), (a.id, c.id)}
        res = await G.run(verbose=False)
        assert [c] == list(res.keys())
        assert res[c] == {"str": "(a_str,b_str)", "num": None, "nested": None}

    @pytest.mark.asyncio
    @patch("sb_models.graph.node.node_instance")
    async def test_3_nodes_ref_index(self, mock_node_instance):
        mock_node_instance.side_effect = mock_node_init
        a = FakeNode(num=1)
        a.id = "a_id"
        b = FakeNode(num=a.future.num, str="b_str", nested=[{"key": "b_nest_1"}, {"key": "b_nest_2"}]).output()
        b.id = "b_id"
        c = FakeNode(num=3, str=b.future.nested[a.future.num].key, nested=[{"key": b.future.str}]).output()
        c.id = "c_id"
        G0 = Graph().add_node(a).add_node(b).add_node(c)
        d = G0.to_dict()
        G = ServerGraph.from_dict(d)
        assert G.DAG.number_of_nodes() == 3
        # check internal graph representation
        implicit_dag = G._make_implicit_dag()
        implicit_edges = implicit_dag.edges()
        assert list(implicit_edges) == [(a.id, b.id), (b.id, c.id)]
        # run and check result
        res = await G.run(verbose=False)
        assert [b, c], list(res.keys())
        assert res[b] == {
            "num": 1,
            "str": "b_str",
            "nested": [{"key": "b_nest_1"}, {"key": "b_nest_2"}],
        }
        assert res[c] == {
            "num": 3,
            "str": "b_nest_2",
            "nested": [{"key": "b_str"}],
        }

    @pytest.mark.asyncio
    @patch("sb_models.graph.node.node_instance")
    async def test_3_nodes_nested_ref_index(self, mock_node_instance):
        mock_node_instance.side_effect = mock_node_init
        a = FakeNode(num=1)
        a.id = "a_id"
        b = FakeNode(num=a.future.num, str="b_str", nested=[{"key": "b_nest_1"}, {"foo": {"bar": 8}}]).output()
        b.id = "b_id"
        c = FakeNode(num=3, str=b.future.str, nested=[{"key": b.future.nested[a.future.num].foo}]).output()
        c.id = "c_id"
        G0 = Graph().add_node(a).add_node(b).add_node(c)
        d = G0.to_dict()
        G = ServerGraph.from_dict(d)
        assert G.DAG.number_of_nodes() == 3
        # check internal graph representation
        implicit_dag = G._make_implicit_dag()
        implicit_edges = implicit_dag.edges()
        assert list(implicit_edges) == [(a.id, b.id), (b.id, c.id)]
        # run and check result
        res = await G.run(verbose=False)
        assert [b, c] == list(res.keys())
        assert res[b] == {
            "num": 1,
            "str": "b_str",
            "nested": [{"key": "b_nest_1"}, {"foo": {"bar": 8}}],
        }
        assert res[c] == {
            "num": 3,
            "str": "b_str",
            "nested": [{"key": {"bar": 8}}],
        }

    @pytest.mark.asyncio
    @patch("sb_models.graph.node.node_instance")
    async def test_nodes_nested_wit_concat(self, mock_node_instance):
        mock_node_instance.side_effect = mock_node_init
        a = FakeNode(num=1)
        a.id = "a_id"
        b = FakeNode(num=a.future.num, str="b_str", nested=[{"key": "b_nest_1"}, {"foo": {"bar": 8}}]).output()
        b.id = "b_id"
        c = FakeNode(
            num=3,
            str=sb.concat(sb.concat(b.future.str, b.future.nested[0].key), "888"),
            # TODO(rob) test futures used as keys
            # nested=[{sb.concat("key", "_concat"): b.future.nested[a.future.num].foo}],
            nested=[{"key": b.future.nested[a.future.num].foo}],
        ).output()
        c.id = "c_id"
        G0 = Graph().add_node(a).add_node(b).add_node(c)
        d = G0.to_dict()
        G = ServerGraph.from_dict(d)
        assert G.DAG.number_of_nodes() == 3
        # check internal graph representation
        implicit_dag = G._make_implicit_dag()
        implicit_edges = implicit_dag.edges()
        assert list(implicit_edges) == [(a.id, b.id), (b.id, c.id)]
        # run and check result
        res = await G.run(verbose=False)
        assert [b, c] == list(res.keys())
        assert res[b] == {
            "num": 1,
            "str": "b_str",
            "nested": [{"key": "b_nest_1"}, {"foo": {"bar": 8}}],
        }
        assert res[c] == {
            "num": 3,
            "str": "b_strb_nest_1888",
            "nested": [{"key": {"bar": 8}}],
        }

    @pytest.mark.asyncio
    @patch("sb_models.graph.node.node_instance")
    async def test_3_nodes_dependent_refs(self, mock_node_instance):
        mock_node_instance.side_effect = mock_node_init
        a = FakeNode(num=1)
        a.id = "a_id"
        b = FakeNode(str="b_str", nested=[{"key": "b_nest_1"}, {"key": "b_nest_2"}]).output()
        b.id = "b_id"
        c0 = FakeNode(num=3, str=b.future.str, nested=[{"key": a.future.num}]).output()
        c0.id = "c0_id"
        G0 = Graph().add_node(a).add_node(b).add_node(c0)
        assert G0.DAG.number_of_nodes() == 3
        d0 = G0.to_dict()
        G = ServerGraph.from_dict(d0)
        implicit_dag = G._make_implicit_dag()
        implicit_nodes = implicit_dag.nodes()
        implicit_edges = implicit_dag.edges()
        assert list(implicit_nodes) == [b.id, c0.id, a.id]
        assert list(implicit_edges) == [(b.id, c0.id), (a.id, c0.id)]
        # c1's args create an edge where b depends on a - this edge doesn't exist otherwise
        c1 = FakeNode(num=3, str=b.future.str, nested=[{"key": b.future.nested[a.future.num].key}]).output()
        c1.id = "c1_id"
        G1 = ServerGraph().add_node(a).add_node(b).add_node(c1)
        assert G1.DAG.number_of_nodes() == 3
        d1 = G1.to_dict()
        G = ServerGraph.from_dict(d1)
        # check internal graph representation
        implicit_dag = G._make_implicit_dag()
        implicit_nodes = implicit_dag.nodes()
        implicit_edges = implicit_dag.edges()
        assert list(implicit_nodes) == [b.id, c1.id, a.id]
        assert list(implicit_edges) == [(b.id, c1.id), (a.id, c1.id), (a.id, b.id)]
        # run and check result
        res = await G.run(verbose=False)
        assert [b, c1], list(res.keys())
        assert res[b] == {
            "num": None,
            "str": "b_str",
            "nested": [{"key": "b_nest_1"}, {"key": "b_nest_2"}],
        }
        assert res[c1] == {
            "num": 3,
            "str": "b_str",
            "nested": [{"key": "b_nest_2"}],
        }

    @pytest.mark.asyncio
    @patch("sb_models.graph.node.node_instance")
    async def test_3_nodes_dependent_refs(self, mock_node_instance):
        mock_node_instance.side_effect = mock_node_init
        z = Node(blue=1)
        z.id = "z_id"
        a = Node(num=1)
        a.id = "a_id"
        b = Node(str="b_str").output()
        b.id = "b_id"
        c = Node(num=3).output()
        c.id = "c_id"
        d = Node(qux={"foo": b.future.results[a.future.results[c.future.idx]]})
        d.id = "d_id"
        e = Node(boo=sb.concat("boo", d.future.baa[a.future.bee[z.future.fafa]]))
        e.id = "e_id"
        G = Graph().add_nodes(a, b, c, d, e, z)
        SG = ServerGraph.from_dict(G.to_dict())
        print(json.dumps(G.to_dict(), indent=2))
        implicit_dag = SG._make_implicit_dag()
        implicit_edges = implicit_dag.edges()
        assert set(implicit_edges) == {
            (a.id, b.id),
            (c.id, a.id),
            (b.id, d.id),
            (d.id, e.id),
            (a.id, d.id),
            (z.id, a.id),
        }


if __name__ == "__main__":
    unittest.main()
