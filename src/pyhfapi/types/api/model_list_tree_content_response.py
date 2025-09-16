# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ModelListTreeContentResponse",
    "ModelListTreeContentResponseItem",
    "ModelListTreeContentResponseItemLastCommit",
    "ModelListTreeContentResponseItemLFS",
    "ModelListTreeContentResponseItemSecurityFileStatus",
    "ModelListTreeContentResponseItemSecurityFileStatusAvScan",
    "ModelListTreeContentResponseItemSecurityFileStatusAvScanPickleImport",
    "ModelListTreeContentResponseItemSecurityFileStatusPickleImportScan",
    "ModelListTreeContentResponseItemSecurityFileStatusPickleImportScanPickleImport",
    "ModelListTreeContentResponseItemSecurityFileStatusJFrogScan",
    "ModelListTreeContentResponseItemSecurityFileStatusJFrogScanPickleImport",
    "ModelListTreeContentResponseItemSecurityFileStatusProtectAIScan",
    "ModelListTreeContentResponseItemSecurityFileStatusProtectAIScanPickleImport",
]


class ModelListTreeContentResponseItemLastCommit(BaseModel):
    id: str

    date: datetime

    title: str


class ModelListTreeContentResponseItemLFS(BaseModel):
    oid: str

    pointer_size: int = FieldInfo(alias="pointerSize")

    size: int


class ModelListTreeContentResponseItemSecurityFileStatusAvScanPickleImport(BaseModel):
    module: str

    name: str

    safety: Literal["innocuous", "suspicious", "dangerous"]


class ModelListTreeContentResponseItemSecurityFileStatusAvScan(BaseModel):
    status: Literal["unscanned", "safe", "queued", "error", "caution", "suspicious", "unsafe"]

    message: Optional[str] = None

    pickle_imports: Optional[List[ModelListTreeContentResponseItemSecurityFileStatusAvScanPickleImport]] = FieldInfo(
        alias="pickleImports", default=None
    )

    report_label: Optional[str] = FieldInfo(alias="reportLabel", default=None)

    report_link: Optional[str] = FieldInfo(alias="reportLink", default=None)

    version: Optional[str] = None


class ModelListTreeContentResponseItemSecurityFileStatusPickleImportScanPickleImport(BaseModel):
    module: str

    name: str

    safety: Literal["innocuous", "suspicious", "dangerous"]


class ModelListTreeContentResponseItemSecurityFileStatusPickleImportScan(BaseModel):
    status: Literal["unscanned", "safe", "queued", "error", "caution", "suspicious", "unsafe"]

    message: Optional[str] = None

    pickle_imports: Optional[List[ModelListTreeContentResponseItemSecurityFileStatusPickleImportScanPickleImport]] = (
        FieldInfo(alias="pickleImports", default=None)
    )

    report_label: Optional[str] = FieldInfo(alias="reportLabel", default=None)

    report_link: Optional[str] = FieldInfo(alias="reportLink", default=None)

    version: Optional[str] = None


class ModelListTreeContentResponseItemSecurityFileStatusJFrogScanPickleImport(BaseModel):
    module: str

    name: str

    safety: Literal["innocuous", "suspicious", "dangerous"]


class ModelListTreeContentResponseItemSecurityFileStatusJFrogScan(BaseModel):
    status: Literal["unscanned", "safe", "queued", "error", "caution", "suspicious", "unsafe"]

    message: Optional[str] = None

    pickle_imports: Optional[List[ModelListTreeContentResponseItemSecurityFileStatusJFrogScanPickleImport]] = FieldInfo(
        alias="pickleImports", default=None
    )

    report_label: Optional[str] = FieldInfo(alias="reportLabel", default=None)

    report_link: Optional[str] = FieldInfo(alias="reportLink", default=None)

    version: Optional[str] = None


class ModelListTreeContentResponseItemSecurityFileStatusProtectAIScanPickleImport(BaseModel):
    module: str

    name: str

    safety: Literal["innocuous", "suspicious", "dangerous"]


class ModelListTreeContentResponseItemSecurityFileStatusProtectAIScan(BaseModel):
    status: Literal["unscanned", "safe", "queued", "error", "caution", "suspicious", "unsafe"]

    message: Optional[str] = None

    pickle_imports: Optional[List[ModelListTreeContentResponseItemSecurityFileStatusProtectAIScanPickleImport]] = (
        FieldInfo(alias="pickleImports", default=None)
    )

    report_label: Optional[str] = FieldInfo(alias="reportLabel", default=None)

    report_link: Optional[str] = FieldInfo(alias="reportLink", default=None)

    version: Optional[str] = None


class ModelListTreeContentResponseItemSecurityFileStatus(BaseModel):
    av_scan: ModelListTreeContentResponseItemSecurityFileStatusAvScan = FieldInfo(alias="avScan")

    pickle_import_scan: ModelListTreeContentResponseItemSecurityFileStatusPickleImportScan = FieldInfo(
        alias="pickleImportScan"
    )

    status: Literal["unscanned", "safe", "queued", "error", "caution", "suspicious", "unsafe"]

    j_frog_scan: Optional[ModelListTreeContentResponseItemSecurityFileStatusJFrogScan] = FieldInfo(
        alias="jFrogScan", default=None
    )

    protect_ai_scan: Optional[ModelListTreeContentResponseItemSecurityFileStatusProtectAIScan] = FieldInfo(
        alias="protectAiScan", default=None
    )


class ModelListTreeContentResponseItem(BaseModel):
    oid: str

    type: Literal["file", "directory", "unknown"]

    last_commit: Optional[ModelListTreeContentResponseItemLastCommit] = FieldInfo(alias="lastCommit", default=None)

    lfs: Optional[ModelListTreeContentResponseItemLFS] = None

    security_file_status: Optional[ModelListTreeContentResponseItemSecurityFileStatus] = FieldInfo(
        alias="securityFileStatus", default=None
    )

    size: Optional[int] = None
    """If the file is a LFS pointer, it'll return the size of the remote file"""

    xet_hash: Optional[str] = FieldInfo(alias="xetHash", default=None)


ModelListTreeContentResponse: TypeAlias = List[ModelListTreeContentResponseItem]
