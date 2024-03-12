import os
import time
import uuid
from typing import Any, Dict, List, Optional, TypedDict
from pathlib import Path

from modal import (
    Stub,
    Image,
    Secret,
    Function,
    gpu,
    method,
    asgi_app,
)
from fastapi import Depends, FastAPI
from pydantic import parse_obj_as

from sb_models.logger import log
from sb_models.vec_db import VecDB, TableType
from sb_models.network import api_req
from sb_models.types.inputs import StoreInfo
from sb_models.usage_models import JinaUsage
from sb_models.types.outputs import InferenceRun
from sb_models.types.request import QueryArgs, SubstrateRequest

# TODO: replace with new public .models (carefully! in use)
from sb_models.substratecore.deprecated_models import JinaDoc, JinaEmbedding

GPU_TYPE = gpu.A10G()
MODEL_DIR = "/onnx_model"
OPT_MODEL_DIR = "/onnx_model_opt"
max_length = 8080
MODEL_ID = "jinaai/jina-embeddings-v2-base-en"
TABLE_TYPE: TableType = "jina_base_v2_docs"


def download_model():
    from huggingface_hub import snapshot_download

    os.makedirs(MODEL_DIR, exist_ok=True)
    snapshot_download(
        MODEL_ID,
        local_dir=MODEL_DIR,
        ignore_patterns=[
            "pytorch_model.bin",
            "model.safetensors",
            "model-w-mean-pooling.onnx",
        ],
    )


def get_model():
    from optimum.onnxruntime import ORTModelForFeatureExtraction
    from llama_index.embeddings import OptimumEmbedding

    opt_model = ORTModelForFeatureExtraction.from_pretrained(
        Path(OPT_MODEL_DIR),
        provider="CUDAExecutionProvider",
        local_files_only=True,
        file_name="model_optimized.onnx",
        use_io_binding=True,
    )
    assert opt_model.providers == ["CUDAExecutionProvider", "CPUExecutionProvider"]
    return OptimumEmbedding(
        folder_name=OPT_MODEL_DIR,
        max_length=max_length,
        model=opt_model,
        pooling="mean",
        device="cuda",
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


def optimize_model():
    t0 = time.time()
    from optimum.onnxruntime import ORTOptimizer, ORTModelForFeatureExtraction
    from optimum.onnxruntime.configuration import (
        AutoOptimizationConfig,
    )

    optimization_config = AutoOptimizationConfig.O4(for_gpu=True)

    m = ORTModelForFeatureExtraction.from_pretrained(
        Path(MODEL_DIR),
        local_files_only=True,
        provider="CUDAExecutionProvider",
        file_name="model.onnx",
    )
    assert m.providers == ["CUDAExecutionProvider", "CPUExecutionProvider"]
    optimizer = ORTOptimizer.from_pretrained(m)
    optimizer.optimize(save_dir=OPT_MODEL_DIR, optimization_config=optimization_config)

    log.info(f"loaded and optimized model in {time.time() - t0:.2f}s")
    load_parser()
    model = get_model()
    model.get_text_embedding_batch(["a", "b", "c"])
    log.info("Warmed up")


# NB: onnxruntime only supports <= CUDA 11.8 for now
image = (
    Image.from_registry(
        "nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04",
        add_python="3.10",
    )
    .pip_install("hf-transfer==0.1.4", "huggingface_hub")
    .env({"HF_HUB_ENABLE_HF_TRANSFER": "1"})
    .run_function(download_model, timeout=60 * 10)
    .apt_install("git", "libgl1-mesa-glx", "libglib2.0-0")
    .pip_install("git+https://github.com/UKPLab/sentence-transformers.git@c006921")
    .pip_install("llama_index==0.9.19", "optimum[onnxruntime-gpu]")
    .run_function(optimize_model, timeout=60 * 10, gpu=GPU_TYPE)
    .pip_install("git+https://github.com/SubstrateLabs/vecs.git@a6da61d")
)

stub = Stub("jina-base-v2", image=image)


class SimilarityResult(TypedDict):
    id: str
    metadata: dict
    distance: Optional[float]


def _query(
    vec_db,
    embs: list[list[float]],
    store: StoreInfo,
    limit: int,
    measure,
    returning,
    ef_search,
    filters,
    req,
) -> list[list[SimilarityResult]]:
    t1 = time.time()
    result = vec_db.query_batch(
        TABLE_TYPE,
        embs,
        collection=store.collection,
        user_id=req.user_id,
        organization_id=req.organization_id,
        limit=limit,
        measure=measure,
        returning=returning,
        ef_search=ef_search,
        filters=filters,
    )
    log.info(f"Similarity query in {time.time() - t1:.2f}s limit: {limit}")

    first_res = next((sublist for sublist in result if sublist), None)

    if first_res is None:
        return []

    ret_meta = returning and "metadata" in returning
    if isinstance(first_res[0], str):
        ret = [[{"id": _id} for _id in r] for r in result]
    else:
        ret = [
            [
                {
                    "id": row[0],
                    "metadata": {} if not ret_meta else row[2],
                    "distance": row[1],
                }
                for row in r
            ]
            for r in result
        ]

    return ret


@stub.cls(
    gpu=GPU_TYPE,
    concurrency_limit=4,
    timeout=60,
    container_idle_timeout=60 * 2,
    secrets=[Secret.from_name("pg-vec-urls", environment_name="main")],
    _experimental_boost=True,
)
class Embeddings(VecDB):
    def __enter__(self):
        super().__enter__()
        self.model = get_model()
        self.model.get_text_embedding("hello")

    @method(
        keep_warm=1 if os.environ.get("MODAL_ENVIRONMENT", "main") == "main" else None,
    )
    async def run_embed(
        self,
        docs: List[Dict[str, Any]],
        store: Optional[str] = None,
        req: Optional[SubstrateRequest] = None,
    ) -> InferenceRun[List[JinaEmbedding], JinaUsage]:
        from llama_index import Document
        from llama_index.schema import MetadataMode

        mode = MetadataMode.EMBED
        t0 = time.time()

        jina_docs = list(map(lambda x: parse_obj_as(JinaDoc, x), docs))
        li_docs = [
            Document(
                text=doc.text,
                metadata=doc.metadata if doc.metadata else {},
                doc_id=doc.id if doc.id else uuid.uuid4().hex,
                excluded_embed_metadata_keys=[k for k in doc.metadata.keys() if k not in doc.embed_metadata_keys]
                if doc.metadata and doc.embed_metadata_keys
                else [k for k in doc.metadata.keys()]
                if doc.metadata and not doc.embed_metadata_keys
                else [],
            )
            for doc in jina_docs
        ]

        result: list[tuple[str, list[float], dict]] = []
        emb_texts = [d.get_content(mode) for d in li_docs]
        for i, d in enumerate(li_docs):
            try:
                base_meta = d.metadata or {}
                emb = await self.model.aget_text_embedding(emb_texts[i])
                meta = {**base_meta, "doc_id": d.doc_id, "doc": emb_texts[i]}
                result.append((str(d.doc_id), emb, meta))
            except Exception as e:
                log.error(f"Error embedding {d.doc_id}: {e}")

        total = len(result)
        if store and req:
            self.write_emb(
                TABLE_TYPE,
                req.user_id,
                req.organization_id,
                collection=store,
                params=[(i, e, m) for i, e, m in result],
            )
        embs = [JinaEmbedding(id=i, vector=e, metadata=m) for i, e, m in result]

        execution_s = time.time() - t0
        log.info(f"Generated {total} embeddings in {execution_s:.3f}s")

        usage = JinaUsage(
            execution_seconds=execution_s,
            machine_config=str(GPU_TYPE),
            input_doc_count=len(jina_docs),
            output_embedding_count=len(embs),
        )
        return InferenceRun(
            result=embs,
            usage=usage,
        )

    @method(
        keep_warm=1 if os.environ.get("MODAL_ENVIRONMENT", "main") == "main" else None,
    )
    def similarity(
        self,
        texts: list[str],
        limit: int = 10,
        store: StoreInfo = None,
        measure=None,
        returning=None,
        ef_search: Optional[int] = None,
        filters: Optional[Dict] = None,
        req: Optional[SubstrateRequest] = None,
    ) -> list[list[SimilarityResult]]:
        t0 = time.time()
        embs = self.model.get_text_embedding_batch(texts)
        log.info(f"Similarity embeddings ({len(embs)}) in {time.time() - t0:.2f}s")
        return _query(
            self,
            embs,
            store,
            limit,
            measure,
            returning,
            ef_search,
            filters,
            req,
        )


@stub.cls(
    timeout=36,
    container_idle_timeout=60,
    secrets=[Secret.from_name("pg-vec-urls", environment_name="main")],
    allow_concurrent_inputs=12,
    _experimental_boost=True,
)
class QueryNoGPU(VecDB):
    @method(
        keep_warm=1 if os.environ.get("MODAL_ENVIRONMENT", "main") == "main" else None,
    )
    def similarity(
        self,
        embs: list[list[float]],
        limit: int = 10,
        store: StoreInfo = None,
        measure=None,
        returning=None,
        ef_search: Optional[int] = None,
        filters: Optional[Dict] = None,
        req: Optional[SubstrateRequest] = None,
    ) -> list[list[SimilarityResult]]:
        return _query(
            self,
            embs,
            store,
            limit,
            measure,
            returning,
            ef_search,
            filters,
            req,
        )


web_app = FastAPI()


@web_app.post("/query")
async def query(args: QueryArgs, req: SubstrateRequest = Depends(api_req)):  # noqa: B008
    has_text = args.texts and len(args.texts) > 0
    has_vecs = args.vecs and len(args.vecs) > 0
    if not has_text and not has_vecs:
        return {"error": "Invalid request. Must provide a text or vec to query against"}

    t0 = time.time()
    store_info = StoreInfo(collection=args.collection)
    if args.texts:
        result = await Embeddings().similarity.remote.aio(
            args.texts,
            limit=args.limit,
            store=store_info,
            returning=args.returning,
            ef_search=args.ef_search,
            measure=args.measure,
            filters=args.filters,
            req=req,
        )
    elif args.vecs:
        result = await QueryNoGPU().similarity.remote.aio(
            args.vecs,
            limit=args.limit,
            store=store_info,
            returning=args.returning,
            ef_search=args.ef_search,
            measure=args.measure,
            filters=args.filters,
            req=req,
        )
    else:
        return {"error": "Invalid request. Must provide either texts or vecs"}

    log.info(f"Full similarity query in {time.time() - t0:.2f}s")
    t1 = time.time()

    usage = Function.lookup("substrate-usage", "notify_usage")
    usage.spawn(
        user_id=req.user_id,
        organization_id=req.organization_id,
        path=req.proxy_path,
        metadata={
            "returning": args.returning,
            "collection": args.collection,
            "limit": args.limit,
        },
        req=req,
    )
    log.info(f"Usage notification in {time.time() - t1:.2f}s")
    return {"data": result}


web_image = (
    Image.debian_slim(python_version="3.10")
    .pip_install("llama_index", "transformers")
    .run_function(load_parser, timeout=60 * 10)
)


@stub.function(
    timeout=60,
    secrets=[Secret.from_name("api-secret-key", environment_name="main")],
    image=web_image,
    allow_concurrent_inputs=8,
    keep_warm=1 if os.environ.get("MODAL_ENVIRONMENT", "main") == "main" else None,
)
@asgi_app(label="jina-base-v2-api")
def fastapi_app():
    return web_app


@stub.local_entrypoint()
def stats():
    stats = Embeddings().run_embed.get_current_stats()
    log.info(stats)
    t0 = time.time()
    emb = Embeddings().run_embed.remote([{"text": "hello"}])
    log.info(f"Embedding took {time.time() - t0:.2f}s")
    log.info(emb)
