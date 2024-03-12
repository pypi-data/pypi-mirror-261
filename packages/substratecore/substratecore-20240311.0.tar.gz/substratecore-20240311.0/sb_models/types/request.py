from typing import Any, Dict, List, Literal, Optional

from pydantic import BaseModel

# Private request types


class RequestInfo(BaseModel):
    id: Optional[str] = None
    method: str
    path: str
    headers: Dict[str, str]
    query: Dict[str, str]
    body: Optional[Dict[str, Any]] = None


class SubstrateRequest(BaseModel):
    request: RequestInfo
    proxy_path: str
    graph_id: Optional[str] = None
    organization_id: Optional[str] = None
    user_id: Optional[str] = None


class EmbeddingArgs(BaseModel):
    texts: List[str]
    embed_metadata_keys: Optional[List[str]] = None
    collection: Optional[str]
    metadatas: Optional[List[Dict]]
    ids: Optional[List[str]]
    split: Optional[bool] = False


class TextGenerationArgs(BaseModel):
    prompt: Optional[str] = None
    n: Optional[int] = 1
    prompts: Optional[List[str]] = None
    system: Optional[str] = ""
    temperature: Optional[float] = 0.8
    presence_penalty: Optional[float] = 1.0
    frequency_penalty: Optional[float] = 0.3
    repetition_penalty: Optional[float] = 1.0
    top_p: Optional[float] = 1.0
    max_tokens: Optional[int] = None


class TranscriptionArgs(BaseModel):
    audio_url: str
    prompt: Optional[str] = None
    align: Optional[bool] = False
    diarize: Optional[bool] = False
    language: Optional[str] = "en"


class QueryArgs(BaseModel):
    texts: Optional[list[str]]
    vecs: Optional[list[list[float]]]

    collection: str
    limit: Optional[int] = 10
    ef_search: Optional[int] = None
    returning: Optional[list[str]] = None
    measure: Optional[str] = None
    filters: Optional[Dict] = None


class CLIPQueryArgs(BaseModel):
    texts: Optional[list[str]]
    image_uris: Optional[list[str]]
    collection: str
    limit: Optional[int] = 10
    ef_search: Optional[int] = None
    returning: Optional[list[str]] = None


class ComposeArgs(BaseModel):
    dag: dict


class BakllavaArgs(BaseModel):
    prompt: str
    image_url: str
    history: Optional[List[dict]] = None


LanguageCode = Literal[
    "arb",
    "ben",
    "cat",
    "ces",
    "cmn",
    "cym",
    "dan",
    "deu",
    "eng",
    "est",
    "fin",
    "fra",
    "hin",
    "ind",
    "ita",
    "jpn",
    "kan",
    "kor",
    "mlt",
    "nld",
    "pes",
    "pol",
    "por",
    "ron",
    "rus",
    "slk",
    "spa",
    "swe",
    "swh",
    "tam",
    "tel",
    "tgl",
    "tha",
    "tur",
    "ukr",
    "urd",
    "uzn",
    "vie",
]


class SeamlessArgs(BaseModel):
    # either base64 encoded wav or url to wav
    input_audio: str
    target_language_code: LanguageCode
    source_language_code: Optional[LanguageCode] = "eng"

    use_hosted_url: Optional[bool] = False
