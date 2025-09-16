# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "DatasetListTreeContentResponse",
    "DatasetListTreeContentResponseItem",
    "DatasetListTreeContentResponseItemLastCommit",
    "DatasetListTreeContentResponseItemLFS",
    "DatasetListTreeContentResponseItemSecurityFileStatus",
    "DatasetListTreeContentResponseItemSecurityFileStatusAvScan",
    "DatasetListTreeContentResponseItemSecurityFileStatusAvScanPickleImport",
    "DatasetListTreeContentResponseItemSecurityFileStatusPickleImportScan",
    "DatasetListTreeContentResponseItemSecurityFileStatusPickleImportScanPickleImport",
    "DatasetListTreeContentResponseItemSecurityFileStatusJFrogScan",
    "DatasetListTreeContentResponseItemSecurityFileStatusJFrogScanPickleImport",
    "DatasetListTreeContentResponseItemSecurityFileStatusProtectAIScan",
    "DatasetListTreeContentResponseItemSecurityFileStatusProtectAIScanPickleImport",
]


class DatasetListTreeContentResponseItemLastCommit(BaseModel):
    id: str

    date: datetime

    title: str


class DatasetListTreeContentResponseItemLFS(BaseModel):
    oid: str

    pointer_size: int = FieldInfo(alias="pointerSize")

    size: int


class DatasetListTreeContentResponseItemSecurityFileStatusAvScanPickleImport(BaseModel):
    module: str

    name: str

    safety: Literal["innocuous", "suspicious", "dangerous"]


class DatasetListTreeContentResponseItemSecurityFileStatusAvScan(BaseModel):
    status: Literal["unscanned", "safe", "queued", "error", "caution", "suspicious", "unsafe"]

    message: Optional[str] = None

    pickle_imports: Optional[List[DatasetListTreeContentResponseItemSecurityFileStatusAvScanPickleImport]] = FieldInfo(
        alias="pickleImports", default=None
    )

    report_label: Optional[str] = FieldInfo(alias="reportLabel", default=None)

    report_link: Optional[str] = FieldInfo(alias="reportLink", default=None)

    version: Optional[str] = None


class DatasetListTreeContentResponseItemSecurityFileStatusPickleImportScanPickleImport(BaseModel):
    module: str

    name: str

    safety: Literal["innocuous", "suspicious", "dangerous"]


class DatasetListTreeContentResponseItemSecurityFileStatusPickleImportScan(BaseModel):
    status: Literal["unscanned", "safe", "queued", "error", "caution", "suspicious", "unsafe"]

    message: Optional[str] = None

    pickle_imports: Optional[List[DatasetListTreeContentResponseItemSecurityFileStatusPickleImportScanPickleImport]] = (
        FieldInfo(alias="pickleImports", default=None)
    )

    report_label: Optional[str] = FieldInfo(alias="reportLabel", default=None)

    report_link: Optional[str] = FieldInfo(alias="reportLink", default=None)

    version: Optional[str] = None


class DatasetListTreeContentResponseItemSecurityFileStatusJFrogScanPickleImport(BaseModel):
    module: str

    name: str

    safety: Literal["innocuous", "suspicious", "dangerous"]


class DatasetListTreeContentResponseItemSecurityFileStatusJFrogScan(BaseModel):
    status: Literal["unscanned", "safe", "queued", "error", "caution", "suspicious", "unsafe"]

    message: Optional[str] = None

    pickle_imports: Optional[List[DatasetListTreeContentResponseItemSecurityFileStatusJFrogScanPickleImport]] = (
        FieldInfo(alias="pickleImports", default=None)
    )

    report_label: Optional[str] = FieldInfo(alias="reportLabel", default=None)

    report_link: Optional[str] = FieldInfo(alias="reportLink", default=None)

    version: Optional[str] = None


class DatasetListTreeContentResponseItemSecurityFileStatusProtectAIScanPickleImport(BaseModel):
    module: str

    name: str

    safety: Literal["innocuous", "suspicious", "dangerous"]


class DatasetListTreeContentResponseItemSecurityFileStatusProtectAIScan(BaseModel):
    status: Literal["unscanned", "safe", "queued", "error", "caution", "suspicious", "unsafe"]

    message: Optional[str] = None

    pickle_imports: Optional[List[DatasetListTreeContentResponseItemSecurityFileStatusProtectAIScanPickleImport]] = (
        FieldInfo(alias="pickleImports", default=None)
    )

    report_label: Optional[str] = FieldInfo(alias="reportLabel", default=None)

    report_link: Optional[str] = FieldInfo(alias="reportLink", default=None)

    version: Optional[str] = None


class DatasetListTreeContentResponseItemSecurityFileStatus(BaseModel):
    av_scan: DatasetListTreeContentResponseItemSecurityFileStatusAvScan = FieldInfo(alias="avScan")

    pickle_import_scan: DatasetListTreeContentResponseItemSecurityFileStatusPickleImportScan = FieldInfo(
        alias="pickleImportScan"
    )

    status: Literal["unscanned", "safe", "queued", "error", "caution", "suspicious", "unsafe"]

    j_frog_scan: Optional[DatasetListTreeContentResponseItemSecurityFileStatusJFrogScan] = FieldInfo(
        alias="jFrogScan", default=None
    )

    protect_ai_scan: Optional[DatasetListTreeContentResponseItemSecurityFileStatusProtectAIScan] = FieldInfo(
        alias="protectAiScan", default=None
    )


class DatasetListTreeContentResponseItem(BaseModel):
    oid: str

    type: Literal["file", "directory", "unknown"]

    last_commit: Optional[DatasetListTreeContentResponseItemLastCommit] = FieldInfo(alias="lastCommit", default=None)

    lfs: Optional[DatasetListTreeContentResponseItemLFS] = None

    security_file_status: Optional[DatasetListTreeContentResponseItemSecurityFileStatus] = FieldInfo(
        alias="securityFileStatus", default=None
    )

    size: Optional[int] = None
    """If the file is a LFS pointer, it'll return the size of the remote file"""

    xet_hash: Optional[str] = FieldInfo(alias="xetHash", default=None)


DatasetListTreeContentResponse: TypeAlias = List[DatasetListTreeContentResponseItem]
