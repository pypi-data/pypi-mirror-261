import re
from typing import List

from modal import Cls, Stub, Image, Secret, asgi_app
from fastapi import Depends, FastAPI, HTTPException
from psycopg2 import Error

from sb_models.vec_db import Model, DimsByTable, TableTypeMap, DistanceMetricMap
from sb_models.network import api_req
from sb_models.types.request import SubstrateRequest
from sb_models.vec_db_client import (
    get_vectors,
    delete_vectors,
    update_vectors,
    get_vector_stores,
    query_vector_store,
    delete_vector_store,
    create_vector_store_with_index,
    get_vector_store_from_table_name,
)
from sb_models.substratecore.models import (
    GetVectorsParams,
    VectorStoreParams,
    GetVectorsResponse,
    DeleteVectorsParams,
    UpdateVectorsParams,
    QueryVectorStoreParams,
    DeleteVectorStoreParams,
    QueryVectorStoreResponse,
    VectorUpdateCountResponse,
)

### Vector Stores API Routes

vector_stores_web_app = FastAPI()
vectors_web_app = FastAPI()
stub = Stub("vector-stores")


# Collection APIs (/vector-stores/*)
@vector_stores_web_app.post("/create", status_code=200)
async def create_vector_store_api(
    item: VectorStoreParams,
    req: SubstrateRequest = Depends(api_req),  # noqa: B008
) -> VectorStoreParams:
    # Validate that name string contains only dashes, underscores, or alphanumeric characters.
    # Postgres has a table name limit of 63 chars.
    rgx = re.compile(r"^[a-z0-9_-]{1,63}$")
    if not rgx.match(item.name):
        raise HTTPException(
            status_code=400,
            detail="Collection name must be 1-24 characters long and contain only dashes, underscores, or alphanumeric characters",
        )

    # Realistically we'll never hit this as the default values will be populated, but it makes the typechecker happy
    if not item.m or not item.ef_construction or not item.metric:
        raise HTTPException(status_code=400, detail="Index parameters must be specified")

    model = TableTypeMap[item.model]
    owner_id = req.organization_id or req.user_id
    if not owner_id:
        raise HTTPException(status_code=400, detail="Must specify either user_id or organization_id")

    table_name = get_table_name(req, item.name, item.model)
    try:
        create_vector_store_with_index(
            table_name, DimsByTable[model], item.m, item.ef_construction, DistanceMetricMap[item.metric]
        )
    except Error as e:
        raise HTTPException(status_code=400, detail=f"{e}") from e

    return item


@vector_stores_web_app.get("/list", status_code=200)
async def get_vector_stores_api(req: SubstrateRequest = Depends(api_req)) -> List[VectorStoreParams]:  # noqa: B008
    owner_id = req.organization_id or req.user_id
    if not owner_id:
        raise HTTPException(status_code=400, detail="Must specify either user_id or organization_id")

    return get_vector_stores(owner_id)


@vector_stores_web_app.post("/delete", status_code=204)
async def delete_vector_store_api(item: DeleteVectorStoreParams, req: SubstrateRequest = Depends(api_req)):  # noqa: B008
    table_name = get_table_name(req, item.name, item.model)
    try:
        delete_vector_store(table_name)
    except Error as e:
        raise HTTPException(status_code=404, detail=f"{e}") from e

    return


@vector_stores_web_app.post("/query")
async def query_vector_stores_api(
    item: QueryVectorStoreParams,
    req: SubstrateRequest = Depends(api_req),  # noqa: B008
) -> QueryVectorStoreResponse:
    if (
        sum(
            [
                item.query_ids is not None,
                item.query_vectors is not None,
                item.query_strings is not None,
                item.query_image_uris is not None,
            ]
        )
        != 1
    ):
        raise HTTPException(
            status_code=400,
            detail="Must specify exactly one of query_ids, query_vectors, or query_strings, or query_image_uris",
        )

    owner_id = req.organization_id or req.user_id
    if not owner_id:
        raise HTTPException(status_code=400, detail="Must specify either user_id or organization_id")

    table_name = get_table_name(req, item.name, item.model)
    vecs = None
    if item.query_ids is not None:
        vecs = [x.vector for x in get_vectors(table_name, item.query_ids)]
    elif item.query_vectors is not None:
        vecs = item.query_vectors
    elif item.query_strings is not None:
        vecs = _get_text_embeddings(item.query_strings, item.model, req)
    elif item.query_image_uris is not None:
        if item.model != "clip":
            raise HTTPException(status_code=400, detail="Model not supported for image queries")
        vecs = _get_image_embeddings(item.query_image_uris, item.model, req)
    else:
        raise HTTPException(
            status_code=400,
            detail="Must specify exactly one of query_ids, query_vectors, or query_strings, or query_image_uris",
        )

    vector_store = get_vector_store_from_table_name(table_name, owner_id)

    results = query_vector_store(
        table_name,
        vector_store,
        vecs,
        item.top_k or 10,
        item.ef_search or 40,
        item.include_values or False,
        item.include_metadata or False,
        item.filters,
    )

    return QueryVectorStoreResponse(results=results, name=item.name, model=item.model, metric=vector_store.metric)


def _get_text_embeddings(s: List[str], model: Model, req: SubstrateRequest) -> List[List[float]]:
    inputs = [{"text": x} for x in s]
    res = None
    match model:
        case "clip":
            obj = Cls.lookup("clip", "CLIP")()
            res = obj.embed.remote(inputs, req=req)
        case "jina-v2":
            obj = Cls.lookup("jina-base-v2", "Embeddings")()
            res = obj.run_embed.remote(inputs, req=req)
        case _:
            raise HTTPException(status_code=400, detail="Model not supported")

    return [x.vector for x in res.result]


def _get_image_embeddings(s: List[str], model: Model, req: SubstrateRequest) -> List[List[float]]:
    inputs = [{"image_uri": x} for x in s]
    res = None
    match model:
        case "clip":
            obj = Cls.lookup("clip", "CLIP")()
            res = obj.embed.remote(inputs, req=req)
        case "jina-v2":
            raise HTTPException(status_code=400, detail="Jina-V2 does not support image embeddings")
        case _:
            raise HTTPException(status_code=400, detail="Model not supported")

    return [x.vector for x in res.result]


# Vector APIs (/vectors/*)
@vectors_web_app.post("/fetch", status_code=200)
async def get_vectors_api(item: GetVectorsParams, req: SubstrateRequest = Depends(api_req)) -> GetVectorsResponse:  # noqa: B008
    table_name = get_table_name(req, item.name, item.model)
    try:
        return GetVectorsResponse(vectors=get_vectors(table_name, item.ids))
    except Error as e:
        raise HTTPException(status_code=400, detail=f"{e}") from e


@vectors_web_app.post("/update", status_code=200)
async def update_vectors_api(
    item: UpdateVectorsParams,
    req: SubstrateRequest = Depends(api_req),  # noqa: B008
) -> VectorUpdateCountResponse:
    table_name = get_table_name(req, item.name, item.model)
    try:
        return VectorUpdateCountResponse(count=update_vectors(table_name, item.vectors))
    except Error as e:
        raise HTTPException(status_code=400, detail=f"{e}") from e


@vectors_web_app.post("/delete", status_code=200)
async def delete_vectors_api(
    item: DeleteVectorsParams,
    req: SubstrateRequest = Depends(api_req),  # noqa: B008
) -> VectorUpdateCountResponse:
    table_name = get_table_name(req, item.name, item.model)
    try:
        return VectorUpdateCountResponse(count=delete_vectors(table_name, item.ids))
    except Error as e:
        raise HTTPException(status_code=400, detail=f"{e}") from e


### Fast API Server config

web_image = Image.debian_slim(python_version="3.10").pip_install(["psycopg2-binary>=2.7", "sqlalchemy", "pgvector"])


@stub.function(
    secrets=[Secret.from_name("pg-vec-urls", environment_name="main")],
    image=web_image,
)
@asgi_app(label="vector-stores-api")
def fastapi_vector_stores_app():
    return vector_stores_web_app


@stub.function(
    secrets=[Secret.from_name("pg-vec-urls", environment_name="main")],
    image=web_image,
)
@asgi_app(label="vectors-api")
def fastapi_vectors_app():
    return vectors_web_app


def get_table_name(req: SubstrateRequest, name: str, model: Model):
    owner_id = req.organization_id or req.user_id
    if not owner_id:
        raise HTTPException(status_code=400, detail="Must specify either user_id or organization_id")

    m = TableTypeMap[model]
    sanitized_name = re.sub(r"[^a-zA-Z0-9_]", "", name)
    return f"{owner_id}_{m}.{sanitized_name}".lower()
