# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypedDict

from ..._types import SequenceNotStr

__all__ = ["CollectionListParams"]


class CollectionListParams(TypedDict, total=False):
    cursor: str

    expand: object

    item: Union[SequenceNotStr[str], str]

    limit: float

    owner: Union[SequenceNotStr[str], str]

    q: str

    sort: Literal["upvotes", "lastModified", "trending"]
