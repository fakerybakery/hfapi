# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SpaceGetNotebookURLResponse", "Error", "NotInCache", "URL"]


class Error(BaseModel):
    error: str


class NotInCache(BaseModel):
    not_in_cache: Literal[True] = FieldInfo(alias="notInCache")


class URL(BaseModel):
    url: str


SpaceGetNotebookURLResponse: TypeAlias = Union[Error, NotInCache, URL]
