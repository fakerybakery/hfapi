# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ModelListCommitsParams"]


class ModelListCommitsParams(TypedDict, total=False):
    namespace: Required[str]

    repo: Required[str]

    expand: List[Literal["formatted"]]

    limit: int

    p: int
