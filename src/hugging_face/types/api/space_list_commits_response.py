# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = [
    "SpaceListCommitsResponse",
    "SpaceListCommitsResponseItem",
    "SpaceListCommitsResponseItemAuthor",
    "SpaceListCommitsResponseItemFormatted",
]


class SpaceListCommitsResponseItemAuthor(BaseModel):
    user: str

    avatar: Optional[str] = None


class SpaceListCommitsResponseItemFormatted(BaseModel):
    title: str

    message: Optional[str] = None


class SpaceListCommitsResponseItem(BaseModel):
    id: str

    authors: List[SpaceListCommitsResponseItemAuthor]

    date: datetime

    message: str

    title: str

    formatted: Optional[SpaceListCommitsResponseItemFormatted] = None
    """Available if expand includes formatted"""


SpaceListCommitsResponse: TypeAlias = List[SpaceListCommitsResponseItem]
