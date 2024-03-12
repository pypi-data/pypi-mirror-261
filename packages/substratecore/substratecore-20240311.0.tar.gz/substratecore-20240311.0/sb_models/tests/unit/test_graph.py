import unittest
from unittest import mock

import pytest

pytest_plugins = ("pytest_asyncio",)


from sb_models.graph.node import Node, Adapter
from sb_models.types.outputs import TextCompletion, TextGeneration
from sb_models.graph.adapters import AdapterTransform
from sb_models.graph.server_graph import ServerGraph

FAKE_TG = TextGeneration(
    completions=[TextCompletion(text="sancho panza", token_count=12)],
    token_count=12,
)

my_num_to_y = Adapter(source_key="my_num", dest_key="y")
sum_to_y = Adapter(source_key="sum", dest_key="y")
ary_to_values = Adapter(source_key="ary", dest_key="values")
prod_to_y = Adapter(source_key="product", dest_key="y")


def fake_node_run(**kwargs):
    if kwargs["fn"] == "add":
        return {"sum": kwargs["x"] + kwargs["y"]}
    elif kwargs["fn"] == "mult":
        return {"product": kwargs["x"] * kwargs["y"]}
    elif kwargs["fn"] == "ary":
        return {"ary": [kwargs["x"], kwargs["y"]]}


@pytest.mark.unit
class TestGraph:
    def test_pipe(self):
        """
        Demonstrate pipe api expectations. Pipe operator should return the root node
        ╙── Node(a)
            └─╼ Node(b)
                └─╼ Node(c)
                    └─╼ Node(d)
        """
        G = ServerGraph()
        b = Node(name="b")
        c = Node(name="c")
        d = Node(name="d")

        c.pipe(d)
        b.pipe(c)
        a = Node(name="a").pipe(b)

        G.add_node(a)

        assert G.DAG.number_of_nodes() == 4
        assert G.DAG.number_of_edges() == 3

    def test_nested_with_siblings(self):
        """
        Results in the graph with structure:

        ╙── Node(root)
            └─╼ Node(child)
                ├─╼ Node(grandchild-1)
                ├─╼ Node(grandchild-2)
                └─╼ Node(grandchild-3)
        :return:
        """
        G = ServerGraph()
        child = Node(name="child")
        root = Node(name="root").pipe(
            child.pipe([Node(name="grandchild-1"), Node(name="grandchild-2"), Node(name="grandchild-3")])
        )

        G.add_node(root)

        assert G.DAG.number_of_nodes() == 5
        assert G.DAG.number_of_edges() == 4
        assert len(G.DAG[child]) == 3

    @pytest.mark.asyncio
    async def test_run_default(self):
        with mock.patch("sb_models.graph.node.Node.run") as mock_run:
            mock_run.side_effect = fake_node_run
            G = ServerGraph(y=2)  # initial arg
            final = Node(fn="mult", x=6)
            root = (
                Node(fn="add", x=1)
                .adapt_to(sum_to_y)
                .pipe(  # 1 + 2 = 3
                    Node(fn="mult", x=2).adapt_to(prod_to_y).pipe(final)  # 3 * 2 = 6
                )
            )  # 6 * 6 = 36

            G.add_node(root)
            outputs = await G.run()

        # By default, output the last node if it is a simple straight pipeline
        assert len(outputs) == 1
        assert outputs.first() == {"product": 36}
        assert {final.id: {"product": 36}} == outputs.to_dict()

    @pytest.mark.asyncio
    async def test_run_from_adapter(self):
        with mock.patch("sb_models.graph.node.Node.run") as mock_run:
            mock_run.side_effect = fake_node_run
            G = ServerGraph(my_num=2)  # initial arg
            final = Node(fn="mult", x=6).adapt_from(prod_to_y)
            root = (
                Node(fn="add", x=1)
                .adapt_from(my_num_to_y)
                .pipe(  # 1 + 2 = 3
                    Node(fn="mult", x=2).adapt_from(sum_to_y).pipe(final),  # 3 * 2 = 6
                )
            )  # 6 * 6 = 36

            G.add_node(root)
            outputs = await G.run()

        # By default, output the last node if it is a simple straight pipeline
        assert len(outputs) == 1
        assert outputs.first() == {"product": 36}
        assert {final.id: {"product": 36}} == outputs.to_dict()

    @pytest.mark.asyncio
    async def test_edge_data_adapter(self):
        with mock.patch("sb_models.graph.node.Node.run") as mock_run:
            mock_run.side_effect = fake_node_run
            G = ServerGraph(y=2)  # initial arg
            root = (
                Node(fn="add", x=1)
                .adapt_to(sum_to_y)
                .pipe(  # 1 + 2 = 3
                    Node(fn="mult", x=2)
                    .adapt_to(prod_to_y)
                    .pipe(
                        Node(fn="mult", x=6),
                    )  # 6 * 6 = 36  # 3 * 2 = 6
                )
            )

            G.add_node(root)
            outputs = await G.run()

        # By default, output the last node if it is a simple straight pipeline
        assert len(outputs) == 1
        assert outputs.first() == {"product": 36}

    @pytest.mark.asyncio
    async def test_run_output(self):
        with mock.patch("sb_models.graph.node.Node.run") as mock_run:
            mock_run.side_effect = fake_node_run
            G = ServerGraph(y=2)  # initial arg
            root = (
                Node(fn="add", x=1)
                .adapt_to(sum_to_y)
                .pipe(  # 1 + 2 = 3
                    Node(fn="mult", x=2)
                    .adapt_to(prod_to_y)  # 3 * 2 = 6
                    .pipe(
                        Node(fn="mult", x=6)
                        .adapt_to(prod_to_y)
                        .output()  # 6 * 6 = 36
                        .pipe(
                            Node(fn="add", x=4),
                        )
                    )
                )
            )  # 36 + 4 = 40

            G.add_node(root)
            outputs = await G.run()

        assert len(outputs) == 1
        assert outputs.first() == {"product": 36}

    @pytest.mark.asyncio
    async def test_run_multi_out(self):
        with mock.patch("sb_models.graph.node.Node.run") as mock_run:
            mock_run.side_effect = fake_node_run
            G = ServerGraph(y=2)  # initial arg
            root = (
                Node(fn="add", x=1)
                .adapt_to(sum_to_y)
                .pipe(  # 1 + 2 = 3
                    Node(fn="mult", x=2)
                    .adapt_to(prod_to_y)
                    .output()  # 3 * 2 = 6
                    .pipe(Node(fn="mult", x=3).adapt_to(prod_to_y).output())
                )
            )  # 6 * 3 = 18

            G.add_node(root)
            outputs = await G.run()

        assert len(outputs) == 2
        assert list(outputs.values()) == [{"product": 6}, {"product": 18}]

    def test_to_dict(self):
        G = ServerGraph(y=2)
        add = Node(fn="add", x=1).adapt_to(sum_to_y)
        mult = Node(fn="mult", x=2)
        root = add.pipe(mult)
        G.add_node(root)
        as_dict = G.to_dict()
        assert as_dict["initial_args"] == {"y": 2}
        assert as_dict["nodes"] == [n.to_dict() for n in G.DAG.nodes()]
        assert as_dict["edges"] == [[add.id, mult.id, {}]]

    def test_adapter(self):
        get_text = Adapter(
            source_key="completions",
            dest_key="texts",
            transform=AdapterTransform.get,
            transform_args={"path": "completions[0].text"},
        )
        path_get = get_text.apply(FAKE_TG)
        assert path_get["texts"] == "sancho panza"
        wrap_in_list = Adapter(source_key="texts", transform=AdapterTransform.wrap_in_list)
        wrap_list = wrap_in_list.apply(path_get)
        assert wrap_list["texts"] == ["sancho panza"]
        pick_texts = Adapter(
            transform=AdapterTransform.pick,
            transform_args={"keys": ["texts"]},
        )
        pick = pick_texts.apply(wrap_list)
        assert pick == {"texts": ["sancho panza"]}

    def test_from_dict(self):
        G = ServerGraph()
        add = Node(fn="add", x=1).adapt_to(sum_to_y)
        mult = Node(fn="mult", x=2)
        root = add.pipe(mult)
        G.add_node(root)
        as_dict = G.to_dict()
        G2 = ServerGraph.from_dict(as_dict)
        assert G2.to_dict() == as_dict


if __name__ == "__main__":
    unittest.main()
