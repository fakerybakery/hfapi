# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SettingUpdateWatchParams", "Add", "Delete"]


class SettingUpdateWatchParams(TypedDict, total=False):
    add: Iterable[Add]

    delete: Iterable[Delete]


class Add(TypedDict, total=False):
    id: Required[str]

    type: Required[Literal["org", "user", "repo"]]


class Delete(TypedDict, total=False):
    id: Required[str]

    type: Required[Literal["org", "user", "repo"]]
