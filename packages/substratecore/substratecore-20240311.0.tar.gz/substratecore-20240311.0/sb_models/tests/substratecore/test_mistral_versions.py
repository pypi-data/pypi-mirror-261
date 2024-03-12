import datetime
import unittest

import pytest

from sb_models.substratecore.mistral_versions import (
    ToMistralIn,
    FromMistralOut,
)
from sb_models.substratecore.deprecated_models import (
    ErrorOut,
    MistralIn,
)

# latest fully loaded model examples

mistral_in = {
    "prompts": [{"prompt": "foo"}, {"prompt": "bar"}],
    "temperature": 0.7,
    "max_tokens": 500,
    "num_completions": 2,
    "json_schema": None,
}

mistral_out_2023_12_12 = {
    "completions": [
        {
            "text": "foo1",
        },
        {
            "text": "foo2",
        },
        {
            "text": "bar1",
        },
        {
            "text": "bar2",
        },
    ],
}

mistral_out_2024_01_01 = [
    {
        "completions": ["foo1", "foo2"],
    },
    {
        "completions": ["bar1", "bar2"],
    },
]


@pytest.mark.unit
class MistralVersions(unittest.TestCase):
    def setUp(self) -> None:
        print(f"\n꩜{self._testMethodName}")

    def test_req_today_version(self) -> None:
        today_date = datetime.date.today().strftime("%Y-%m-%d")
        orig_req = mistral_in
        args = ToMistralIn(orig_req).from_version(today_date)
        self.assertIsInstance(args, MistralIn)
        self.assertEqual(args.dict(), mistral_in)

    def test_req_none_version(self) -> None:
        orig_req = mistral_in
        args = ToMistralIn(orig_req).from_version(None)
        self.assertIsInstance(args, MistralIn)
        self.assertEqual(args.dict(), mistral_in)

    def test_req_invalid_model(self) -> None:
        """invalid request"""
        orig_req = {"data": "foo"}
        args = ToMistralIn(orig_req).from_version("2023-12-15")
        self.assertEqual(
            args,
            ErrorOut(type="invalid_request_error", message="field required: ['prompts']"),
        )

    def test_out_latest(self) -> None:
        """latest version – no change"""
        today_date = datetime.date.today().strftime("%Y-%m-%d")
        res = FromMistralOut(mistral_out_2024_01_01).to_version(today_date)
        self.assertEqual(res, mistral_out_2024_01_01)

    def test_out_none(self) -> None:
        """latest version – no change"""
        res = FromMistralOut(mistral_out_2024_01_01).to_version(None)
        self.assertEqual(res, mistral_out_2024_01_01)

    # request versioning
    def test_req_multiprompt_2023_12_12(self) -> None:
        orig_req = {
            "prompts": ["foo", "bar"],
        }
        args = ToMistralIn(orig_req).from_version("2023-12-12")
        expected_req = {
            "prompts": [{"prompt": "foo"}, {"prompt": "bar"}],
        }
        assert args is not None
        self.assertEqual(args.dict(exclude_none=True, exclude_defaults=True), expected_req)

    def test_req_singleprompt_2023_12_12(self) -> None:
        orig_req = {"prompt": "foo"}
        args = ToMistralIn(orig_req).from_version("2023-12-12")
        expected_req = {
            "prompts": [{"prompt": "foo"}],
        }
        assert args is not None
        self.assertEqual(args.dict(exclude_none=True, exclude_defaults=True), expected_req)

    def test_req_input_prompts_2023_12_12(self) -> None:
        orig_req = {"input_prompts": ["foo"]}
        args = ToMistralIn(orig_req).from_version("2023-12-12")
        expected_req = {
            "prompts": [{"prompt": "foo"}],
        }
        assert args is not None
        self.assertEqual(args.dict(exclude_none=True, exclude_defaults=True), expected_req)

    # response versioning
    def test_res_2023_12_12(self) -> None:
        """old completions format -> new format"""
        res = FromMistralOut(mistral_out_2024_01_01).to_version("2023-12-12")
        print("res", res)
        self.assertEqual(res, mistral_out_2023_12_12)
