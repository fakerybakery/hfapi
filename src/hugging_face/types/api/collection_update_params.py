# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["CollectionUpdateParams", "Gating", "GatingMode", "GatingUnionMember1", "GatingUnionMember1Notifications"]


class CollectionUpdateParams(TypedDict, total=False):
    namespace: Required[str]

    slug: Required[str]

    description: str

    gating: Gating

    position: int

    private: bool

    theme: Literal["orange", "blue", "green", "purple", "pink", "indigo"]

    title: str


class GatingMode(TypedDict, total=False):
    mode: Required[Literal["auto"]]


class GatingUnionMember1Notifications(TypedDict, total=False):
    mode: Required[Literal["bulk", "real-time"]]

    email: str


class GatingUnionMember1(TypedDict, total=False):
    mode: Required[Literal["manual"]]

    notifications: Required[GatingUnionMember1Notifications]


Gating: TypeAlias = Union[GatingMode, GatingUnionMember1, object]
