import time
from typing import Optional, TypedDict

from modal import (
    Stub,
    Image,
    Secret,
    Function,
    gpu,
    method,
    asgi_app,
)
from fastapi import Header, FastAPI, HTTPException

from sb_models.logger import log
from sb_models.vec_db import VecDB, TableType, IndexMeasure
from sb_models.types.inputs import StoreInfo
from sb_models.types.outputs import Embedding
from sb_models.types.request import QueryArgs, EmbeddingArgs
from sb_models.types.response import SuccessResponse

GPU_TYPE = gpu.A10G()
MODEL_DIR = "/onnx_model"
max_length = 512


def get_model():
    from optimum.onnxruntime import ORTModelForFeatureExtraction
    from llama_index.embeddings import OptimumEmbedding

    m = ORTModelForFeatureExtraction.from_pretrained(MODEL_DIR, provider="CUDAExecutionProvider")
    return OptimumEmbedding(
        folder_name=MODEL_DIR,
        max_length=max_length,
        model=m,
    )


def load_parser():
    import nltk
    from llama_index import Document
    from llama_index.node_parser import SimpleNodeParser

    t0 = time.time()
    nltk.download("punkt")
    node_parser = SimpleNodeParser.from_defaults(chunk_size=max_length, include_prev_next_rel=True)
    docs = [Document(text=text) for text in ["a", "b"]]
    node_parser.get_nodes_from_documents(docs, show_progress=False)
    log.info(f"loaded parser in {time.time() - t0:.2f}s")


def load_model():
    import subprocess

    t0 = time.time()

    subprocess.run(
        [
            "optimum-cli",
            "export",
            "onnx",
            f"--model={MODEL_ID}",
            f"--task=feature-extraction",
            "--optimize=O4",
            "--device=cuda",
            MODEL_DIR,
        ]
    )
    model = get_model()
    log.info(f"loaded and optimized model in {time.time() - t0:.2f}s")

    load_parser()
    model.get_text_embedding_batch(["a", "b", "c"])
    log.info(f"Warmed up")


# NB: Optimum Runtime only supports CUDA 11.x for now
image = (
    Image.from_registry(
        "nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04",
        add_python="3.10",
    )
    .pip_install("llama_index", "transformers", "optimum[onnxruntime-gpu]")
    .run_function(load_model, timeout=60 * 10, gpu=GPU_TYPE)
    .apt_install("git")
    .pip_install("git+https://github.com/SubstrateLabs/vecs.git@a6da61d")
)

stub = Stub("bge-base-en-v1-5", image=image)
MODEL_ID = "BAAI/bge-base-en-v1.5"
INSTRUCTION = "Represent this sentence for searching relevant passages: "

TABLE_TYPE: TableType = "bge_base_1_5_docs"


class SimilarityResult(TypedDict):
    id: str
    metadata: dict


@stub.cls(
    gpu=GPU_TYPE,
    concurrency_limit=36,
    timeout=60 * 2,
    container_idle_timeout=60 * 1,
    secrets=[Secret.from_name("pg-vec-urls", environment_name="main")],
)
class Embeddings(VecDB):
    def __enter__(self):
        super().__enter__()
        self.model = get_model()

    @method()
    def run_embed(
        self,
        texts: list[str],
        embed_metadata_keys: Optional[list[str]] = None,
        provider_ids: Optional[list[str]] = None,
        split: bool = False,
        store_info: StoreInfo = None,
    ) -> list[list[tuple[str, list[float], dict]]]:
        import uuid

        from llama_index.schema import MetadataMode

        mode = MetadataMode.EMBED
        t0 = time.time()

        from llama_index import Document
        from llama_index.node_parser import SimpleNodeParser

        node_parser = SimpleNodeParser.from_defaults(chunk_size=max_length, include_prev_next_rel=False)
        include_keys = embed_metadata_keys or []
        all_metadata_keys = store_info.full_metadata[0].keys() if store_info and store_info.full_metadata else []
        excluded_embed_metadata_keys = (
            [k for k in store_info.full_metadata[0].keys() if k not in include_keys]
            if store_info and store_info.full_metadata
            else all_metadata_keys
        )

        docs = [
            Document(
                text=text,
                metadata=store_info.full_metadata[idx] if store_info and store_info.full_metadata else {},
                doc_id=str(provider_ids[idx]) if provider_ids else uuid.uuid4().hex,
                excluded_embed_metadata_keys=excluded_embed_metadata_keys,
            )
            for idx, text in enumerate(texts)
        ]

        result: list[list[tuple[str, list[float], dict]]] = []
        if split:
            for d in docs:
                nodes = node_parser.get_nodes_from_documents([d], show_progress=False)
                emb_texts = [n.get_content(mode) for n in nodes]
                base_meta = d.metadata or {}
                metas = [{**base_meta, "doc_id": d.doc_id, "doc": t} for t in emb_texts]
                embeds = self.model.get_text_embedding_batch(emb_texts)
                ids = [f"{d.doc_id}.{i}" for i, n in enumerate(nodes)]
                batch = list(zip(ids, embeds, metas))
                result.append(batch)
        else:
            emb_texts = [d.get_content(mode) for d in docs]
            embeds = self.model.get_text_embedding_batch(emb_texts)
            for i, d in enumerate(docs):
                base_meta = d.metadata or {}
                meta = {**base_meta, "doc_id": d.doc_id, "doc": emb_texts[i]}
                result.append([(str(d.doc_id), embeds[i], meta)])

        total = sum(len(batch) for batch in result)
        log.info(f"Got {total} embeddings in {time.time() - t0:.2f}s")

        if store_info:
            self.write_emb(
                TABLE_TYPE,
                store_info.user_id,
                store_info.organization_id,
                collection=store_info.collection,
                params=[(i, e, m) for batch in result for i, e, m in batch],
            )
        return result

    @method()
    def similarity(
        self,
        texts: list[str],
        limit: int = 10,
        store: StoreInfo = None,
        measure=IndexMeasure.max_inner_product,
        returning=None,
        ef_search: Optional[int] = None,
    ) -> list[list[SimilarityResult]]:
        embs = self.model.get_text_embedding_batch(texts)
        result = self.query_batch(
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


@web_app.post("/")
def api(
    args: EmbeddingArgs,
    x_proxy_path: str = Header(None),
    x_organization_id: str = Header(None),
    x_user_id: str = Header(None),
    x_modal_secret: str = Header(None),
) -> SuccessResponse[Embedding]:
    import os

    secret = os.environ["API_SECRET_KEY"]
    if secret and x_modal_secret != secret:
        raise HTTPException(status_code=401, detail={"error": "Not authorized"})

    if not x_user_id and not x_organization_id:
        raise HTTPException(status_code=401, detail={"error": "Not authorized"})
    if not x_proxy_path:
        raise HTTPException(status_code=400, detail={"error": "Invalid request"})

    if len(args.texts) > 256:
        raise HTTPException(
            status_code=400,
            detail={"error": "Invalid request. Max embedding batch size is 256 documents"},
        )

    if args.collection:
        if not args.ids or len(args.ids) != len(args.texts):
            raise HTTPException(
                status_code=400,
                detail={"error": "Invalid request. If persisting, must provide a list of unique document ids"},
            )
        if len(args.ids) != len(set(args.ids)):
            dupes = set([i for i in args.ids if args.ids.count(i) > 1])
            raise HTTPException(
                status_code=400,
                detail={"error": f"Invalid request. Duplicate ids found: {dupes}"},
            )

    store_info = (
        StoreInfo(
            collection=args.collection,
            user_id=x_user_id,
            organization_id=x_organization_id,
            full_metadata=args.metadatas,
        )
        if args.collection
        else None
    )

    result: list[list[tuple[str, list[float], dict]]] = Embeddings().run_embed.remote(
        args.texts,
        split=args.split,
        embed_metadata_keys=args.embed_metadata_keys,
        store_info=store_info,
        provider_ids=args.ids,
    )

    usage = Function.lookup("substrate-usage", "notify_usage")

    embedding_count = sum(len(batch) for batch in result)

    usage.spawn(
        user_id=x_user_id,
        organization_id=x_organization_id,
        path=x_proxy_path,
        metadata={
            "input_count": len(args.texts),
            "embedding_count": embedding_count,
            "collection": args.collection,
        },
    )
    data = [[Embedding(id=i, vec=e, meta=m) for i, e, m in batch] for batch in result]

    # find any records where id does not start with the doc_id:
    invalid_ids = [
        {"id": i, "vec": e, "doc": m["doc"], "meta": m}
        for batch in result
        for i, e, m in batch
        if not i.startswith(m["doc_id"])
    ]
    if invalid_ids:
        log.error(f"Invalid ids found: {invalid_ids}")
        log.warn(args)
    return SuccessResponse(data=data)


@web_app.post("/query")
async def query(
    args: QueryArgs,
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

    if not args.texts or len(args.texts) == 0:
        return {"error": "Invalid request. Must provide a text to query against"}

    store_info = StoreInfo(
        collection=args.collection,
        user_id=x_user_id,
        organization_id=x_organization_id,
    )
    result = Embeddings().similarity.remote(
        args.texts,
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


web_image = (
    Image.debian_slim(python_version="3.10")
    .pip_install("llama_index", "transformers")
    .run_function(load_parser, timeout=60 * 10)
)


@stub.function(
    timeout=60 * 10,
    secrets=[Secret.from_name("api-secret-key", environment_name="main")],
    concurrency_limit=64,
    image=web_image,
)
@asgi_app(label="bge-base-en-v1-5-api")
def fastapi_app():
    return web_app
