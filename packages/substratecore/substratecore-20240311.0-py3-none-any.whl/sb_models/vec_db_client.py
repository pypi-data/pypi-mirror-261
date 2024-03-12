import os
import re
import json
from typing import Dict, List, Union

import psycopg2
import psycopg2.extras
from psycopg2.extras import Json, RealDictCursor
from psycopg2.extensions import register_adapter

from sb_models.vec_db import DimsByTable, TableTypeMap, DistanceMetricMap

register_adapter(dict, Json)
from sb_models.substratecore.models import (
    Vector as APIVector,
    VectorStoreParams,
    UpdateVectorParams,
    VectorStoreQueryResult,
)


def _get_connection():
    return psycopg2.connect(os.environ["SB_POOLER_URL"])


def create_vector_store_with_index(table_name: str, dimension: int, m: int, ef_construction: int, metric: str):
    conn = _get_connection()
    with conn.cursor() as cur:
        cur.execute(f"CREATE SCHEMA IF NOT EXISTS {table_name.split('.')[0]}")
        cur.execute(
            f"CREATE TABLE {table_name} (id varchar PRIMARY KEY, vec vector({dimension}) not null, metadata jsonb not null default '{{}}'::jsonb)"
        )
        cur.execute(
            f"CREATE INDEX ON {table_name} USING hnsw (vec {metric}) WITH (m = {m}, ef_construction = {ef_construction})"
        )
        conn.commit()
        cur.close()
        conn.close()

    return


def get_vector_stores(owner_id: str) -> List[VectorStoreParams]:
    conn = _get_connection()

    with conn.cursor() as cur:
        query = f"""
            SELECT table_schema, table_name, indexdef 
                    FROM information_schema.tables t JOIN pg_indexes i ON t.table_schema = i.schemaname and t.table_name = i.tablename 
                    WHERE table_schema LIKE '{owner_id.lower()}%' AND indexname LIKE '%_vec_idx'
            """
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
        conn.close()

        return [_parse_vector_store_params(owner_id, x[0], x[1], x[2]) for x in rows]


def get_vector_store_from_table_name(table_name: str, owner_id: str):
    conn = _get_connection()
    schema, name = table_name.split(".")
    with conn.cursor() as cur:
        query = f"""
            SELECT table_schema, table_name, indexdef 
                FROM information_schema.tables t JOIN pg_indexes i ON t.table_schema = i.schemaname and t.table_name = i.tablename 
                WHERE table_schema LIKE '{schema}' AND indexname LIKE '%_vec_idx' and table_name = '{name}'
            """
        cur.execute(query)
        row = cur.fetchone()
        cur.close()
        conn.close()

        if not row:
            raise ValueError(f"Table {table_name} not found")

        return _parse_vector_store_params(owner_id, row[0], row[1], row[2])


def _parse_vector_store_params(owner_id: str, table_schema: str, table_name: str, index_def: str):
    inv_map = {v: k for k, v in TableTypeMap.items()}
    model = inv_map[remove_prefix(table_schema, f"{owner_id.lower()}_")]

    m = re.search(r"m='(\d+)'", index_def)
    ef_construction = re.search(r"ef_construction='(\d+)'", index_def)
    metric = re.search(r"vec (\w+)", index_def)

    if not m or not ef_construction or not metric:
        raise ValueError("Index parameters not found in index definition")

    inv_metric_map = {v: k for k, v in DistanceMetricMap.items()}
    metric = inv_metric_map[metric.group(1)]

    return VectorStoreParams(
        name=table_name,
        model=model,  # type: ignore
        m=int(m.group(1)),
        ef_construction=int(ef_construction.group(1)),
        metric=metric,  # type: ignore
    )


# Can replace this with str.removeprefix once we can use Python 3.9
def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix) :]
    return text


def delete_vector_store(table_name: str):
    conn = _get_connection()

    with conn.cursor() as cur:
        cur.execute(f"DROP TABLE {table_name}")
        conn.commit()
        cur.close()
        conn.close()

    return


def get_vectors(table_name: str, ids: List[str]):
    conn = _get_connection()

    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(f"SELECT id, vec as vector, metadata FROM {table_name} WHERE id = ANY(%s) LIMIT 100", (ids,))
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return [APIVector(id=x["id"], vector=json.loads(x["vector"]), metadata=x["metadata"]) for x in rows]


def update_vectors(table_name: str, records: List[UpdateVectorParams]):
    conn = _get_connection()

    with conn.cursor() as cur:
        query = f"UPDATE {table_name} AS t SET vec = COALESCE(e.vec::vector, t.vec), metadata = COALESCE(e.metadata::jsonb, t.metadata) FROM (VALUES %s) AS e(id, vec, metadata) WHERE e.id = t.id"
        tuples = [(x.id, x.vector, x.metadata) for x in records]
        psycopg2.extras.execute_values(cur, query, tuples, template=None, page_size=100)
        conn.commit()
        update_count = cur.rowcount
        cur.close()
        conn.close()
        return update_count


def delete_vectors(table_name: str, ids: List[str]):
    conn = _get_connection()

    with conn.cursor() as cur:
        cur.execute(f"DELETE FROM {table_name} WHERE id = ANY(%s)", (ids,))
        conn.commit()
        delete_count = cur.rowcount
        cur.close()
        conn.close()
        return delete_count


def query_vector_store(
    table_name: str,
    vector_store: VectorStoreParams,
    vectors: List[List[float]],
    top_k: int = 10,
    ef_search: int = 40,
    include_values: bool = False,
    include_metadata: bool = False,
    filters: Union[Dict, None] = None,
):
    engine = create_engine(os.environ["SB_POOLER_URL"])
    session = sessionmaker(engine)

    if not vector_store.metric:
        raise ValueError("Invalid distance measure")

    distance_lambda = INDEX_MEASURE_TO_SQLA_ACC.get(vector_store.metric)
    if distance_lambda is None:
        # unreachable
        raise ValueError("invalid distance_measure")  # pragma: no cover

    schema, name = table_name.split(".")
    dimension = DimsByTable[TableTypeMap[vector_store.model]]
    table = Table(
        name,
        MetaData(schema=schema),
        Column("id", String, primary_key=True),
        Column("vec", Vector(dimension), nullable=False),
        Column(
            "metadata",
            postgresql.JSONB,
            server_default=text("'{}'::jsonb"),
            nullable=False,
        ),
        extend_existing=True,
    )

    rows = []
    for v in vectors:
        distance_clause = distance_lambda(table.c.vec)(v)

        cols = [table.c.id, distance_clause]

        if include_values:
            cols.append(table.c.vec)

        if include_metadata:
            cols.append(table.c.metadata)

        stmt = select(*cols)

        if filters:
            stmt = stmt.filter(
                build_filters(table.c.metadata, filters)  # type: ignore
            )

        stmt = stmt.order_by(distance_clause)
        stmt = stmt.limit(top_k)

        with session() as sess:
            with sess.begin():
                sess.execute(text("set local hnsw.ef_search = :ef_search").bindparams(ef_search=ef_search))
                results = sess.execute(stmt).fetchall() or []
                rows.append(
                    [
                        VectorStoreQueryResult(
                            id=x[0],
                            distance=x[1],
                            vector=list(x._mapping["vec"]) if include_values else None,
                            metadata=x._mapping["metadata"] if include_metadata else None,
                        )
                        for x in results
                    ]
                )

    return rows


### Query builder logic from supabase vecs client

from sqlalchemy import Table, Column, String, MetaData, or_, and_, cast, text, select, create_engine
from sqlalchemy.orm import sessionmaker
from pgvector.sqlalchemy import Vector
from sqlalchemy.dialects import postgresql

INDEX_MEASURE_TO_SQLA_ACC = {
    "cosine": lambda x: x.cosine_distance,
    "l2": lambda x: x.l2_distance,
    "inner": lambda x: x.max_inner_product,
}


class FilterError(ValueError):
    pass


class Unreachable(Exception):
    pass


def build_filters(json_col: Column, filters: Dict):
    """
    PRIVATE

    Builds filters for SQL query based on provided dictionary.

    Args:
        json_col (Column): The column in the database table.
        filters (Dict): The dictionary specifying filter conditions.

    Raises:
        FilterError: If filter conditions are not correctly formatted.

    Returns:
        The filter clause for the SQL query.
    """

    if not isinstance(filters, dict):
        raise FilterError("filters must be a dict")

    if len(filters) > 1:
        raise FilterError("max 1 entry per filter")

    for key, value in filters.items():
        if not isinstance(key, str):
            raise FilterError("*filters* keys must be strings")

        if key in ("$and", "$or"):
            if not isinstance(value, list):
                raise FilterError("$and/$or filters must have associated list of conditions")

            if key == "$and":
                return and_(*[build_filters(json_col, subcond) for subcond in value])

            if key == "$or":
                return or_(*[build_filters(json_col, subcond) for subcond in value])

            raise Unreachable()

        if isinstance(value, dict):
            if len(value) > 1:
                raise FilterError("only one operator permitted")
            for operator, clause in value.items():
                if operator not in ("$eq", "$ne", "$lt", "$lte", "$gt", "$gte", "$in"):
                    raise FilterError("unknown operator")

                # equality of singular values can take advantage of the metadata index
                # using containment operator. Containment can not be used to test equality
                # of lists or dicts so we restrict to single values with a __len__ check.
                if operator == "$eq" and not hasattr(clause, "__len__"):
                    contains_value = cast({key: clause}, postgresql.JSONB)
                    return json_col.op("@>")(contains_value)

                if operator == "$in":
                    if not isinstance(clause, list):
                        raise FilterError("argument to $in filter must be a list")

                    for elem in clause:
                        if not isinstance(elem, (int, str, float)):
                            raise FilterError("argument to $in filter must be a list or scalars")

                    # cast the array of scalars to a postgres array of jsonb so we can
                    # directly compare json types in the query
                    contains_value = [cast(elem, postgresql.JSONB) for elem in clause]
                    return json_col.op("->")(key).in_(contains_value)

                matches_value = cast(clause, postgresql.JSONB)

                # handles non-singular values
                if operator == "$eq":
                    return json_col.op("->")(key) == matches_value

                elif operator == "$ne":
                    return json_col.op("->")(key) != matches_value

                elif operator == "$lt":
                    return json_col.op("->")(key) < matches_value

                elif operator == "$lte":
                    return json_col.op("->")(key) <= matches_value

                elif operator == "$gt":
                    return json_col.op("->")(key) > matches_value

                elif operator == "$gte":
                    return json_col.op("->")(key) >= matches_value

                else:
                    raise Unreachable()
