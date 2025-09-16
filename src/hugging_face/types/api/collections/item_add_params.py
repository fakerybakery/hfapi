# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ItemAddParams", "Item"]


class ItemAddParams(TypedDict, total=False):
    namespace: Required[str]

    slug: Required[str]

    item: Required[Item]

    note: str


class Item(TypedDict, total=False):
    id: Required[str]

    type: Required[Literal["paper", "collection", "space", "model", "dataset"]]
