import os
import re
from typing import Optional

import modal
import requests

from sb_models.logger import log
from sb_models.types.request import SubstrateRequest

image = modal.Image.debian_slim("3.11").pip_install("orb-billing==1.29.0", "datadog_api_client==2.19.0", "requests")
stub = modal.Stub("substrate-usage", image=image)
stub.last_checked_usage = modal.Dict.new()


def redact(input_dict):
    long_string = 20
    redacted_url_str = "<redacted_url>"
    redacted_string_str = "<redacted_string>"
    redacted_dict = {}

    for key, value in input_dict.items():
        # skip redaction for specific keys
        if key in ["model", "model_id", "path", "source_key"]:
            redacted_dict[key] = value
            continue
        if isinstance(value, str):
            if (
                len(value) > long_string
                or re.match(r"^https?://", value, re.IGNORECASE)  # urls
                or re.match(r"\S+@\S+", value)  # emails
                or re.match(r"^\d{1,3}(\.\d{1,3}){3}$", value)  # ips
            ):
                redacted_dict[key] = (
                    redacted_url_str if re.match(r"^https?://", value, re.IGNORECASE) else redacted_string_str
                )
            else:
                redacted_dict[key] = value
        elif isinstance(value, dict):
            redacted_dict[key] = redact(value)
        elif isinstance(value, list):
            truncated_list = value[:5]  # truncate lists
            redacted_dict[key] = [
                redact(item)
                if isinstance(item, dict)
                else (
                    redacted_string_str
                    if (
                        isinstance(item, str)
                        and (
                            len(item) > long_string
                            or re.match(r"^https?://", item, re.IGNORECASE)
                            or re.match(r"\S+@\S+", item)
                            or re.match(r"^\d{1,3}(\.\d{1,3}){3}$", item)
                        )
                    )
                    else item
                )
                for item in truncated_list
            ]
        else:
            redacted_dict[key] = value

    return redacted_dict


@stub.function(
    secrets=[
        modal.Secret.from_name("orb-test-key", environment_name="main"),
        modal.Secret.from_name("orb-live-key", environment_name="main"),
        modal.Secret.from_name("datadog-api-key", environment_name="main"),
        modal.Secret.from_name("internal-api-secret", environment_name="main"),
    ],
    keep_warm=1 if os.environ.get("MODAL_ENVIRONMENT", "main") == "main" else None,
)
def notify_usage(
    user_id,
    organization_id,
    path,
    metadata=None,
    req: Optional[SubstrateRequest] = None,
):
    if os.environ.get("MODAL_ENVIRONMENT", "main") != "main":
        log.info("Usage notifications only run in main env. Skipping")
        return
    log.info(f"PATH {path}")
    log.info(f"METADATA {metadata}")
    import time
    import uuid
    from datetime import datetime

    from orb import Orb

    org_or_user_id = organization_id or user_id

    if metadata is None:
        metadata = {}

    idempotency_key = uuid.uuid4().hex
    properties = metadata
    properties.pop("args", None)

    # Orb clients
    test_orb = Orb(api_key=os.environ["ORB_TEST_KEY"])
    live_orb = Orb(api_key=os.environ["ORB_LIVE_KEY"])

    # Ingest Orb events
    event = {
        "external_customer_id": org_or_user_id,
        "event_name": path,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "idempotency_key": idempotency_key,
        "properties": properties,
    }
    res = test_orb.events.ingest(events=[event])
    log.info(f"test_orb.ingest: {res}")
    res = live_orb.events.ingest(events=[event])
    log.info(f"live_orb.ingest: {res}")

    # Report to Datadog
    datadog = modal.Function.lookup("datadog", "log")
    datadog.spawn(
        metadata=metadata,
        req=req,
    )

    # Check Orb usage every 1 minute
    last_checked = None
    try:
        last_checked = stub.last_checked_usage[org_or_user_id]
    except KeyError:
        pass
    now = time.time()
    buffer = 60 * 1
    if last_checked and now - last_checked < buffer:
        log.info(f"already checked orb usage for {org_or_user_id}, checking again in {buffer - (now - last_checked)}s")
        pass
    else:
        log.info(f"checking orb usage")
        stub.last_checked_usage[org_or_user_id] = now
        # NOTE: We only check usage on livemode orb (but send usage events to live and test)
        check_spend(live_orb, user_id, organization_id)
        check_balance(live_orb, user_id, organization_id)
    return


def check_spend(orb_client, user_id, organization_id):
    org_or_user_id = organization_id or user_id
    res = orb_client.subscriptions.list(external_customer_id=org_or_user_id, status="active")
    subs = list(res)
    if len(subs) > 0:
        sub = subs[0]

        # Check spend limit
        get_spend_limit = modal.Function.lookup("substrate-db", "get_spend_limit")
        res = get_spend_limit.remote(user_id=user_id, organization_id=organization_id)
        log.info(f"db.get_spend_limit: {res}")
        if res and res[0]:
            amount = res[1]
            upcoming_invoice = orb_client.invoices.fetch_upcoming(subscription_id=sub.id)
            usage_line_items = [
                m for m in upcoming_invoice.line_items if m.price and m.price.price_type == "usage_price"
            ]
            usage_total = sum([float(m.subtotal) for m in usage_line_items])
            log.info(f"usage_total: {usage_total} spend_limit: {amount}")
            if usage_total > amount:
                url = "https://api.substrate.run/internal/spend_limit_overages"
                headers = {"Authorization": f"Bearer {os.environ['SUBSTRATE_INTERNAL_SECRET']}"}
                res = requests.put(url, headers=headers, params={"key": org_or_user_id})
                log.info(f"PUT internal/spend_limit_overages: {res}")


USAGE_WHITELIST = ["org_TzwLtEOEfQcDYs8t"]


def check_balance(orb_client, user_id, organization_id):
    org_or_user_id = organization_id or user_id

    # TODO(rishabh): Remove this once we migrate Substack to prepaid billing
    if org_or_user_id in USAGE_WHITELIST:
        return

    url = f"https://api.withorb.com/v1/customers/external_customer_id/{org_or_user_id}/credits"

    params = {"limit": "1", "currency": "USD"}
    headers = {"Accept": "application/json", "Authorization": f"Bearer {orb_client.api_key}"}

    response = requests.get(url, headers=headers, params=params).json()
    has_credits = len(response["data"]) > 0
    if not has_credits:
        url = "https://api.substrate.run/internal/usage_limit_overages"
        headers = {"Authorization": f"Bearer {os.environ['SUBSTRATE_INTERNAL_SECRET']}"}
        res = requests.put(url, headers=headers, params={"key": org_or_user_id})
        log.info(f"PUT internal/usage_limit_overages: {res}")


@stub.local_entrypoint()
def run():
    notify_usage = modal.Function.lookup("substrate-usage", "notify_usage")
    notify_usage.spawn(None, "org_JWx9kL06SD7YM1nt", "/sdxl", {"image_count": 100})
