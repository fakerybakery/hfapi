# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = [
    "ModelListCommitsResponse",
    "ModelListCommitsResponseItem",
    "ModelListCommitsResponseItemAuthor",
    "ModelListCommitsResponseItemFormatted",
]


class ModelListCommitsResponseItemAuthor(BaseModel):
    user: str

    avatar: Optional[str] = None


class ModelListCommitsResponseItemFormatted(BaseModel):
    title: str

    message: Optional[str] = None


class ModelListCommitsResponseItem(BaseModel):
    id: str

    authors: List[ModelListCommitsResponseItemAuthor]

    date: datetime

    message: str

    title: str

    formatted: Optional[ModelListCommitsResponseItemFormatted] = None
    """Available if expand includes formatted"""


ModelListCommitsResponse: TypeAlias = List[ModelListCommitsResponseItem]
