# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ModelGetXetReadTokenResponse"]


class ModelGetXetReadTokenResponse(BaseModel):
    access_token: str = FieldInfo(alias="accessToken")

    cas_url: str = FieldInfo(alias="casUrl")

    exp: float
