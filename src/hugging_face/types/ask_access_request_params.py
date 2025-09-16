# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["AskAccessRequestParams"]


class AskAccessRequestParams(TypedDict, total=False):
    namespace: Required[str]

    body: Dict[str, object]
