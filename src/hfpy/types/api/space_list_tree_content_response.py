# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "SpaceListTreeContentResponse",
    "SpaceListTreeContentResponseItem",
    "SpaceListTreeContentResponseItemLastCommit",
    "SpaceListTreeContentResponseItemLFS",
    "SpaceListTreeContentResponseItemSecurityFileStatus",
    "SpaceListTreeContentResponseItemSecurityFileStatusAvScan",
    "SpaceListTreeContentResponseItemSecurityFileStatusAvScanPickleImport",
    "SpaceListTreeContentResponseItemSecurityFileStatusPickleImportScan",
    "SpaceListTreeContentResponseItemSecurityFileStatusPickleImportScanPickleImport",
    "SpaceListTreeContentResponseItemSecurityFileStatusJFrogScan",
    "SpaceListTreeContentResponseItemSecurityFileStatusJFrogScanPickleImport",
    "SpaceListTreeContentResponseItemSecurityFileStatusProtectAIScan",
    "SpaceListTreeContentResponseItemSecurityFileStatusProtectAIScanPickleImport",
]


class SpaceListTreeContentResponseItemLastCommit(BaseModel):
    id: str

    date: datetime

    title: str


class SpaceListTreeContentResponseItemLFS(BaseModel):
    oid: str

    pointer_size: int = FieldInfo(alias="pointerSize")

    size: int


class SpaceListTreeContentResponseItemSecurityFileStatusAvScanPickleImport(BaseModel):
    module: str

    name: str

    safety: Literal["innocuous", "suspicious", "dangerous"]


class SpaceListTreeContentResponseItemSecurityFileStatusAvScan(BaseModel):
    status: Literal["unscanned", "safe", "queued", "error", "caution", "suspicious", "unsafe"]

    message: Optional[str] = None

    pickle_imports: Optional[List[SpaceListTreeContentResponseItemSecurityFileStatusAvScanPickleImport]] = FieldInfo(
        alias="pickleImports", default=None
    )

    report_label: Optional[str] = FieldInfo(alias="reportLabel", default=None)

    report_link: Optional[str] = FieldInfo(alias="reportLink", default=None)

    version: Optional[str] = None


class SpaceListTreeContentResponseItemSecurityFileStatusPickleImportScanPickleImport(BaseModel):
    module: str

    name: str

    safety: Literal["innocuous", "suspicious", "dangerous"]


class SpaceListTreeContentResponseItemSecurityFileStatusPickleImportScan(BaseModel):
    status: Literal["unscanned", "safe", "queued", "error", "caution", "suspicious", "unsafe"]

    message: Optional[str] = None

    pickle_imports: Optional[List[SpaceListTreeContentResponseItemSecurityFileStatusPickleImportScanPickleImport]] = (
        FieldInfo(alias="pickleImports", default=None)
    )

    report_label: Optional[str] = FieldInfo(alias="reportLabel", default=None)

    report_link: Optional[str] = FieldInfo(alias="reportLink", default=None)

    version: Optional[str] = None


class SpaceListTreeContentResponseItemSecurityFileStatusJFrogScanPickleImport(BaseModel):
    module: str

    name: str

    safety: Literal["innocuous", "suspicious", "dangerous"]


class SpaceListTreeContentResponseItemSecurityFileStatusJFrogScan(BaseModel):
    status: Literal["unscanned", "safe", "queued", "error", "caution", "suspicious", "unsafe"]

    message: Optional[str] = None

    pickle_imports: Optional[List[SpaceListTreeContentResponseItemSecurityFileStatusJFrogScanPickleImport]] = FieldInfo(
        alias="pickleImports", default=None
    )

    report_label: Optional[str] = FieldInfo(alias="reportLabel", default=None)

    report_link: Optional[str] = FieldInfo(alias="reportLink", default=None)

    version: Optional[str] = None


class SpaceListTreeContentResponseItemSecurityFileStatusProtectAIScanPickleImport(BaseModel):
    module: str

    name: str

    safety: Literal["innocuous", "suspicious", "dangerous"]


class SpaceListTreeContentResponseItemSecurityFileStatusProtectAIScan(BaseModel):
    status: Literal["unscanned", "safe", "queued", "error", "caution", "suspicious", "unsafe"]

    message: Optional[str] = None

    pickle_imports: Optional[List[SpaceListTreeContentResponseItemSecurityFileStatusProtectAIScanPickleImport]] = (
        FieldInfo(alias="pickleImports", default=None)
    )

    report_label: Optional[str] = FieldInfo(alias="reportLabel", default=None)

    report_link: Optional[str] = FieldInfo(alias="reportLink", default=None)

    version: Optional[str] = None


class SpaceListTreeContentResponseItemSecurityFileStatus(BaseModel):
    av_scan: SpaceListTreeContentResponseItemSecurityFileStatusAvScan = FieldInfo(alias="avScan")

    pickle_import_scan: SpaceListTreeContentResponseItemSecurityFileStatusPickleImportScan = FieldInfo(
        alias="pickleImportScan"
    )

    status: Literal["unscanned", "safe", "queued", "error", "caution", "suspicious", "unsafe"]

    j_frog_scan: Optional[SpaceListTreeContentResponseItemSecurityFileStatusJFrogScan] = FieldInfo(
        alias="jFrogScan", default=None
    )

    protect_ai_scan: Optional[SpaceListTreeContentResponseItemSecurityFileStatusProtectAIScan] = FieldInfo(
        alias="protectAiScan", default=None
    )


class SpaceListTreeContentResponseItem(BaseModel):
    oid: str

    type: Literal["file", "directory", "unknown"]

    last_commit: Optional[SpaceListTreeContentResponseItemLastCommit] = FieldInfo(alias="lastCommit", default=None)

    lfs: Optional[SpaceListTreeContentResponseItemLFS] = None

    security_file_status: Optional[SpaceListTreeContentResponseItemSecurityFileStatus] = FieldInfo(
        alias="securityFileStatus", default=None
    )

    size: Optional[int] = None
    """If the file is a LFS pointer, it'll return the size of the remote file"""

    xet_hash: Optional[str] = FieldInfo(alias="xetHash", default=None)


SpaceListTreeContentResponse: TypeAlias = List[SpaceListTreeContentResponseItem]
