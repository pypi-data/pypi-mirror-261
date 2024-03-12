import os
import hmac
import json
import time
import base64
import hashlib
import urllib.request
from typing import Any, Union, Optional, NamedTuple
from pathlib import Path
from urllib.parse import urlparse

from fastapi import Header, Request, HTTPException, status
from pydantic import BaseModel

from sb_models.logger import log
from sb_models.types.request import RequestInfo, SubstrateRequest
from sb_models.substratecore.models import ErrorOut


class DownloadResult(NamedTuple):
    data: bytes
    content_type: str


FAKE_UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
FILE_STORE_SERVICE_PROTOCOLS = {"s3"}


def download_file(url: str, req: Optional[SubstrateRequest] = None) -> DownloadResult:
    import re
    import base64

    if is_fs_uri(url):
        if not req or (not req.user_id and not req.organization_id):
            raise ValueError("SubstrateRequest object with user_id or organization_id is required for file store URIs")
        resp = resolve_input_uri(url, req.user_id, req.organization_id)
        return DownloadResult(data=resp["Body"].read(), content_type=resp["ContentType"])
    elif len(url) > 500 or url.startswith("data:"):
        data_uri_pattern = re.compile(r"data:(?P<content_type>.+?);base64,(?P<data>.+)")
        match = data_uri_pattern.match(url)
        if match:
            content_type = match.group("content_type")
            base64_data = match.group("data")
            data = base64.b64decode(base64_data)
            return DownloadResult(data=data, content_type=content_type)
        else:
            raise ValueError("Invalid data URI format")
    else:
        request = urllib.request.Request(url, data=None, headers={"User-Agent": FAKE_UA})
        with urllib.request.urlopen(request) as response:
            return DownloadResult(data=response.read(), content_type=response.headers["content-type"])


def pretty_size(num: Union[float, int], suffix: str = "B") -> str:
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, "Yi", suffix)


def save_file(
    url: str,
    destination: Path,
    overwrite: bool = False,
    req: Optional[SubstrateRequest] = None,
) -> int:
    t0 = time.time()
    if destination.exists():
        if overwrite:
            log.info(f"Overwriting file at {destination}")
        else:
            log.info(f"Using cached file at {destination}")
            return destination.stat().st_size

    result = download_file(url=url, req=req)
    size = len(result.data)
    log.info(f"Downloaded {size} bytes from {url} in {time.time() - t0:.2f}s")

    with open(destination, "wb") as f:
        f.write(result.data)
    log.info(f"Stored file at {destination}")
    return size


class AudioFileInfo(BaseModel):
    size_bytes: int
    length_seconds: float


# TODO: make this more generic so it handles all file types
def save_wav(
    url: str,
    destination: Path,
    overwrite: bool = False,
    req: Optional[SubstrateRequest] = None,
) -> AudioFileInfo:
    t0 = time.time()
    should_download = True
    if destination.exists():
        if overwrite:
            log.info(f"Overwriting file at {destination}")
        else:
            log.info(f"Using cached file at {destination}")
            should_download = False

    size = 0
    if should_download:
        result = download_file(url=url, req=req)
        size = len(result.data)
        log.info(f"Downloaded {size} bytes from {url} in {time.time() - t0:.2f}s")
        with open(destination, "wb") as f:
            f.write(result.data)
        log.info(f"Stored file at {destination}")

    sec = get_wav_seconds_at_path(destination)
    return AudioFileInfo(size_bytes=size, length_seconds=sec)


def get_wav_seconds_at_path(destination: Path) -> float:
    length_in_seconds = 0
    with open(destination, "rb") as file:
        length_in_seconds = get_wav_seconds(file)
    return length_in_seconds


# TODO: maybe use ffmpeg.probe to make this more generic across file types
def get_wav_seconds(file: Any) -> float:
    import wave

    with wave.open(file, "rb") as wav_file:
        frames = wav_file.getnframes()
        rate = wav_file.getframerate()
        length_in_seconds = frames / float(rate)
        return length_in_seconds


def sign_webhook(secret_key: str, message: dict) -> str:
    """
    We sign the post body in python with the secret key so that we can trust that we sent the message
    back to the webhook. In order to verify the signature, we need to replicate the process in javascript
    with the same secret. NB since we are signing the whole body object, we need a standard stringification
    method. Here we choose the most compact version, without key or item separators.

    """
    return hmac.new(
        secret_key.encode(),
        json.dumps(message, separators=(",", ":")).encode(),
        hashlib.sha256,
    ).hexdigest()


# todo
DEV_CALLBACK_PREFIX = "http://"


def notify_callback(callback_url: str, body: dict) -> None:
    import requests

    if not callback_url.startswith(DEV_CALLBACK_PREFIX):
        signature = sign_webhook(os.environ["API_SECRET_KEY"], body)
        try:
            res = requests.post(callback_url, headers={"x-substrate-sig": signature}, json=body)
            if res.status_code == 200:
                log.info(f"Notified webhook @ {callback_url}")
            else:
                log.error(f"Failed to notify webhook @ {callback_url}: {res.status_code} {res.text}")
        except Exception as e:
            log.exception(f"Failed to notify webhook @ {callback_url}: {e}")
    else:
        log.info(f"Skipping dev webhook @ {callback_url}")


def upload_bytes(
    bytes: bytes,
    uri: str,
    user_id: Optional[str] = None,
    organization_id: Optional[str] = None,
) -> None:
    import requests

    if is_fs_uri(uri):
        resolve_output_uri(uri, bytes, user_id, organization_id)
    else:
        requests.put(uri, data=bytes)
    return


async def async_load_image(img_url: str, req: Union[SubstrateRequest, None]) -> "PIL.Image.Image":
    import io
    from io import BytesIO

    import aiohttp
    from PIL import Image

    # try:
    #     from modal import Function
    # except ModuleNotFoundError:
    #     os.environ["USE_MODAL"] = "0"

    if len(img_url) > 500 or img_url.startswith("data:image/"):
        import re
        import base64

        # remove data prefix if present
        # TODO: factor this out, duped below
        match = re.match(r"data:image/(?P<type>[a-zA-Z]+);base64,", img_url)
        if match:
            image = img_url[match.end() :]

        return Image.open(BytesIO(base64.b64decode(image)))
    else:
        if is_fs_uri(img_url):
            if not req or (not req.user_id and not req.organization_id):
                raise ValueError(
                    "SubstrateRequest object with user_id or organization_id is required for file store URIs"
                )
            body = resolve_input_uri(img_url, req.user_id, req.organization_id)["Body"]
            return Image.open(body)
        elif os.path.isfile(img_url):
            return Image.open(img_url)
        else:
            async with aiohttp.ClientSession() as session:
                async with session.get(img_url) as response:
                    if response.status == 200:
                        image_data = await response.read()
                        image_stream = io.BytesIO(image_data)
                        return Image.open(image_stream)
                    else:
                        # try one more time:
                        async with session.get(img_url) as r2:
                            if r2.status == 200:
                                image_data = await r2.read()
                                image_stream = io.BytesIO(image_data)
                                # if USE_MODAL():
                                #     dd = Function.lookup("datadog", "log_event")
                                #     dd.spawn(
                                #         message="IMAGE_RETRY_SUCCESS",
                                #         name="async_load_image",
                                #         attributes={"url": img_url},
                                #     )
                                return Image.open(image_stream)
                            else:
                                raise Exception(f"Failed to download image: {img_url}")


def load_image(
    image: Union[str, "PIL.Image.Image"],
    req: Optional[SubstrateRequest] = None,
) -> "PIL.Image.Image":
    from io import BytesIO

    import requests
    from PIL import Image, ImageOps

    """
    Loads `image` to a PIL Image.

    Args:
        image (`str` or `PIL.Image.Image`):
            The image URI to convert to the PIL Image format.
    Returns:
        `PIL.Image.Image`:
            A PIL Image.
    """
    if isinstance(image, str):
        scheme = urlparse(image).scheme
        if scheme == "http" or scheme == "https":
            image = Image.open(requests.get(image, stream=True).raw)
        elif is_fs_uri(image):
            if not req or (not req.user_id and not req.organization_id):
                raise ValueError(
                    "SubstrateRequest object with user_id or organization_id is required for file store URIs"
                )
            body = resolve_input_uri(image, req.user_id, req.organization_id)["Body"]
            image = Image.open(body)
        elif os.path.isfile(image):
            image = Image.open(image)
        elif len(image) > 500 or image.startswith("data:image/"):
            import re
            import base64

            # remove data prefix if present
            match = re.match(r"data:image/(?P<type>[a-zA-Z]+);base64,", image)
            if match:
                image = image[match.end() :]

            image = Image.open(BytesIO(base64.b64decode(image)))
        else:
            raise ValueError(
                f"Incorrect path or url, URLs must start with `http://` or `https://`, and {image} is not a valid path"
            )
    elif isinstance(image, Image.Image):
        image = image
    else:
        raise ValueError(
            "Incorrect format used for image. Should be an url linking to an image, a local path, or a PIL image."
        )
    image = ImageOps.exif_transpose(image)
    image = image.convert("RGB")
    return image


def load_video(uri: str):
    from io import BytesIO

    import imageio
    import requests
    from PIL import Image

    frames = []

    if uri.startswith(("http://", "https://")):
        # If the file_path is a URL
        response = requests.get(uri)
        response.raise_for_status()
        content = BytesIO(response.content)
        vid = imageio.get_reader(content)
        for frame in vid:
            pil_image = Image.fromarray(frame)
            frames.append(pil_image)

    return frames


async def api_req(
    request: Request,
    x_proxy_path: str = Header(None),
    x_organization_id: str = Header(None),
    x_user_id: str = Header(None),
    x_modal_secret: str = Header(None),
) -> SubstrateRequest:
    """
    This is the primary entrypoint for all substrate API endpoints. It validates the request and returns a
    SubstrateRequest object that contains information about the request.

    It can be used as a Depends() in FastAPI endpoints like so:

        ```python
        @app.get("/some/endpoint")
        def my_endpoint(req: SubstrateRequest = Depends(api_req)):
            ...
        ```
    """
    secret = os.environ.get("API_SECRET_KEY")

    error = None
    if secret and x_modal_secret != secret:
        error = ErrorOut(type="api_error", message=f"Unexpected error – missing secret")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=error)
    if not x_user_id and not x_organization_id:
        error = ErrorOut(type="api_error", message=f"Unexpected error – missing user id")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=error)
    if not x_proxy_path:
        error = ErrorOut(type="api_error", message=f"Unexpected error – missing proxy path")
        error = {"error": "Invalid request"}
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    body = None
    if request.method in ["POST", "PUT"]:
        body = await request.json()

    req: RequestInfo = RequestInfo(
        id=request.headers.get("x-request-id"),
        method=request.method,
        path=request.url.path,
        headers=dict(request.headers),
        query=dict(request.query_params),
        body=body,
    )

    sreq = SubstrateRequest(
        request=req,
        proxy_path=x_proxy_path,
        organization_id=x_organization_id,
        user_id=x_user_id,
    )
    if error is not None:
        datadog = Function.lookup("datadog", "log")
        datadog.spawn(error=error, req=sreq)
    return sreq


### File Storage API Resolvers
def resolve_input_uri(uri: str, user_id: Optional[str], organization_id: Optional[str]):
    p = urlparse(uri)
    service, bucket, key = p.scheme, p.netloc, p.path
    key = key.lstrip("/")
    client = get_file_store_client(service, bucket, user_id, organization_id)

    return client.get_object(Bucket=bucket, Key=key)


def resolve_output_uri(uri: str, file, user_id: Optional[str], organization_id: Optional[str]):
    p = urlparse(uri)
    service, bucket, key = p.scheme, p.netloc, p.path
    key = key.lstrip("/")
    client = get_file_store_client(service, bucket, user_id, organization_id)

    return client.put_object(Bucket=bucket, Key=key, Body=file)


def get_file_store_client(service, bucket, user_id, organization_id):
    import boto3

    get_file_storage_config = Function.lookup("substrate-db", "get_file_storage_config")
    svc_data, cred_data = get_file_storage_config.remote(
        service=service, bucket=bucket, user_id=user_id, organization_id=organization_id
    )

    type = cred_data["type"]
    region = svc_data["region"]

    client = None

    if service == "s3":
        if type == "aws_cross_account":
            ext_id = cred_data["externalId"]
            arn = cred_data["arn"]
            sts_client = boto3.client(
                "sts",
                aws_access_key_id=os.environ["AWS_FILE_STORAGE_KEY_ID"],
                aws_secret_access_key=os.environ["AWS_FILE_STORAGE_KEY_SECRET"],
            )
            resp = sts_client.assume_role(
                RoleArn=arn,
                RoleSessionName=f"substrate_{int(time.time())}",
                ExternalId=ext_id,
            )
            assume_creds = resp["Credentials"]
            key_id = assume_creds["AccessKeyId"]
            key_secret = assume_creds["SecretAccessKey"]
            key_token = assume_creds["SessionToken"]

            client = boto3.client(
                "s3",
                aws_access_key_id=key_id,
                aws_secret_access_key=key_secret,
                aws_session_token=key_token,
                region_name=region,
            )
        elif type == "aws_access_key":
            key_id = cred_data["accessKeyId"]
            key_secret = cred_data["secretAccessKey"]
            client = boto3.client(
                "s3",
                aws_access_key_id=key_id,
                aws_secret_access_key=key_secret,
                region_name=region,
            )
    else:
        raise NotImplementedError(f"Could not resolve file storage uri")

    return client


def is_fs_uri(uri):
    return type(uri) == str and urlparse(uri).scheme in FILE_STORE_SERVICE_PROTOCOLS


def is_fs_folder(uri):
    return is_fs_uri(uri) and uri.endswith("/")


def multi_store_jpg_to_uri(
    store: Union[str, bool],
    images: list["PIL.Image.Image"],
    write_path: str,
    model_folder: str,
    req: Optional[SubstrateRequest] = None,
) -> list[str]:
    if len(images) > 1 and is_fs_uri(store) and not is_fs_folder(store):
        raise ValueError(
            f"Invalid file store uri: {store}. You must specify a folder with a trailing slash if storing multiple images."
        )

    uris = list(
        map(
            lambda i: store_jpg_to_uri(store, i, write_path, model_folder, req=req),
            images,
        )
    )

    return uris


def byte_vals_from_image(img: "PIL.Image.Image", file_type: str) -> bytes:
    import io

    image_bytes = io.BytesIO()
    img.save(image_bytes, format=file_type.upper())
    return image_bytes.getvalue()


def store_png_to_uri(
    store: Union[str, bool],
    image: "PIL.Image.Image",
    write_path: str,
    model_folder: str,
    req: Optional[SubstrateRequest] = None,
) -> str:
    bytes = byte_vals_from_image(image, "png")
    return store_file_to_uri(store, bytes, "png", write_path, model_folder, req)


def store_jpg_to_uri(
    store: Union[str, bool],
    image: "PIL.Image.Image",
    write_path: str,
    model_folder: str,
    req: Optional[SubstrateRequest] = None,
) -> str:
    bytes = byte_vals_from_image(image, "jpeg")
    return store_file_to_uri(store, bytes, "jpeg", write_path, model_folder, req)


def store_file_to_uri(
    store: Union[str, bool],
    bytes: bytes,
    file_type: str,
    write_path: str,
    model_folder: str,
    req: Optional[SubstrateRequest] = None,
) -> str:
    uri = None
    if not store:
        uri = base64.b64encode(bytes).decode("utf-8")
        if not req:  # don't add data prefix in local dev
            uri = f"{uri}"
        if req:
            version = req.request.headers.get("x-substrate-version")
            if version and version > "2024-01-01":
                uri = f"data:image/{file_type};base64,{uri}"
    elif isinstance(store, str) and store != "hosted":
        if not req or (not req.user_id and not req.organization_id):
            raise ValueError("SubstrateRequest object with user_id or organization_id is required for file store URIs")

        if is_fs_folder(store):
            store += f"sb_out_{round(time.time())}.{file_type}"
        upload_bytes(bytes, store, req.user_id, req.organization_id)
        uri = store
    else:
        Path(write_path).mkdir(parents=True, exist_ok=True)
        output_path = os.path.join(
            write_path,
            f"{os.urandom(24).hex()}_{round(time.time())}.{file_type}",
        )
        with open(output_path, "wb") as f:
            f.write(bytes)
        file_key = os.path.basename(output_path)
        uri = f"https://assets.substrate.run/{model_folder}/{file_key}"

    return uri


def upload_audio(
    audio: bytes,
    uri: str,
    user_id: Optional[str] = None,
    organization_id: Optional[str] = None,
) -> None:
    import requests

    if is_fs_uri(uri):
        resolve_output_uri(uri, audio, user_id, organization_id)
    else:
        requests.put(uri, data=audio)
    return


# NB: This only handles wavs for now
def handle_store_for_audio(
    store: Union[str, bool],
    audio_b64: bytes,
    write_path: str,
    model_folder: str,
    req: Optional[SubstrateRequest] = None,
) -> str:
    uri = None
    if not store:
        uri = audio_b64.decode("utf-8")
    elif type(store) == str and store != "hosted":
        if not req or (not req.user_id and not req.organization_id):
            raise ValueError("SubstrateRequest object with user_id or organization_id is required for file store URIs")

        if is_fs_folder(store):
            store += f"sb_out_{round(time.time())}.wav"
        upload_audio(audio_b64, store, req.user_id, req.organization_id)
        uri = store
    else:
        Path(write_path).mkdir(parents=True, exist_ok=True)
        output_path = os.path.join(
            write_path,
            f"{os.urandom(24).hex()}_{round(time.time())}.wav",
        )
        with open(output_path, "wb") as f:
            f.write(base64.b64decode(audio_b64))
            name = f.name

        file_key = os.path.basename(output_path)
        uri = f"https://assets.substrate.run/{model_folder}/{file_key}"

    return uri
