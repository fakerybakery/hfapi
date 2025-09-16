# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["APIGetDatasetTagsParams"]


class APIGetDatasetTagsParams(TypedDict, total=False):
    type: Literal[
        "task_categories",
        "size_categories",
        "modality",
        "format",
        "library",
        "language",
        "license",
        "arxiv",
        "doi",
        "region",
        "other",
        "task_ids",
        "annotations_creators",
        "language_creators",
        "multilinguality",
        "source_datasets",
        "benchmark",
    ]
