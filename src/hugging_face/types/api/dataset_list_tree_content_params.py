# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DatasetListTreeContentParams"]


class DatasetListTreeContentParams(TypedDict, total=False):
    namespace: Required[str]

    repo: Required[str]

    rev: Required[str]

    cursor: str

    expand: object
    """
    If true, returns returns associated commit data for each entry and security
    scanner metadata.
    """

    limit: int
    """1.000 by default, 100 by default for expand=true"""

    recursive: object
    """If true, returns the tree recursively."""
