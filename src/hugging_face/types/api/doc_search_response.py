# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DocSearchResponse", "DocSearchResponseItem", "DocSearchResponseItem_Vectors"]


class DocSearchResponseItem_Vectors(BaseModel):
    embeddings: List[float]


class DocSearchResponseItem(BaseModel):
    id: str

    api_vectors: DocSearchResponseItem_Vectors = FieldInfo(alias="_vectors")

    heading1: str

    product: str

    source_page_title: str

    source_page_url: str

    text: str

    heading2: Optional[str] = None

    heading3: Optional[str] = None

    heading4: Optional[str] = None

    heading5: Optional[str] = None


DocSearchResponse: TypeAlias = List[DocSearchResponseItem]
