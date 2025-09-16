# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SettingGetMcpResponse", "SpaceTool"]


class SpaceTool(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    emoji: str

    name: str

    subdomain: str


class SettingGetMcpResponse(BaseModel):
    built_in_tools: List[str] = FieldInfo(alias="builtInTools")

    space_tools: List[SpaceTool] = FieldInfo(alias="spaceTools")
