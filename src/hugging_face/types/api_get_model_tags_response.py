# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["APIGetModelTagsResponse", "APIGetModelTagsResponseItem"]


class APIGetModelTagsResponseItem(BaseModel):
    id: str

    label: str

    type: Literal["pipeline_tag", "library", "dataset", "language", "license", "arxiv", "doi", "region", "other"]

    sub_type: Optional[str] = FieldInfo(alias="subType", default=None)


APIGetModelTagsResponse: TypeAlias = Dict[str, List[APIGetModelTagsResponseItem]]
