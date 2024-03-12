import os
from typing import Dict, List

from modal import Dict as ModalDict, Stub, Image, Secret, web_endpoint
from fastapi import Depends

from sb_models.network import api_req
from sb_models.types.request import ComposeArgs, SubstrateRequest
from sb_models.types.response import SuccessResponse
from sb_models.graph.server_graph import ServerGraph


def pull_dependencies():
    from transformers import AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-v0.1")
    text = "hello world"
    tokenizer(text, max_length=128, truncation=True)


image = (
    Image.debian_slim("3.10")
    .pip_install("networkx==3.2.1", "requests", "transformers==4.37.2", "aiohttp==3.9.3")
    .run_function(pull_dependencies)
)

stub = Stub("compose", image=image)
stub.compose_state = ModalDict.persisted("compose-state")


@stub.function(
    secrets=[
        Secret.from_name("api-secret-key", environment_name="main"),
        Secret.from_name("anyscale-secret", environment_name="main"),
    ],
    image=image,
    keep_warm=2 if os.environ.get("MODAL_ENVIRONMENT", "main") == "main" else None,
    timeout=60 * 20,
    allow_concurrent_inputs=16,
)
@web_endpoint(method="POST")
async def api(args: ComposeArgs, req: SubstrateRequest = Depends(api_req)) -> SuccessResponse[Dict]:  # noqa: B008
    from sb_models.graph.server_graph import ServerGraph

    G = ServerGraph.from_dict(args.dag)
    req.graph_id = G.id
    res = await G.run(req=req, verbose=False)
    outputs = res.to_dict()
    return SuccessResponse(data=outputs)


@stub.local_entrypoint()
async def main():
    from sb_models.logger import log

    prompts = [
        {"prompt": "give me a news story about Nvidia"},
        {"prompt": "give me an uplifting news story about Strawberries"},
        {"prompt": "give me an uplifting news story about Carrots"},
        {"prompt": "give me an news story about Rodger Federer"},
    ]
    from pydantic import BaseModel

    from sb_models.graph.modal_nodes import ModalNode, ModalHandle

    class Item(BaseModel):
        title: str
        short_summary: str
        extended_summary: str

    class Response(BaseModel):
        stories: List[Item]

    # ss_json = '{"title":"ParsingModel[Response]","$ref":"#/definitions/Response","definitions":{"Response":{"title":"Response","type":"object","properties":{"type":{"title":"Type","type":"string"},"expanded_search_term":{"title":"Expanded search term","type":"string"}},"required":["type","expanded_search_term"]}}}'
    ss_json = '{"title":"ParsingModel[Response]","$ref":"#/definitions/Response","definitions":{"Response":{"title":"Response","type":"object","properties":{"title":{"title":"Type","type":"string"},"topics":{"title":"Topics","type":"array","items":{"type":"string"}},"short_summary":{"title":"Short Summary","type":"string"},"extended_summary":{"title":"Extended Summary","type":"string"}},"required":["title","topics","short_summary","extended_summary"]}}}'
    # '{"title":"ParsingModel[Response]","$ref":"#/definitions/Response","definitions":{"Response":{"title":"Response","type":"object","properties":{"title":{"title":"Type","type":"string"},"topics":{"title":"Topics","type":"array","items":{"type":"string"}},"short_summary":{"title":"Short Summary","type":"string"},"extended_summary":{"title":"Extended Summary","type":"string"}},"required":["title","topics","short_summary","extended_summary"]}}}'
    # json_schema = Response.schema_json()
    # json_schema = schema_json_of(Response)

    n = ModalNode(
        ModalHandle.mistral7b_instruct,
        prompts=prompts,
        json_schema=ss_json,
        temperature=0,
        max_tokens=1250,
        frequency_penalty=0.1,
        presence_penalty=1.1,
        repetition_penalty=1.0,
        top_p=0.9,
    )

    # result = await n.run()
    g = ServerGraph()
    g.add_node(n)
    result = await g.run()
    log.info(result)
