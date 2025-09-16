# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "RepoCreateParams",
    "Variant0",
    "Variant0File",
    "Variant1",
    "Variant1File",
    "Variant2",
    "Variant2File",
    "Variant2Secret",
    "Variant2Variable",
]


class Variant0(TypedDict, total=False):
    type: Required[Literal["dataset"]]

    files: Iterable[Variant0File]

    license: Literal[
        "apache-2.0",
        "mit",
        "openrail",
        "bigscience-openrail-m",
        "creativeml-openrail-m",
        "bigscience-bloom-rail-1.0",
        "bigcode-openrail-m",
        "afl-3.0",
        "artistic-2.0",
        "bsl-1.0",
        "bsd",
        "bsd-2-clause",
        "bsd-3-clause",
        "bsd-3-clause-clear",
        "c-uda",
        "cc",
        "cc0-1.0",
        "cc-by-2.0",
        "cc-by-2.5",
        "cc-by-3.0",
        "cc-by-4.0",
        "cc-by-sa-3.0",
        "cc-by-sa-4.0",
        "cc-by-nc-2.0",
        "cc-by-nc-3.0",
        "cc-by-nc-4.0",
        "cc-by-nd-4.0",
        "cc-by-nc-nd-3.0",
        "cc-by-nc-nd-4.0",
        "cc-by-nc-sa-2.0",
        "cc-by-nc-sa-3.0",
        "cc-by-nc-sa-4.0",
        "cdla-sharing-1.0",
        "cdla-permissive-1.0",
        "cdla-permissive-2.0",
        "wtfpl",
        "ecl-2.0",
        "epl-1.0",
        "epl-2.0",
        "etalab-2.0",
        "eupl-1.1",
        "eupl-1.2",
        "agpl-3.0",
        "gfdl",
        "gpl",
        "gpl-2.0",
        "gpl-3.0",
        "lgpl",
        "lgpl-2.1",
        "lgpl-3.0",
        "isc",
        "h-research",
        "intel-research",
        "lppl-1.3c",
        "ms-pl",
        "apple-ascl",
        "apple-amlr",
        "mpl-2.0",
        "odc-by",
        "odbl",
        "open-mdw",
        "openrail++",
        "osl-3.0",
        "postgresql",
        "ofl-1.1",
        "ncsa",
        "unlicense",
        "zlib",
        "pddl",
        "lgpl-lr",
        "deepfloyd-if-license",
        "fair-noncommercial-research-license",
        "llama2",
        "llama3",
        "llama3.1",
        "llama3.2",
        "llama3.3",
        "llama4",
        "gemma",
        "unknown",
        "other",
    ]
    """The license of the repository.

    You can select 'Other' if your license is not in the list
    """

    license_link: Union[Literal["LICENSE", "LICENSE.md"], str]

    license_name: str

    name: str

    organization: Optional[str]

    private: Optional[bool]
    """Repository visibility. Defaults to public"""

    resource_group_id: Annotated[Optional[str], PropertyInfo(alias="resourceGroupId")]


class Variant0File(TypedDict, total=False):
    content: Required[str]

    path: Required[str]

    encoding: Literal["utf-8", "base64"]


class Variant1(TypedDict, total=False):
    files: Iterable[Variant1File]

    license: Literal[
        "apache-2.0",
        "mit",
        "openrail",
        "bigscience-openrail-m",
        "creativeml-openrail-m",
        "bigscience-bloom-rail-1.0",
        "bigcode-openrail-m",
        "afl-3.0",
        "artistic-2.0",
        "bsl-1.0",
        "bsd",
        "bsd-2-clause",
        "bsd-3-clause",
        "bsd-3-clause-clear",
        "c-uda",
        "cc",
        "cc0-1.0",
        "cc-by-2.0",
        "cc-by-2.5",
        "cc-by-3.0",
        "cc-by-4.0",
        "cc-by-sa-3.0",
        "cc-by-sa-4.0",
        "cc-by-nc-2.0",
        "cc-by-nc-3.0",
        "cc-by-nc-4.0",
        "cc-by-nd-4.0",
        "cc-by-nc-nd-3.0",
        "cc-by-nc-nd-4.0",
        "cc-by-nc-sa-2.0",
        "cc-by-nc-sa-3.0",
        "cc-by-nc-sa-4.0",
        "cdla-sharing-1.0",
        "cdla-permissive-1.0",
        "cdla-permissive-2.0",
        "wtfpl",
        "ecl-2.0",
        "epl-1.0",
        "epl-2.0",
        "etalab-2.0",
        "eupl-1.1",
        "eupl-1.2",
        "agpl-3.0",
        "gfdl",
        "gpl",
        "gpl-2.0",
        "gpl-3.0",
        "lgpl",
        "lgpl-2.1",
        "lgpl-3.0",
        "isc",
        "h-research",
        "intel-research",
        "lppl-1.3c",
        "ms-pl",
        "apple-ascl",
        "apple-amlr",
        "mpl-2.0",
        "odc-by",
        "odbl",
        "open-mdw",
        "openrail++",
        "osl-3.0",
        "postgresql",
        "ofl-1.1",
        "ncsa",
        "unlicense",
        "zlib",
        "pddl",
        "lgpl-lr",
        "deepfloyd-if-license",
        "fair-noncommercial-research-license",
        "llama2",
        "llama3",
        "llama3.1",
        "llama3.2",
        "llama3.3",
        "llama4",
        "gemma",
        "unknown",
        "other",
    ]
    """The license of the repository.

    You can select 'Other' if your license is not in the list
    """

    license_link: Union[Literal["LICENSE", "LICENSE.md"], str]

    license_name: str

    name: str

    organization: Optional[str]

    private: Optional[bool]
    """Repository visibility. Defaults to public"""

    resource_group_id: Annotated[Optional[str], PropertyInfo(alias="resourceGroupId")]

    type: Literal["model"]


class Variant1File(TypedDict, total=False):
    content: Required[str]

    path: Required[str]

    encoding: Literal["utf-8", "base64"]


class Variant2(TypedDict, total=False):
    sdk: Required[Literal["gradio", "docker", "static", "streamlit"]]

    type: Required[Literal["space"]]

    dev_mode_enabled: Annotated[bool, PropertyInfo(alias="devModeEnabled")]

    files: Iterable[Variant2File]

    hardware: Literal[
        "cpu-basic",
        "cpu-upgrade",
        "cpu-performance",
        "cpu-xl",
        "zero-a10g",
        "t4-small",
        "t4-medium",
        "l4x1",
        "l4x4",
        "l40sx1",
        "l40sx4",
        "l40sx8",
        "a10g-small",
        "a10g-large",
        "a10g-largex2",
        "a10g-largex4",
        "a100-large",
        "h100",
        "h100x8",
        "inf2x6",
        "zerogpu",
    ]
    """The hardware flavor of the space.

    If you select 'zero-a10g' or 'zerogpu', the SDK must be Gradio.
    """

    license: Literal[
        "apache-2.0",
        "mit",
        "openrail",
        "bigscience-openrail-m",
        "creativeml-openrail-m",
        "bigscience-bloom-rail-1.0",
        "bigcode-openrail-m",
        "afl-3.0",
        "artistic-2.0",
        "bsl-1.0",
        "bsd",
        "bsd-2-clause",
        "bsd-3-clause",
        "bsd-3-clause-clear",
        "c-uda",
        "cc",
        "cc0-1.0",
        "cc-by-2.0",
        "cc-by-2.5",
        "cc-by-3.0",
        "cc-by-4.0",
        "cc-by-sa-3.0",
        "cc-by-sa-4.0",
        "cc-by-nc-2.0",
        "cc-by-nc-3.0",
        "cc-by-nc-4.0",
        "cc-by-nd-4.0",
        "cc-by-nc-nd-3.0",
        "cc-by-nc-nd-4.0",
        "cc-by-nc-sa-2.0",
        "cc-by-nc-sa-3.0",
        "cc-by-nc-sa-4.0",
        "cdla-sharing-1.0",
        "cdla-permissive-1.0",
        "cdla-permissive-2.0",
        "wtfpl",
        "ecl-2.0",
        "epl-1.0",
        "epl-2.0",
        "etalab-2.0",
        "eupl-1.1",
        "eupl-1.2",
        "agpl-3.0",
        "gfdl",
        "gpl",
        "gpl-2.0",
        "gpl-3.0",
        "lgpl",
        "lgpl-2.1",
        "lgpl-3.0",
        "isc",
        "h-research",
        "intel-research",
        "lppl-1.3c",
        "ms-pl",
        "apple-ascl",
        "apple-amlr",
        "mpl-2.0",
        "odc-by",
        "odbl",
        "open-mdw",
        "openrail++",
        "osl-3.0",
        "postgresql",
        "ofl-1.1",
        "ncsa",
        "unlicense",
        "zlib",
        "pddl",
        "lgpl-lr",
        "deepfloyd-if-license",
        "fair-noncommercial-research-license",
        "llama2",
        "llama3",
        "llama3.1",
        "llama3.2",
        "llama3.3",
        "llama4",
        "gemma",
        "unknown",
        "other",
    ]
    """The license of the repository.

    You can select 'Other' if your license is not in the list
    """

    license_link: Union[Literal["LICENSE", "LICENSE.md"], str]

    license_name: str

    name: str

    organization: Optional[str]

    private: Optional[bool]
    """Repository visibility. Defaults to public"""

    resource_group_id: Annotated[Optional[str], PropertyInfo(alias="resourceGroupId")]

    sdk_version: Annotated[Optional[str], PropertyInfo(alias="sdkVersion")]

    secrets: Iterable[Variant2Secret]

    short_description: str

    sleep_time_seconds: Annotated[Union[int, Literal[-1]], PropertyInfo(alias="sleepTimeSeconds")]

    storage_tier: Annotated[Optional[Literal["small", "medium", "large"]], PropertyInfo(alias="storageTier")]

    template: str

    variables: Iterable[Variant2Variable]


class Variant2File(TypedDict, total=False):
    content: Required[str]

    path: Required[str]

    encoding: Literal["utf-8", "base64"]


class Variant2Secret(TypedDict, total=False):
    key: Required[str]

    value: Required[str]

    description: str


class Variant2Variable(TypedDict, total=False):
    key: Required[str]

    value: Required[str]

    description: str


RepoCreateParams: TypeAlias = Union[Variant0, Variant1, Variant2]
