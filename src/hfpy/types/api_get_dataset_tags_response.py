# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["APIGetDatasetTagsResponse", "APIGetDatasetTagsResponseItem"]


class APIGetDatasetTagsResponseItem(BaseModel):
    id: str

    label: str

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

    sub_type: Optional[str] = FieldInfo(alias="subType", default=None)


APIGetDatasetTagsResponse: TypeAlias = Dict[str, List[APIGetDatasetTagsResponseItem]]
