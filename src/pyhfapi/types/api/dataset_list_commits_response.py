# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = [
    "DatasetListCommitsResponse",
    "DatasetListCommitsResponseItem",
    "DatasetListCommitsResponseItemAuthor",
    "DatasetListCommitsResponseItemFormatted",
]


class DatasetListCommitsResponseItemAuthor(BaseModel):
    user: str

    avatar: Optional[str] = None


class DatasetListCommitsResponseItemFormatted(BaseModel):
    title: str

    message: Optional[str] = None


class DatasetListCommitsResponseItem(BaseModel):
    id: str

    authors: List[DatasetListCommitsResponseItemAuthor]

    date: datetime

    message: str

    title: str

    formatted: Optional[DatasetListCommitsResponseItemFormatted] = None
    """Available if expand includes formatted"""


DatasetListCommitsResponse: TypeAlias = List[DatasetListCommitsResponseItem]
