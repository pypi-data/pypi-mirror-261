import os
import json

import modal

image = modal.Image.debian_slim().pip_install("psycopg2-binary")
stub = modal.Stub("substrate-db", image=image)


def get_connection():
    import psycopg2

    connection_string = os.environ["PG_DB_URL"]
    conn = psycopg2.connect(connection_string)
    return conn


@stub.function(secret=modal.Secret.from_name("postgres-url", environment_name="main"))
def get_spend_limit(user_id, organization_id):
    conn = get_connection()
    cur = conn.cursor()
    user_query = f"""
        SELECT enabled, amount FROM spend_limits
        WHERE user_id = '{user_id}'
    """
    org_query = f"""
        SELECT enabled, amount FROM spend_limits
        WHERE organization_id = '{organization_id}';
    """
    query = user_query if user_id else org_query
    cur.execute(query)
    res = cur.fetchone()
    cur.close()
    conn.close()
    return res


@stub.function(
    secrets=[
        modal.Secret.from_name("postgres-url", environment_name="main"),
        modal.Secret.from_name("postgres-pgp-key", environment_name="main"),
    ]
)
def get_file_storage_config(bucket, service, user_id, organization_id):
    conn = get_connection()
    cur = conn.cursor()
    user_query = f"""
        SELECT service_metadata, PGP_SYM_DECRYPT(credential_data, '{os.environ["PG_PGP_KEY"]}')::text 
        FROM file_stores fs JOIN file_store_credentials fsc ON fs.credential_id = fsc.id
        WHERE fs.user_id = '{user_id}' AND fsc.user_id = '{user_id}' AND bucket = '{bucket}' AND service = '{service}'
        LIMIT 1
    """
    org_query = f"""
        SELECT service_metadata, PGP_SYM_DECRYPT(credential_data, '{os.environ["PG_PGP_KEY"]}')::text 
        FROM file_stores fs JOIN file_store_credentials fsc ON fs.credential_id = fsc.id
        WHERE fs.organization_id = '{organization_id}' AND fsc.organization_id = '{organization_id}' AND bucket = '{bucket}' AND service = '{service}'
        LIMIT 1
    """
    query = user_query if user_id else org_query
    cur.execute(query)
    res = cur.fetchone()
    cur.close()
    conn.close()

    return json.loads(res[0]), json.loads(res[1])
