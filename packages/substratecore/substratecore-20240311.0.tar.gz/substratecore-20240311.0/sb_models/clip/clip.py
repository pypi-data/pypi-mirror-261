import asyncio
from typing import Any, Dict, List, Optional, TypedDict

from modal import (
    Stub,
    Image,
    Secret,
    Function,
    gpu,
    method,
    asgi_app,
)
from fastapi import Header, FastAPI
from pydantic import parse_obj_as

from sb_models.logger import log
from sb_models.vec_db import VecDB, TableType, IndexMeasure
from sb_models.network import async_load_image
from sb_models.types.inputs import StoreInfo
from sb_models.usage_models import ClipUsage
from sb_models.types.outputs import ClipDoc, InferenceRun, ClipEmbedding
from sb_models.types.request import CLIPQueryArgs, SubstrateRequest

GPU_TYPE = gpu.A10G()


def get_model():
    import open_clip

    model, _, preprocess = open_clip.create_model_and_transforms(
        "ViT-L-14", pretrained="datacomp_xl_s13b_b90k", device="cuda"
    )
    import torch

    inputs = open_clip.tokenizer.tokenize(["hello", "substrate"]).to("cuda")
    with torch.no_grad():
        model.encode_text(inputs)
    return model, preprocess


image = (
    Image.debian_slim(python_version="3.11")
    .pip_install(["open_clip_torch"])
    .run_function(get_model, gpu="any")
    .pip_install("smart_open")
    .apt_install("git")
    .pip_install("git+https://github.com/SubstrateLabs/vecs.git@a6da61d")
    .pip_install("boto3==1.34.47")
    .pip_install("requests==2.28.1")
)

stub = Stub("clip", image=image)


TABLE_TYPE: TableType = "clip_docs"


class SimilarityResult(TypedDict):
    id: str
    metadata: dict


def text_from_doc(doc: ClipDoc):
    text = ""
    if doc.text and doc.metadata and doc.embed_metadata_keys:
        for key in doc.embed_metadata_keys:
            if doc.metadata.get(key):
                text += f"{key}: {doc.metadata[key]}\n"
    if doc.text:
        text += "\n"
        text += doc.text
    return text


@stub.cls(
    gpu=GPU_TYPE,
    concurrency_limit=10,
    timeout=60 * 2,
    container_idle_timeout=60 * 1,
    secrets=[
        Secret.from_name("pg-vec-urls", environment_name="main"),
        Secret.from_name("aws-file-storage-key", environment_name="main"),
    ],
)
class CLIP(VecDB):
    def __enter__(self):
        super().__enter__()

        self.model, self.preprocess = get_model()

    @method()
    async def embed(
        self,
        docs: List[Dict[str, Any]],
        store: Optional[str] = None,
        req: Optional[SubstrateRequest] = None,
    ) -> InferenceRun[List[ClipEmbedding], ClipUsage]:
        import time
        import uuid

        import numpy as np
        import torch
        from open_clip import tokenizer

        t0 = time.time()
        clip_docs = list(map(lambda x: parse_obj_as(ClipDoc, x), docs))
        first_doc = clip_docs[0]
        # we can assume that the docs are all-text or all-image
        # we validate this in clip_versions.py
        is_text = first_doc.text
        texts = []
        image_uris = []

        input_image_count = 0
        input_image_bytes = 0
        input_text_count = 0
        input_token_count = 0
        if is_text:
            texts = [text_from_doc(d) for d in clip_docs]
            input_text_count = len(texts)

            inputs = tokenizer.tokenize(texts).to("cuda")
            input_token_count = len(inputs)
            with torch.no_grad():
                outputs = self.model.encode_text(inputs).tolist()
        else:
            image_uris = [d.image_uri for d in clip_docs]
            images = await asyncio.gather(*[async_load_image(uri, req) for uri in image_uris])
            input_image_count = len(images)

            for im in images:
                input_image_bytes += len(im.tobytes())
            images = [self.preprocess(im) for im in images if im is not None]
            with torch.no_grad():
                image_input = torch.tensor(np.stack(images)).to("cuda")
                outputs = self.model.encode_image(image_input).tolist()
            pass

        ids = [d.id if d.id else str(uuid.uuid4()) for d in clip_docs]
        results = [
            (id, e, {"doc_id": id, "doc": d}) for id, e, d in zip(ids, outputs, texts if is_text else image_uris)
        ]
        if store and req:
            self.write_emb(
                TABLE_TYPE,
                req.user_id,
                req.organization_id,
                collection=store,
                params=results,
            )
        embs = [ClipEmbedding(id=id, vector=e, metadata=m) for id, e, m in results]

        execution_s = time.time() - t0
        log.info(f"Generated {len(embs)} embeddings in {execution_s:.2f}s")

        usage = ClipUsage(
            execution_seconds=execution_s,
            machine_config=str(GPU_TYPE),
            input_image_count=input_image_count,
            input_image_bytes=input_image_bytes,
            input_text_count=input_text_count,
            input_token_count=input_token_count,
            output_embedding_count=0,
        )
        return InferenceRun(
            result=embs,
            usage=usage,
        )

    @method()
    def similarity(
        self,
        texts: list[str],
        image_uris: list[str],
        limit: int = 10,
        store: Optional[StoreInfo] = None,
        measure=IndexMeasure.max_inner_product,
        returning=None,
        ef_search: Optional[int] = None,
    ) -> list[list[SimilarityResult]]:
        from multiprocessing import Pool

        import numpy as np
        import torch
        import open_clip

        if not texts and not image_uris:
            return []

        if texts:
            inputs = open_clip.tokenizer.tokenize(texts).to("cuda")
            with torch.no_grad():
                embs = self.model.encode_text(inputs).tolist()
        else:
            with Pool(20) as p:
                images = p.map(load_image, image_uris)
                images = [self.preprocess(im) for im in images if im is not None]
            with torch.no_grad():
                image_input = torch.tensor(np.stack(images)).to("cuda")
                embs = self.model.encode_image(image_input).tolist()

        result = self.query_batch(  # TODO: fix args
            TABLE_TYPE,
            embs,
            collection=store.collection,
            user_id=store.user_id,
            organization_id=store.organization_id,
            limit=limit,
            measure=measure,
            returning=returning,
            ef_search=ef_search,
        )

        first_res = next((sublist for sublist in result if sublist), None)

        if first_res is None:
            return []

        if isinstance(first_res[0], str):
            ret = [[{"id": _id} for _id in r] for r in result]
        else:
            ret = [[{"id": _id, "metadata": metadata} for (_id, metadata) in r] for r in result]
        return ret


web_app = FastAPI()


class QueryOut(TypedDict):
    id: str
    vec: list[float]
    doc: dict


@web_app.post("/query")
async def query(
    args: CLIPQueryArgs,
    x_proxy_path: str = Header(None),
    x_organization_id: str = Header(None),
    x_user_id: str = Header(None),
    x_modal_secret: str = Header(None),
):
    import os

    if not x_user_id and not x_organization_id:
        return {"error": "Not authorized"}
    if not x_proxy_path:
        return {"error": "Invalid request"}

    secret = os.environ["API_SECRET_KEY"]
    if secret and x_modal_secret != secret:
        return {"error": "Not authorized"}

    if not args.texts and not args.image_uris:
        return {"error": "Invalid request. Must provide texts or image urls to query against"}

    store_info = StoreInfo(  # TODO: fix args
        collection=args.collection,
        user_id=x_user_id,
        organization_id=x_organization_id,
    )
    result = CLIP().similarity.remote(
        args.texts,
        args.image_uris,
        limit=args.limit,
        store=store_info,
        returning=args.returning,
        ef_search=args.ef_search,
    )

    usage = Function.lookup("substrate-usage", "notify_usage")
    usage.spawn(
        user_id=x_user_id,
        organization_id=x_organization_id,
        path=x_proxy_path,
        metadata={
            "returning": args.returning,
            "collection": args.collection,
            "limit": args.limit,
        },
    )
    return {"data": result}


web_image = Image.debian_slim(python_version="3.10")


@stub.function(
    timeout=60 * 10,
    secrets=[Secret.from_name("api-secret-key", environment_name="main")],
    concurrency_limit=64,
    image=web_image,
)
@asgi_app(label="clip-api")
def fastapi_app():
    return web_app
