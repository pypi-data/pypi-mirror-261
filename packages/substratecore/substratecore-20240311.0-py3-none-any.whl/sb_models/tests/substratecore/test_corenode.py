import unittest

import pytest

from sb_models.substratecore.corenode import CoreNode
from sb_models.substratecore.base_future import FUTURE_ID_PLACEHOLDER


class FakeNode(CoreNode):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


@pytest.mark.unit
class TestCoreNode:
    """
    TODO:
    - output
    - rename ref->future
    """

    def test_id(self):
        a = FakeNode(num=1)
        d_a = a.to_dict()
        print(d_a)
        assert d_a["id"].startswith("FakeNode") == True
        assert "_" in d_a["id"]

    def test_1_node(self):
        a = FakeNode(num=1)
        a.id = "a_id"
        d_a = a.to_dict()
        assert d_a["id"] == "a_id"
        assert d_a["args"]["num"] == 1

    def test_2_nodes_ref(self):
        a = FakeNode(num=1)
        a.id = "a_id"
        b = FakeNode(num=a.future.num, str="b_str")
        b.id = "b_id"
        d_b = b.to_dict()
        assert d_b["id"] == "b_id"
        assert d_b["args"]["str"] == "b_str"
        assert FUTURE_ID_PLACEHOLDER in d_b["args"]["num"]
        op_key = d_b["args"]["num"][FUTURE_ID_PLACEHOLDER]
        print(op_key)
        assert "future" in op_key
        assert "_" in op_key


if __name__ == "__main__":
    unittest.main()
