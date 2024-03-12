import os
import re
from typing import Any, Dict, Optional

import modal

from sb_models.types.request import SubstrateRequest

image = modal.Image.debian_slim("3.11").pip_install("datadog_api_client==2.21.0", "requests")
stub = modal.Stub("datadog", image=image)


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
        modal.Secret.from_name("datadog-api-key", environment_name="main"),
        modal.Secret.from_name("internal-api-secret", environment_name="main"),
    ],
    keep_warm=1 if os.environ.get("MODAL_ENVIRONMENT", "main") == "main" else None,
)
def log(
    metadata: Optional[Dict[str, Any]] = None,
    error: Optional[Dict[str, Any]] = None,
    req: Optional[SubstrateRequest] = None,
):
    import json

    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.logs_api import LogsApi
    from datadog_api_client.v2.model.http_log import HTTPLog
    from datadog_api_client.v2.model.http_log_item import HTTPLogItem

    if metadata is None:
        metadata = {}

    os.environ["DD_SITE"] = "us5.datadoghq.com"
    configuration = Configuration()
    with ApiClient(configuration) as api_client:
        logs_api = LogsApi(api_client)
        msg_json = {}
        host = "unknown"
        message_suffix = None
        status = ""
        if metadata:
            status = "success"
            msg_json["metadata"] = json.dumps(metadata, indent=2)
            msg_json["evt.outcome"] = status
            msg_json["status"] = status
            status_code = f"{200}"
            msg_json["http.status_code"] = status_code
            status = f"(RES: {status_code})"
        if error:
            status = "error"
            msg_json["error"] = json.dumps(error, indent=2)
            message_suffix = error.get("message", "")
            msg_json["evt.outcome"] = status
            msg_json["status"] = status
            status_code = error.get("type") == "invalid_request_error" and f"{400}" or f"{500}"
            msg_json["http.status_code"] = status_code
            status = f"(RES: {status_code})"
        if req:
            headers = req.request.headers
            user_id = req.organization_id or req.user_id
            msg_json["usr.id"] = user_id
            request_id = headers.get("x-request-id")
            msg_json["http.request_id"] = request_id
            msg_json["http.method"] = req.request.method
            req_path = headers.get("x-proxy-path", "unknown")
            evt_name = f"{req.request.method} {req_path}"
            msg_json["evt.name"] = evt_name
            msg_json["accept"] = headers.get("accept")
            msg_json["x-substrate-version"] = headers.get("x-substrate-version")
            msg_json[
                "message"
            ] = f"{evt_name} {status} – {f'{message_suffix} - ' if message_suffix else ''}reqId:{request_id}{f' usrId:{user_id}' if user_id else ''}"
            host = f"substratelabs--{req_path.split('/')[1]}-api.modal.run"
            body = req.request.body
            if body:
                msg_json["body"] = json.dumps(redact(body), indent=2)
        json_message = json.dumps(msg_json)
        body = HTTPLog(
            value=[
                HTTPLogItem(
                    ddsource="modal",
                    hostname=host,
                    message=json_message,
                    service="sb-models",
                )
            ],
        )
        logs_api.submit_log(body=body)


@stub.function(
    secrets=[
        modal.Secret.from_name("datadog-api-key", environment_name="main"),
        modal.Secret.from_name("internal-api-secret", environment_name="main"),
    ],
    keep_warm=1 if os.environ.get("MODAL_ENVIRONMENT", "main") == "main" else None,
)
def log_event(
    name: str,
    attributes: Dict[str, Any],
    message: Optional[str] = None,
):
    import json

    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.logs_api import LogsApi
    from datadog_api_client.v2.model.http_log import HTTPLog
    from datadog_api_client.v2.model.http_log_item import HTTPLogItem

    if attributes is None:
        attributes = {}

    os.environ["DD_SITE"] = "us5.datadoghq.com"
    configuration = Configuration()
    with ApiClient(configuration) as api_client:
        logs_api = LogsApi(api_client)
        item = {"evt.name": name, **attributes}
        if message:
            item["message"] = message
        body = HTTPLog(
            value=[
                HTTPLogItem(
                    ddsource="modal",
                    message=json.dumps(item),
                    service="sb-models",
                )
            ],
        )
        logs_api.submit_log(body=body)


@stub.function(
    secrets=[
        modal.Secret.from_name("datadog-api-key", environment_name="main"),
        modal.Secret.from_name("internal-api-secret", environment_name="main"),
    ],
    keep_warm=1 if os.environ.get("MODAL_ENVIRONMENT", "main") == "main" else None,
)
def log_metric(name: str, value: float):
    import time

    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.model.point import Point
    from datadog_api_client.v1.model.series import Series
    from datadog_api_client.v1.api.metrics_api import MetricsApi
    from datadog_api_client.v1.model.metrics_payload import MetricsPayload

    os.environ["DD_SITE"] = "us5.datadoghq.com"
    configuration = Configuration()
    with ApiClient(configuration) as api_client:
        metrics_api = MetricsApi(api_client)
        now = int(time.time())
        series = Series(metric=name, type="count", points=[Point([now, value])])
        metrics_api.submit_metrics(body=MetricsPayload(series=[series]))
