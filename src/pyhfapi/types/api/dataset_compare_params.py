# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DatasetCompareParams"]


class DatasetCompareParams(TypedDict, total=False):
    namespace: Required[str]

    repo: Required[str]

    raw: object
