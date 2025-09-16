# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["EmbedUpdateResponse", "View"]


class View(BaseModel):
    display_name: str = FieldInfo(alias="displayName")

    key: str

    view_name: str = FieldInfo(alias="viewName")


class EmbedUpdateResponse(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    created_at: datetime = FieldInfo(alias="createdAt")

    repo_id: str = FieldInfo(alias="repoId")

    slug: str

    sql: str

    title: str

    user_id: str = FieldInfo(alias="userId")

    views: List[View]

    justification: Optional[str] = None

    private: Optional[bool] = None

    rating: Optional[float] = None
