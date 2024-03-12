import os
import time
from enum import Enum
from typing import Dict, List, Tuple, Union, Literal, Iterable, Optional
from collections import deque

from sb_models.logger import log

TableType = Union[
    Literal["jina_base_v2_docs"],
    Literal["bge_base_1_5_docs"],
    Literal["bge_large_1_5_docs"],
    Literal["flag_docs"],
    Literal["clip_docs"],
]

DimsByTable: Dict[TableType, int] = {
    "flag_docs": 1024,
    "clip_docs": 768,
    "bge_base_1_5_docs": 768,
    "bge_large_1_5_docs": 1024,
    "jina_base_v2_docs": 768,
}

Model = Union[Literal["jina-v2"], Literal["clip"]]

TableTypeMap: Dict[Model, TableType] = {"jina-v2": "jina_base_v2_docs", "clip": "clip_docs"}

DistanceMetricMap: Dict[str, str] = {
    "cosine": "vector_cosine_ops",
    "l2": "vector_l2_ops",
    "inner": "vector_ip_ops",
}


class IndexMeasure(str, Enum):
    cosine_distance = "cosine_distance"
    l2_distance = "l2_distance"
    max_inner_product = "max_inner_product"


def table_name_from(table: TableType, owner_id: str, collection: str):
    import re

    if not table or not owner_id or not collection:
        raise ValueError("table_name and owner_id and collection name must be specified")

    sanitized = re.sub(r"[^a-zA-Z0-9_]", "", f"{table}_{owner_id}_{collection}")
    return sanitized.lower()


VecRow = Tuple[str, Iterable[float], dict]
MAX_CACHE_SIZE = 1000


class VecDB:
    def __enter__(self):
        import vecs

        self.known_collections = deque()
        self.client = vecs.create_client(os.environ["SB_POOLER_URL"])
        self.docs_cache = {}

    def _get_docs(self, table_name, table_type, force=False):
        import vecs

        if force:
            t0 = time.time()
            self.docs_cache.pop(table_name, None)
            self.client = vecs.create_client(os.environ["SB_POOLER_URL"])
            log.info(f"Recreated client in {time.time() - t0:.2f}s")

        if table_name in self.docs_cache:
            log.info("Found collection in cache")
            return self.docs_cache[table_name]

        t0 = time.time()
        try:
            docs = self.client.get_or_create_collection(name=table_name, dimension=DimsByTable[table_type])
            log.info(f"Found collection in {time.time() - t0:.2f}s")
        except Exception as e:
            log.error(f"Error getting collection {table_name}: {e}")
            self.client = vecs.create_client(os.environ["SB_POOLER_URL"])
            docs = self.client.get_or_create_collection(name=table_name, dimension=DimsByTable[table_type])
            log.info(f"Found collection with new client in {time.time() - t0:.2f}s")

        if len(self.docs_cache) >= MAX_CACHE_SIZE:
            for k in list(self.docs_cache.keys())[: MAX_CACHE_SIZE // 2]:
                self.docs_cache.pop(k)

        self.docs_cache[table_name] = docs
        return docs

    def upsert(self, records, table_type: TableType, table_name: str):
        import vecs

        try:
            docs = self._get_docs(table_name, table_type)
        except Exception as e:
            log.error(f"Error getting collection {table_name}: {e}")
            docs = self._get_docs(table_name, table_type, force=True)
        self.known_collections.append(table_name)
        if docs.just_created:
            docs.create_index(
                measure=IndexMeasure.max_inner_product,
                method=vecs.IndexMethod.hnsw,
                index_arguments=vecs.IndexArgsHNSW(m=16, ef_construction=64),
            )
        docs.upsert(records=records)

    def write_emb(
        self,
        table_type: TableType,
        user_id,
        organization_id,
        collection,
        params: list[tuple[str, list[float], dict]],
    ):
        import vecs

        if not organization_id and not user_id:
            return

        if organization_id:
            # Can only allow one, and org id always takes precedence if present
            user_id = None

        batch_size = 1024
        table_name = table_name_from(table_type, organization_id or user_id, collection)
        total = 0

        try:
            try:
                docs = self._get_docs(table_name, table_type)
            except Exception as e:
                log.error(f"Error getting collection {table_name}: {e}")
                docs = self._get_docs(table_name, table_type, force=True)
            if docs.just_created:
                docs.create_index(
                    measure=IndexMeasure.max_inner_product,
                    method=vecs.IndexMethod.hnsw,
                    index_arguments=vecs.IndexArgsHNSW(m=16, ef_construction=64),
                )
            ts = time.time()
            for i in range(0, len(params), batch_size):
                batch_params = params[i : i + batch_size]
                total += len(batch_params)
                t0 = time.time()
                try:
                    docs.upsert(records=batch_params)
                    log.info(
                        f"Inserted {len(batch_params)} embeddings ({total} / {len(params)}) in {time.time() - t0:.2f}s"
                    )
                except Exception as e:
                    log.error(f"Error inserting batch: {e}")
        except Exception as e:
            log.error(f"Error writing emb: {e}")
        log.info(f"Inserted {total} total embeddings in {time.time() - ts:.2f}s")

    def query(
        self,
        table_type: TableType,
        embedding: list[float],
        collection,
        user_id=None,
        organization_id=None,
        limit=10,
        returning=None,
        measure: IndexMeasure = IndexMeasure.max_inner_product,
        ef_search: Optional[int] = None,
    ) -> Union[List[VecRow], List[str]]:
        if returning is None:
            returning = []

        owner_id = organization_id or user_id
        table_name = table_name_from(table_type, owner_id, collection)
        try:
            docs = self._get_docs(table_name, table_type)
        except Exception as e:
            log.error(f"Error getting collection {table_name}: {e}")
            docs = self._get_docs(table_name, table_type, force=True)
        t0 = time.time()
        res = docs.query(
            embedding,
            limit=limit,
            measure=measure,
            include_metadata="metadata" in returning,
            ef_search=ef_search,
        )
        log.info(f"Queried embedding {limit}-nn in {time.time() - t0:.2f}s")
        return res

    def query_batch(
        self,
        table_type: TableType,
        embeddings: list[list[float]],
        collection,
        user_id=None,
        organization_id=None,
        limit=10,
        returning=None,
        measure: IndexMeasure = IndexMeasure.max_inner_product,
        ef_search: Optional[int] = None,
        filters: Optional[dict] = None,
    ) -> List[Union[List[VecRow], List[str]]]:
        if returning is None:
            returning = []

        if measure is None:
            measure = IndexMeasure.max_inner_product

        owner_id = organization_id or user_id
        table_name = table_name_from(table_type, owner_id, collection)
        try:
            docs = self._get_docs(table_name, table_type)
        except Exception as e:
            log.error(f"Error getting collection {table_name}: {e}")
            docs = self._get_docs(table_name, table_type, force=True)
        res = []
        i = 0
        for emb in embeddings:
            i += 1
            tx = time.time()
            r = docs.query(
                emb,
                limit=limit,
                measure=measure,
                include_metadata="metadata" in returning,
                ef_search=ef_search,
                include_value=True,
                filters=filters,
            )
            log.info(f"Queried embedding {limit}-nn in {time.time() - tx:.2f}s ({i} / {len(embeddings)})")
            res.append(r)
        return res
