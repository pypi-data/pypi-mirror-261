from typing import Any, Dict, List, Generic, TypeVar, Optional

from pydantic import Extra, BaseModel

RT = TypeVar("RT")
UT = TypeVar("UT")


class InferenceRun(BaseModel, Generic[RT, UT]):
    result: RT
    usage: UT


class InferenceError(BaseModel):
    error_message: str


class EmbeddingMeta(BaseModel):
    """
    EmbeddingMeta is a combination of doc, doc_id which we add and any other user-defined metadata.
    """

    doc_id: str
    doc: str

    class Config:
        extra = Extra.allow


class Embedding(BaseModel):
    id: str
    vec: Optional[List[float]]
    meta: Optional[EmbeddingMeta]


class EmbeddingRow(BaseModel):
    id: str
    vec: List[float]
    doc: Dict


class TextCompletion(BaseModel):
    text: str
    token_count: int


class TextGeneration(BaseModel):
    completions: List[TextCompletion]
    token_count: int
    input_token_count: Optional[int] = None


class AssistantChatCompletion(BaseModel):
    message: str
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class SeamlessOut(BaseModel):
    audio_uri: str
    text: str


class FirellavaItem(BaseModel):
    generated_text: str


class FirellavaOut(BaseModel):
    result: List[FirellavaItem]


class ClipDoc(BaseModel):
    class Config:
        extra = Extra.allow

    text: Optional[str] = None
    """
    Text to embed.
    """
    image_uri: Optional[str] = None
    """
    Image to embed.
    """
    id: Optional[str] = None
    """
    Document id. Required when storing embedding.
    """
    metadata: Optional[Dict[str, Any]] = None
    """
    Additional metadata to store in embedding document.
    """
    embed_metadata_keys: Optional[List[str]] = None
    """
    Contents of `metadata` included to generate embedding.
    """


class ClipEmbedding(BaseModel):
    class Config:
        extra = Extra.allow

    vector: List[float]
    """
    Embedding vector.
    """
    id: Optional[str] = None
    """
    Document id.
    """
    metadata: Optional[Dict[str, Any]] = None
    """
    Additional metadata stored in embedding document.
    """
