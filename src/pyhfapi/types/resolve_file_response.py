# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ResolveFileResponse"]


class ResolveFileResponse(BaseModel):
    etag: str
    """The ETag of the file"""

    hash: str
    """The XET hash of the file"""

    reconstruction_url: str = FieldInfo(alias="reconstructionUrl")
    """The XET reconstruction URL for the file"""

    refresh_url: str = FieldInfo(alias="refreshUrl")
    """The XET auth URL for the file"""

    size: float
    """The size of the file"""
