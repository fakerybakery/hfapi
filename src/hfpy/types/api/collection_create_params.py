# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CollectionCreateParams", "Item"]


class CollectionCreateParams(TypedDict, total=False):
    namespace: Required[str]

    title: Required[str]

    description: str

    item: Item

    private: bool
    """If not provided, the collection will be public.

    This field will respect the organization's visibility setting.
    """


class Item(TypedDict, total=False):
    id: Required[str]

    type: Required[Literal["paper", "collection", "space", "model", "dataset"]]
