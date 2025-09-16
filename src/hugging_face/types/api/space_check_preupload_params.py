# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SpaceCheckPreuploadParams", "File"]


class SpaceCheckPreuploadParams(TypedDict, total=False):
    namespace: Required[str]

    repo: Required[str]

    files: Required[Iterable[File]]

    git_attributes: Annotated[str, PropertyInfo(alias="gitAttributes")]
    """
    Provide this parameter if you plan to modify `.gitattributes` yourself at the
    same time as uploading LFS files. Note that this is not needed if you solely
    rely on automatic LFS detection from HF: the commit endpoint will automatically
    edit the `.gitattributes` file to track the files passed to its `lfsFiles`
    param.
    """

    git_ignore: Annotated[str, PropertyInfo(alias="gitIgnore")]
    """Content of the .gitignore file for the revision.

    Optional, otherwise takes the existing content of `.gitignore` for the revision.
    """


class File(TypedDict, total=False):
    path: Required[str]

    sample: Required[str]

    size: Required[float]
