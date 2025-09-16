# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ResourceGroupAddResponse"]


class ResourceGroupAddResponse(BaseModel):
    added_by: str = FieldInfo(alias="addedBy")

    name: str

    private: bool

    type: Literal["dataset", "model", "space"]
