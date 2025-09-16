# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["DatasetRequestAccessParams"]


class DatasetRequestAccessParams(TypedDict, total=False):
    namespace: Required[str]

    body: Dict[str, object]
