import datetime
import unittest

import pytest

from sb_models.substratecore.deprecated_models import (
    ErrorOut,
    StableDiffusionXLIn,
)
from sb_models.substratecore.stablediffusion_versions import (
    ToStableDiffusionXLIn,
)

# latest fully loaded model examples

sd_in = {
    "prompt": "foo",
    "negative_prompt": "bar",
    "store": True,
    "width": 512,
    "height": 512,
    "steps": 4,
    "seed": 8888,
    "guidance_scale": 8,
    "num_images": 2,
}

sd_in_2023_12_12 = {  # substack
    "prompt": "don quixote",
    "width": 800,
    "height": 512,
    "steps": 4,
    "num_images": 2,
    "use_ssd": False,
    "use_refiner": False,
    "use_turbo": True,
    "guidance_scale": 0.0,
    "return_base64": True,
}


@pytest.mark.unit
class StableDiffusionVersions(unittest.TestCase):
    def setUp(self) -> None:
        print(f"\n꩜{self._testMethodName}")

    def test_xlreq_today_version(self) -> None:
        today_date = datetime.date.today().strftime("%Y-%m-%d")
        orig_req = {
            **sd_in,  # Private params
            "use_ssd": True,
            "use_refiner": True,
        }
        args = ToStableDiffusionXLIn(orig_req).from_version(today_date)
        self.assertIsInstance(args, StableDiffusionXLIn)
        self.assertEqual(args.dict(exclude_none=True), orig_req)
        self.assertTrue(args.dict()["use_ssd"])
        self.assertTrue(args.dict()["use_refiner"])

    def test_xlreq_none_version(self) -> None:
        orig_req = sd_in
        args = ToStableDiffusionXLIn(orig_req).from_version(None)
        self.assertIsInstance(args, StableDiffusionXLIn)
        self.assertEqual(args.dict(exclude_none=True), orig_req)

    def test_xlreq_invalid_model(self) -> None:
        """invalid request"""
        orig_req = {"data": "foo"}
        args = ToStableDiffusionXLIn(orig_req).from_version(None)
        self.assertEqual(
            args,
            ErrorOut(type="invalid_request_error", message="field required: ['prompt']"),
        )

    # Versions
    # substack
    def test_xlreq_2023_12_12(self) -> None:
        args = ToStableDiffusionXLIn(sd_in_2023_12_12).from_version("2023-12-12")
        print(args)
        assert args is not None
        assert not isinstance(args, ErrorOut)
        self.assertEqual(args.store, False)
        self.assertEqual(args.width, 800)
        self.assertEqual(args.height, 512)
        self.assertEqual(args.num_images, 2)
        self.assertEqual(args.guidance_scale, 0.0)
        self.assertEqual(args.steps, 4)
        self.assertEqual(args.prompt, "don quixote")
        self.assertEqual(args.dict()["use_ssd"], False)
        self.assertEqual(args.dict()["use_refiner"], False)
        self.assertEqual(args.dict()["use_turbo"], True)

    def test_xlreq_2023_12_12_full(self) -> None:
        orig_req = {
            "prompt": "foo",
            "negative_prompt": "bar",
            "use_hosted_url": True,  # -> store
            "width": 512,
            "height": 512,
            "steps": 4,
            "seed": 8888,
            "n": 2,  # -> num_images
            # Private params
            "use_ssd": True,
            "use_refiner": True,
            "guidance_scale": True,
        }
        args = ToStableDiffusionXLIn(orig_req).from_version("2023-12-12")
        expected_req = {
            "prompt": "foo",
            "negative_prompt": "bar",
            "store": True,
            "width": 512,
            "height": 512,
            "steps": 4,
            "seed": 8888,
            "num_images": 2,
            "use_ssd": True,
            "use_refiner": True,
            "guidance_scale": True,
        }
        assert args is not None
        print(args.dict())
        self.assertTrue(args.dict()["use_ssd"])
        self.assertTrue(args.dict()["use_refiner"])
        self.assertTrue(args.dict()["guidance_scale"])
        self.assertEqual(args.dict(exclude_none=True), expected_req)
