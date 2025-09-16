# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ModelListPathsInfoResponse",
    "ModelListPathsInfoResponseItem",
    "ModelListPathsInfoResponseItemLastCommit",
    "ModelListPathsInfoResponseItemLFS",
    "ModelListPathsInfoResponseItemSecurityFileStatus",
    "ModelListPathsInfoResponseItemSecurityFileStatusAvScan",
    "ModelListPathsInfoResponseItemSecurityFileStatusAvScanPickleImport",
    "ModelListPathsInfoResponseItemSecurityFileStatusPickleImportScan",
    "ModelListPathsInfoResponseItemSecurityFileStatusPickleImportScanPickleImport",
    "ModelListPathsInfoResponseItemSecurityFileStatusJFrogScan",
    "ModelListPathsInfoResponseItemSecurityFileStatusJFrogScanPickleImport",
    "ModelListPathsInfoResponseItemSecurityFileStatusProtectAIScan",
    "ModelListPathsInfoResponseItemSecurityFileStatusProtectAIScanPickleImport",
]


class ModelListPathsInfoResponseItemLastCommit(BaseModel):
    id: str

    date: str

    title: str


class ModelListPathsInfoResponseItemLFS(BaseModel):
    pointer_size: float = FieldInfo(alias="pointerSize")


class ModelListPathsInfoResponseItemSecurityFileStatusAvScanPickleImport(BaseModel):
    module: str

    name: str

    safety: Literal["innocuous", "suspicious", "dangerous"]


class ModelListPathsInfoResponseItemSecurityFileStatusAvScan(BaseModel):
    status: Literal["unscanned", "safe", "queued", "error", "caution", "suspicious", "unsafe"]

    message: Optional[str] = None

    pickle_imports: Optional[List[ModelListPathsInfoResponseItemSecurityFileStatusAvScanPickleImport]] = FieldInfo(
        alias="pickleImports", default=None
    )

    report_label: Optional[str] = FieldInfo(alias="reportLabel", default=None)

    report_link: Optional[str] = FieldInfo(alias="reportLink", default=None)

    version: Optional[str] = None


class ModelListPathsInfoResponseItemSecurityFileStatusPickleImportScanPickleImport(BaseModel):
    module: str

    name: str

    safety: Literal["innocuous", "suspicious", "dangerous"]


class ModelListPathsInfoResponseItemSecurityFileStatusPickleImportScan(BaseModel):
    status: Literal["unscanned", "safe", "queued", "error", "caution", "suspicious", "unsafe"]

    message: Optional[str] = None

    pickle_imports: Optional[List[ModelListPathsInfoResponseItemSecurityFileStatusPickleImportScanPickleImport]] = (
        FieldInfo(alias="pickleImports", default=None)
    )

    report_label: Optional[str] = FieldInfo(alias="reportLabel", default=None)

    report_link: Optional[str] = FieldInfo(alias="reportLink", default=None)

    version: Optional[str] = None


class ModelListPathsInfoResponseItemSecurityFileStatusJFrogScanPickleImport(BaseModel):
    module: str

    name: str

    safety: Literal["innocuous", "suspicious", "dangerous"]


class ModelListPathsInfoResponseItemSecurityFileStatusJFrogScan(BaseModel):
    status: Literal["unscanned", "safe", "queued", "error", "caution", "suspicious", "unsafe"]

    message: Optional[str] = None

    pickle_imports: Optional[List[ModelListPathsInfoResponseItemSecurityFileStatusJFrogScanPickleImport]] = FieldInfo(
        alias="pickleImports", default=None
    )

    report_label: Optional[str] = FieldInfo(alias="reportLabel", default=None)

    report_link: Optional[str] = FieldInfo(alias="reportLink", default=None)

    version: Optional[str] = None


class ModelListPathsInfoResponseItemSecurityFileStatusProtectAIScanPickleImport(BaseModel):
    module: str

    name: str

    safety: Literal["innocuous", "suspicious", "dangerous"]


class ModelListPathsInfoResponseItemSecurityFileStatusProtectAIScan(BaseModel):
    status: Literal["unscanned", "safe", "queued", "error", "caution", "suspicious", "unsafe"]

    message: Optional[str] = None

    pickle_imports: Optional[List[ModelListPathsInfoResponseItemSecurityFileStatusProtectAIScanPickleImport]] = (
        FieldInfo(alias="pickleImports", default=None)
    )

    report_label: Optional[str] = FieldInfo(alias="reportLabel", default=None)

    report_link: Optional[str] = FieldInfo(alias="reportLink", default=None)

    version: Optional[str] = None


class ModelListPathsInfoResponseItemSecurityFileStatus(BaseModel):
    av_scan: ModelListPathsInfoResponseItemSecurityFileStatusAvScan = FieldInfo(alias="avScan")

    pickle_import_scan: ModelListPathsInfoResponseItemSecurityFileStatusPickleImportScan = FieldInfo(
        alias="pickleImportScan"
    )

    status: Literal["unscanned", "safe", "queued", "error", "caution", "suspicious", "unsafe"]

    j_frog_scan: Optional[ModelListPathsInfoResponseItemSecurityFileStatusJFrogScan] = FieldInfo(
        alias="jFrogScan", default=None
    )

    protect_ai_scan: Optional[ModelListPathsInfoResponseItemSecurityFileStatusProtectAIScan] = FieldInfo(
        alias="protectAiScan", default=None
    )


class ModelListPathsInfoResponseItem(BaseModel):
    oid: str

    path: str

    size: float

    type: Literal["file", "directory", "unknown"]

    last_commit: Optional[ModelListPathsInfoResponseItemLastCommit] = FieldInfo(alias="lastCommit", default=None)

    lfs: Optional[ModelListPathsInfoResponseItemLFS] = None

    security_file_status: Optional[ModelListPathsInfoResponseItemSecurityFileStatus] = FieldInfo(
        alias="securityFileStatus", default=None
    )


ModelListPathsInfoResponse: TypeAlias = List[ModelListPathsInfoResponseItem]
