# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "DatasetListPathsInfoResponse",
    "DatasetListPathsInfoResponseItem",
    "DatasetListPathsInfoResponseItemLastCommit",
    "DatasetListPathsInfoResponseItemLFS",
    "DatasetListPathsInfoResponseItemSecurityFileStatus",
    "DatasetListPathsInfoResponseItemSecurityFileStatusAvScan",
    "DatasetListPathsInfoResponseItemSecurityFileStatusAvScanPickleImport",
    "DatasetListPathsInfoResponseItemSecurityFileStatusPickleImportScan",
    "DatasetListPathsInfoResponseItemSecurityFileStatusPickleImportScanPickleImport",
    "DatasetListPathsInfoResponseItemSecurityFileStatusJFrogScan",
    "DatasetListPathsInfoResponseItemSecurityFileStatusJFrogScanPickleImport",
    "DatasetListPathsInfoResponseItemSecurityFileStatusProtectAIScan",
    "DatasetListPathsInfoResponseItemSecurityFileStatusProtectAIScanPickleImport",
]


class DatasetListPathsInfoResponseItemLastCommit(BaseModel):
    id: str

    date: str

    title: str


class DatasetListPathsInfoResponseItemLFS(BaseModel):
    pointer_size: float = FieldInfo(alias="pointerSize")


class DatasetListPathsInfoResponseItemSecurityFileStatusAvScanPickleImport(BaseModel):
    module: str

    name: str

    safety: Literal["innocuous", "suspicious", "dangerous"]


class DatasetListPathsInfoResponseItemSecurityFileStatusAvScan(BaseModel):
    status: Literal["unscanned", "safe", "queued", "error", "caution", "suspicious", "unsafe"]

    message: Optional[str] = None

    pickle_imports: Optional[List[DatasetListPathsInfoResponseItemSecurityFileStatusAvScanPickleImport]] = FieldInfo(
        alias="pickleImports", default=None
    )

    report_label: Optional[str] = FieldInfo(alias="reportLabel", default=None)

    report_link: Optional[str] = FieldInfo(alias="reportLink", default=None)

    version: Optional[str] = None


class DatasetListPathsInfoResponseItemSecurityFileStatusPickleImportScanPickleImport(BaseModel):
    module: str

    name: str

    safety: Literal["innocuous", "suspicious", "dangerous"]


class DatasetListPathsInfoResponseItemSecurityFileStatusPickleImportScan(BaseModel):
    status: Literal["unscanned", "safe", "queued", "error", "caution", "suspicious", "unsafe"]

    message: Optional[str] = None

    pickle_imports: Optional[List[DatasetListPathsInfoResponseItemSecurityFileStatusPickleImportScanPickleImport]] = (
        FieldInfo(alias="pickleImports", default=None)
    )

    report_label: Optional[str] = FieldInfo(alias="reportLabel", default=None)

    report_link: Optional[str] = FieldInfo(alias="reportLink", default=None)

    version: Optional[str] = None


class DatasetListPathsInfoResponseItemSecurityFileStatusJFrogScanPickleImport(BaseModel):
    module: str

    name: str

    safety: Literal["innocuous", "suspicious", "dangerous"]


class DatasetListPathsInfoResponseItemSecurityFileStatusJFrogScan(BaseModel):
    status: Literal["unscanned", "safe", "queued", "error", "caution", "suspicious", "unsafe"]

    message: Optional[str] = None

    pickle_imports: Optional[List[DatasetListPathsInfoResponseItemSecurityFileStatusJFrogScanPickleImport]] = FieldInfo(
        alias="pickleImports", default=None
    )

    report_label: Optional[str] = FieldInfo(alias="reportLabel", default=None)

    report_link: Optional[str] = FieldInfo(alias="reportLink", default=None)

    version: Optional[str] = None


class DatasetListPathsInfoResponseItemSecurityFileStatusProtectAIScanPickleImport(BaseModel):
    module: str

    name: str

    safety: Literal["innocuous", "suspicious", "dangerous"]


class DatasetListPathsInfoResponseItemSecurityFileStatusProtectAIScan(BaseModel):
    status: Literal["unscanned", "safe", "queued", "error", "caution", "suspicious", "unsafe"]

    message: Optional[str] = None

    pickle_imports: Optional[List[DatasetListPathsInfoResponseItemSecurityFileStatusProtectAIScanPickleImport]] = (
        FieldInfo(alias="pickleImports", default=None)
    )

    report_label: Optional[str] = FieldInfo(alias="reportLabel", default=None)

    report_link: Optional[str] = FieldInfo(alias="reportLink", default=None)

    version: Optional[str] = None


class DatasetListPathsInfoResponseItemSecurityFileStatus(BaseModel):
    av_scan: DatasetListPathsInfoResponseItemSecurityFileStatusAvScan = FieldInfo(alias="avScan")

    pickle_import_scan: DatasetListPathsInfoResponseItemSecurityFileStatusPickleImportScan = FieldInfo(
        alias="pickleImportScan"
    )

    status: Literal["unscanned", "safe", "queued", "error", "caution", "suspicious", "unsafe"]

    j_frog_scan: Optional[DatasetListPathsInfoResponseItemSecurityFileStatusJFrogScan] = FieldInfo(
        alias="jFrogScan", default=None
    )

    protect_ai_scan: Optional[DatasetListPathsInfoResponseItemSecurityFileStatusProtectAIScan] = FieldInfo(
        alias="protectAiScan", default=None
    )


class DatasetListPathsInfoResponseItem(BaseModel):
    oid: str

    path: str

    size: float

    type: Literal["file", "directory", "unknown"]

    last_commit: Optional[DatasetListPathsInfoResponseItemLastCommit] = FieldInfo(alias="lastCommit", default=None)

    lfs: Optional[DatasetListPathsInfoResponseItemLFS] = None

    security_file_status: Optional[DatasetListPathsInfoResponseItemSecurityFileStatus] = FieldInfo(
        alias="securityFileStatus", default=None
    )


DatasetListPathsInfoResponse: TypeAlias = List[DatasetListPathsInfoResponseItem]
