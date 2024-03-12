import datetime
import unittest

import pytest

from sb_models.substratecore.jina_versions import (
    ToJinaIn,
    FromJinaOut,
)
from sb_models.substratecore.deprecated_models import (
    JinaIn,
    ErrorOut,
)

# latest fully loaded model examples

jina_in = {
    "docs": [
        {
            "text": "text_1",
            "id": "id_1",
            "metadata": {"meta_1": "val_1"},
            "embed_metadata_keys": ["meta_1", "meta_2"],
        },
        {
            "text": "text_2",
            "id": "id_2",
            "metadata": {"meta_2": "val_2"},
            "embed_metadata_keys": ["meta_1", "meta_2"],
        },
    ],
    "store": "collection_id",
}

jina_out_2024_12_12 = [
    {
        "id": "id_1",
        "vector": [0.1, -0.1],
        "metadata": {"doc_id": 123, "doc": "text_1", "boolean": True},
    },
    {
        "id": "id_1",
        "vector": [-0.2, 0.2],
        "metadata": {"doc_id": 456, "doc": "text_1", "boolean": False},
    },
]

# Substack expects a list of lists
jina_out_2023_12_12 = [
    [
        {
            "id": "id_1",
            "vec": [0.1, -0.1],
            "meta": {"doc_id": 123, "doc": "text_1", "boolean": True},
        }
    ],
    [
        {
            "id": "id_1",
            "vec": [-0.2, 0.2],
            "meta": {"doc_id": 456, "doc": "text_1", "boolean": False},
        }
    ],
]


@pytest.mark.unit
class JinaVersions(unittest.TestCase):
    def setUp(self) -> None:
        print(f"\n꩜{self._testMethodName}")

    def test_req_today_version(self) -> None:
        today_date = datetime.date.today().strftime("%Y-%m-%d")
        orig_req = jina_in
        args = ToJinaIn(orig_req).from_version(today_date)
        self.assertIsInstance(args, JinaIn)
        self.assertEqual(args.dict(), jina_in)

    def test_req_none_version(self) -> None:
        orig_req = jina_in
        args = ToJinaIn(orig_req).from_version(None)
        self.assertIsInstance(args, JinaIn)
        self.assertEqual(args.dict(), jina_in)

    def test_req_invalid_model(self) -> None:
        """invalid request"""
        orig_req = {"data": "foo"}
        args = ToJinaIn(orig_req).from_version(None)
        self.assertEqual(
            args,
            ErrorOut(type="invalid_request_error", message="field required: ['docs']"),
        )

    def test_out_latest(self) -> None:
        """latest version – no change"""
        today_date = datetime.date.today().strftime("%Y-%m-%d")
        res = FromJinaOut(jina_out_2024_12_12).to_version(today_date)
        self.assertEqual(res, jina_out_2024_12_12)

    def test_req_duplicate_ids(self) -> None:
        """invalid request"""
        docs = [{"text": "foo", "id": "123"} for i in range(3)]
        req = {"docs": docs, "store": "foo"}
        args = ToJinaIn(req).from_version(None)
        self.assertEqual(
            args,
            ErrorOut(
                type="invalid_request_error",
                message="Can't store documents with duplicate ids: {'123'}",
            ),
        )

    def test_req_partial_metadata(self) -> None:
        """invalid request – TODO: update impl and remove constraint"""
        docs = [
            {"text": "foo", "id": "123", "metadata": {"foo": "bar"}},
            {"text": "foo", "id": "456"},
        ]
        req = {"docs": docs, "store": "foo"}
        args = ToJinaIn(req).from_version(None)
        self.assertEqual(
            args,
            ErrorOut(
                type="invalid_request_error",
                message="When using metadata all docs must include metadata",
            ),
        )

    def test_req_partial_embed_metadata_keys(self) -> None:
        """invalid request - TODO: update impl and remove constraint"""
        docs = [
            {
                "text": "foo",
                "id": "123",
                "metadata": {"foo": "bar"},
                "embed_metadata_keys": ["foo"],
            },
            {"text": "foo", "id": "456", "metadata": {"foo": "bar"}},
        ]
        req = {"docs": docs, "store": "foo"}
        args = ToJinaIn(req).from_version(None)
        self.assertEqual(
            args,
            ErrorOut(
                type="invalid_request_error",
                message="When using embed_metadata_keys all docs must include embed_metadata_keys",
            ),
        )

    # request versioning
    def test_req_2023_12_12(self) -> None:
        """collection -> store"""
        orig_req = {
            "collection": "collection_id",
            "texts": ["text_1", "text_2"],
            "ids": ["id_1", "id_2"],
            "metadatas": [{"meta_1": "val_1"}, {"meta_2": "val_2"}],
            "embed_metadata_keys": ["meta_1", "meta_2"],
        }
        args = ToJinaIn(orig_req).from_version("2023-12-12")
        expected_req = {
            "docs": [
                {
                    "text": "text_1",
                    "id": "id_1",
                    "metadata": {"meta_1": "val_1"},
                    "embed_metadata_keys": ["meta_1", "meta_2"],
                },
                {
                    "text": "text_2",
                    "id": "id_2",
                    "metadata": {"meta_2": "val_2"},
                    "embed_metadata_keys": ["meta_1", "meta_2"],
                },
            ],
            "store": "collection_id",
        }
        assert args is not None
        self.assertEqual(args.dict(exclude_none=True), expected_req)

    def test_req_2023_12_12_substack_compose(self) -> None:
        """
        store_info.collection -> store
        store_info.full_metadata -> metadata
        """
        orig_req = {
            "store_info": {
                "collection": "collection_id",
                "full_metadata": [
                    {
                        "title": "title_1",
                        "publication_id": 12345,
                        "boolean": True,
                    },
                    {
                        "title": "title_2",
                        "publication_id": 34567,
                        "boolean": False,
                    },
                ],
            },
            "split": False,
            "texts": ["text_1", "text_2"],
            "provider_ids": ["id_1", "id_2"],
            "embed_metadata_keys": ["title"],
        }
        args = ToJinaIn(orig_req).from_version("2023-12-12")
        expected_req = {
            "docs": [
                {
                    "text": "text_1",
                    "id": "id_1",
                    "metadata": {
                        "title": "title_1",
                        "publication_id": 12345,
                        "boolean": True,
                    },
                    "embed_metadata_keys": ["title"],
                },
                {
                    "text": "text_2",
                    "id": "id_2",
                    "metadata": {
                        "title": "title_2",
                        "publication_id": 34567,
                        "boolean": False,
                    },
                    "embed_metadata_keys": ["title"],
                },
            ],
            "store": "collection_id",
        }
        assert args is not None
        self.assertEqual(args.dict(), expected_req)

    # response versioning
    def test_res_2023_12_12(self) -> None:
        """
        original version
        """
        res = FromJinaOut(jina_out_2024_12_12).to_version("2023-12-12")
        self.assertEqual(res, jina_out_2023_12_12)

    def test_res_no_version(self) -> None:
        """
        assume no version header -> original version
        """
        res = FromJinaOut(jina_out_2024_12_12).to_version(None)
        self.assertEqual(res, jina_out_2024_12_12)
