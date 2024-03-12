from typing import Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class SuccessResponse(BaseModel, Generic[T]):
    data: T


class ErrorResponse(BaseModel):
    error: str


# example usage of Response in success case:
# def foo() -> Response[MyType]:
#     return SuccessResponse(data=MyType())
#     return ErrorResponse(error="something went wrong")
ResponseType = TypeVar("ResponseType", SuccessResponse, ErrorResponse)
