# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["APIGetModelTagsParams"]


class APIGetModelTagsParams(TypedDict, total=False):
    type: Literal["pipeline_tag", "library", "dataset", "language", "license", "arxiv", "doi", "region", "other"]
