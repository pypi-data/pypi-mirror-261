import os
import json
import unittest
import subprocess
from typing import Any, Dict

import pytest
import requests

from scripts.modal_cmd import set_env, create_env, delete_env, deploy_apps, is_modal_env
from sb_models.types.request import RequestInfo, SubstrateRequest
from sb_models.graph.modal_nodes import ModalNode, ModalHandle
from sb_models.graph.server_graph import ServerGraph


def load_fixture(name: str) -> Dict[str, Any]:
    root = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(root, f"fixtures/{name}.json")
    with open(path, "r") as f:
        data = json.load(f)
        return data


def mock_req(version: str) -> SubstrateRequest:
    info = RequestInfo(
        method="mock",
        path="mock",
        headers={"x-substrate-version": version},
        query={},
    )
    req = SubstrateRequest(request=info, proxy_path="mock")
    return req


@pytest.mark.e2e
class E2E(unittest.IsolatedAsyncioTestCase):
    """
    End-to-end tests for live production usage of the API
    """

    @classmethod
    def setUpClass(cls) -> None:
        git_sha = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], text=True).strip()
        env = f"ci-{git_sha}"
        is_ci = os.environ.get("IS_GHA")
        if is_ci:
            cls.modal_env = env
            has_env = is_modal_env(env)
            if not has_env:
                print("Setting up CI environment")
                create_env(env)
            else:
                print(f"Using existing CI environment: {env}")
            print(f"Deploying to environment: {env}")
            deploy_apps(
                [
                    "compose/compose",
                    "jina_embedding/jina_base_v2",
                    "mistral/mistral_7b_instruct",
                    "sdxl/sdxl",
                    "whisper/wx",
                    "usage",
                    "datadog",
                ],
                env,
            )
            set_env(env)
            os.environ["MODAL_ENVIRONMENT"] = env
        else:
            cls.modal_env = "test"
            print("Running in 'test' environment")

    @classmethod
    def tearDownClass(cls) -> None:
        is_ci = os.environ.get("IS_GHA")
        if is_ci and cls.modal_env != "test":
            print(f"Deleting CI environment: {cls.modal_env}")
            delete_env(cls.modal_env)

    def setUp(self) -> None:
        print(f"\n꩜{self._testMethodName}")

    async def test_mistral_substack(self):
        g = ServerGraph()
        g.add_node(
            ModalNode(
                model=ModalHandle.mistral7b_instruct,
                environment=E2E.modal_env,
                **load_fixture("requests/mistral_substack"),
            )
        )
        outputs = await g.run(req=mock_req("2023-12-12"))
        self.assertEqual(len(outputs), 1)
        output = outputs.first()
        print(json.dumps(output, indent=2))
        self.assertIn("Don Quixote", output["completions"][0]["text"])

    async def test_mistral_substack_json(self):
        from typing import List

        from pydantic import BaseModel, schema_json_of

        class Response(BaseModel):
            title: str
            topics: List[str]
            short_summary: str
            extended_summary: str

        json_schema = schema_json_of(Response)
        print(json_schema)

        g = ServerGraph()
        g.add_node(
            ModalNode(
                model=ModalHandle.mistral7b_instruct,
                environment=E2E.modal_env,
                **load_fixture("requests/mistral_substack"),
                json_schema=json_schema,
            )
        )
        outputs = await g.run(req=mock_req("2023-12-12"))
        self.assertEqual(len(outputs), 1)
        output = outputs.first()
        print(json.dumps(output, indent=2))
        completion = output["completions"][0]
        self.assertIsNone(completion.get("text"))
        self.assertIsNotNone(completion["json"])

    async def test_sdxl_substack(self):
        g = ServerGraph()
        g.add_node(
            ModalNode(
                model=ModalHandle.stablediffusionxl,
                environment=E2E.modal_env,
                variant_args={"use_turbo": True, "use_refiner": False},
                **load_fixture("requests/stablediffusion_substack"),
            )
        )
        outputs = await g.run(req=mock_req("2023-12-12"))
        output = outputs.first()
        self.assertGreater(len(output[0]["uri"]), 120)  # base64 image data

    async def test_jina_substack(self):
        g = ServerGraph()
        g.add_node(
            ModalNode(
                model=ModalHandle.jinav2,
                environment=E2E.modal_env,
                **load_fixture("requests/jina_substack"),
            )
        )
        outputs = await g.run(req=mock_req("2023-12-12"))
        self.assertEqual(len(outputs), 1)
        output = outputs.first()
        self.assertEqual(5, len(output))
        emb = output[0][0]
        self.assertEqual(emb["id"], "46804987")
        self.assertEqual(len(emb["vec"]), 768)
        self.assertEqual(emb["meta"]["doc"], "<redacted_string>")

    async def test_whisper_substack(self):
        g = ServerGraph()
        g.add_node(
            ModalNode(
                model=ModalHandle.whisper,
                environment=E2E.modal_env,
                **{
                    "audio_url": "https://media.substrate.run/chess.mp3",
                    "align": True,
                    "diarize": False,
                    "suggest_chapters": False,
                    "return_segments": True,
                },
            )
        )
        outputs = await g.run(req=mock_req("2023-12-12"))
        self.assertEqual(len(outputs), 1)
        output = outputs.first()
        self.assertIsNotNone(output.get("text"))
        self.assertGreater(len(output.get("segments")), 10)

    async def test_compose_substack(self):
        d = load_fixture("requests/compose_substack")
        g = ServerGraph.from_dict(d["dag"])
        res = await g.run(req=mock_req("2023-12-12"))
        outputs = res.to_dict()
        self.assertEqual(len(outputs["embed"]), 5)
        self.assertEqual(len(outputs["summary"]["completions"]), 5)

    async def test_compose_substack_http(self):
        # NB: environment variables for this test are set in CI
        # If you want this to run locally, it might be useful to set them in something like
        # `~/.substraterc` and in add something like `source  "${HOME}/.substraterc"` to your bash/zsh/foo rc file
        d = load_fixture("requests/compose_substack")
        url = f"https://substratelabs-{E2E.modal_env}--compose-api.modal.run"
        headers = {
            "x-proxy-path": "/compose",
            "x-substrate-version": "2023-12-12",
            "x-user-id": os.environ.get("SUBSTRATE_API_USER_ID"),
            "x-modal-secret": os.environ.get("MODAL_API_SECRET"),
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.environ.get('SUBSTRATE_API_TOKEN_CI')}",
        }
        response = requests.request("POST", url, headers=headers, data=json.dumps(d))
        outputs = response.json()["data"]
        self.assertEqual(len(outputs["embed"]), 5)
        self.assertEqual(len(outputs["summary"]["completions"]), 5)


if __name__ == "__main__":
    unittest.main()
