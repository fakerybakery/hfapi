# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "SpaceListPathsInfoResponse",
    "SpaceListPathsInfoResponseItem",
    "SpaceListPathsInfoResponseItemLastCommit",
    "SpaceListPathsInfoResponseItemLFS",
    "SpaceListPathsInfoResponseItemSecurityFileStatus",
    "SpaceListPathsInfoResponseItemSecurityFileStatusAvScan",
    "SpaceListPathsInfoResponseItemSecurityFileStatusAvScanPickleImport",
    "SpaceListPathsInfoResponseItemSecurityFileStatusPickleImportScan",
    "SpaceListPathsInfoResponseItemSecurityFileStatusPickleImportScanPickleImport",
    "SpaceListPathsInfoResponseItemSecurityFileStatusJFrogScan",
    "SpaceListPathsInfoResponseItemSecurityFileStatusJFrogScanPickleImport",
    "SpaceListPathsInfoResponseItemSecurityFileStatusProtectAIScan",
    "SpaceListPathsInfoResponseItemSecurityFileStatusProtectAIScanPickleImport",
]


class SpaceListPathsInfoResponseItemLastCommit(BaseModel):
    id: str

    date: str

    title: str


class SpaceListPathsInfoResponseItemLFS(BaseModel):
    pointer_size: float = FieldInfo(alias="pointerSize")


class SpaceListPathsInfoResponseItemSecurityFileStatusAvScanPickleImport(BaseModel):
    module: str

    name: str

    safety: Literal["innocuous", "suspicious", "dangerous"]


class SpaceListPathsInfoResponseItemSecurityFileStatusAvScan(BaseModel):
    status: Literal["unscanned", "safe", "queued", "error", "caution", "suspicious", "unsafe"]

    message: Optional[str] = None

    pickle_imports: Optional[List[SpaceListPathsInfoResponseItemSecurityFileStatusAvScanPickleImport]] = FieldInfo(
        alias="pickleImports", default=None
    )

    report_label: Optional[str] = FieldInfo(alias="reportLabel", default=None)

    report_link: Optional[str] = FieldInfo(alias="reportLink", default=None)

    version: Optional[str] = None


class SpaceListPathsInfoResponseItemSecurityFileStatusPickleImportScanPickleImport(BaseModel):
    module: str

    name: str

    safety: Literal["innocuous", "suspicious", "dangerous"]


class SpaceListPathsInfoResponseItemSecurityFileStatusPickleImportScan(BaseModel):
    status: Literal["unscanned", "safe", "queued", "error", "caution", "suspicious", "unsafe"]

    message: Optional[str] = None

    pickle_imports: Optional[List[SpaceListPathsInfoResponseItemSecurityFileStatusPickleImportScanPickleImport]] = (
        FieldInfo(alias="pickleImports", default=None)
    )

    report_label: Optional[str] = FieldInfo(alias="reportLabel", default=None)

    report_link: Optional[str] = FieldInfo(alias="reportLink", default=None)

    version: Optional[str] = None


class SpaceListPathsInfoResponseItemSecurityFileStatusJFrogScanPickleImport(BaseModel):
    module: str

    name: str

    safety: Literal["innocuous", "suspicious", "dangerous"]


class SpaceListPathsInfoResponseItemSecurityFileStatusJFrogScan(BaseModel):
    status: Literal["unscanned", "safe", "queued", "error", "caution", "suspicious", "unsafe"]

    message: Optional[str] = None

    pickle_imports: Optional[List[SpaceListPathsInfoResponseItemSecurityFileStatusJFrogScanPickleImport]] = FieldInfo(
        alias="pickleImports", default=None
    )

    report_label: Optional[str] = FieldInfo(alias="reportLabel", default=None)

    report_link: Optional[str] = FieldInfo(alias="reportLink", default=None)

    version: Optional[str] = None


class SpaceListPathsInfoResponseItemSecurityFileStatusProtectAIScanPickleImport(BaseModel):
    module: str

    name: str

    safety: Literal["innocuous", "suspicious", "dangerous"]


class SpaceListPathsInfoResponseItemSecurityFileStatusProtectAIScan(BaseModel):
    status: Literal["unscanned", "safe", "queued", "error", "caution", "suspicious", "unsafe"]

    message: Optional[str] = None

    pickle_imports: Optional[List[SpaceListPathsInfoResponseItemSecurityFileStatusProtectAIScanPickleImport]] = (
        FieldInfo(alias="pickleImports", default=None)
    )

    report_label: Optional[str] = FieldInfo(alias="reportLabel", default=None)

    report_link: Optional[str] = FieldInfo(alias="reportLink", default=None)

    version: Optional[str] = None


class SpaceListPathsInfoResponseItemSecurityFileStatus(BaseModel):
    av_scan: SpaceListPathsInfoResponseItemSecurityFileStatusAvScan = FieldInfo(alias="avScan")

    pickle_import_scan: SpaceListPathsInfoResponseItemSecurityFileStatusPickleImportScan = FieldInfo(
        alias="pickleImportScan"
    )

    status: Literal["unscanned", "safe", "queued", "error", "caution", "suspicious", "unsafe"]

    j_frog_scan: Optional[SpaceListPathsInfoResponseItemSecurityFileStatusJFrogScan] = FieldInfo(
        alias="jFrogScan", default=None
    )

    protect_ai_scan: Optional[SpaceListPathsInfoResponseItemSecurityFileStatusProtectAIScan] = FieldInfo(
        alias="protectAiScan", default=None
    )


class SpaceListPathsInfoResponseItem(BaseModel):
    oid: str

    path: str

    size: float

    type: Literal["file", "directory", "unknown"]

    last_commit: Optional[SpaceListPathsInfoResponseItemLastCommit] = FieldInfo(alias="lastCommit", default=None)

    lfs: Optional[SpaceListPathsInfoResponseItemLFS] = None

    security_file_status: Optional[SpaceListPathsInfoResponseItemSecurityFileStatus] = FieldInfo(
        alias="securityFileStatus", default=None
    )


SpaceListPathsInfoResponse: TypeAlias = List[SpaceListPathsInfoResponseItem]
