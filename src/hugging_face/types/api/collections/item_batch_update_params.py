# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["ItemBatchUpdateParams", "Body", "BodyData"]


class ItemBatchUpdateParams(TypedDict, total=False):
    namespace: Required[str]

    slug: Required[str]

    body: Iterable[Body]


class BodyData(TypedDict, total=False):
    gallery: SequenceNotStr[str]

    note: str

    position: int


class Body(TypedDict, total=False):
    _id: Required[str]

    action: Required[Literal["update"]]

    data: Required[BodyData]
