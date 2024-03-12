import pytest

from sb_models.graph.node import Node
from sb_models.substratecore.base_future import FUTURE_ID_PLACEHOLDER


class FooNode(Node):
    pass


@pytest.mark.unit
class TestNode:
    def test_to_dict(self):
        a = FooNode(foo=1)
        a.id = "a"

        assert a.to_dict() == {"id": "a", "args": {"foo": 1}}

        ref = a.future.bar
        ref.id = "future_id"
        b = FooNode(foo=ref)
        b.id = "b"
        assert b.to_dict() == {"id": "b", "args": {"foo": {FUTURE_ID_PLACEHOLDER: "future_id"}}}

    def test_futures_from_args(self):
        a = FooNode(foo=1)
        a.id = "a"
        assert a.futures_from_args == []

        ref = a.future.bar
        ref.id = "future_id"
        b = FooNode(foo=ref)
        b.id = "b"
        assert b.futures_from_args == [ref]
