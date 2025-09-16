# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ModelCheckPreuploadResponse", "File"]


class File(BaseModel):
    path: str

    should_ignore: bool = FieldInfo(alias="shouldIgnore")

    upload_mode: Literal["lfs", "regular"] = FieldInfo(alias="uploadMode")

    oid: Optional[str] = None
    """The oid of the blob if it already exists in the repository.

    If the blob is a LFS file, it'll be the lfs oid.
    """


class ModelCheckPreuploadResponse(BaseModel):
    commit_oid: str = FieldInfo(alias="commitOid")

    files: List[File]
