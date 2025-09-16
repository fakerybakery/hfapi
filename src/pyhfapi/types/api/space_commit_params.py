# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SpaceCommitParams"]


class SpaceCommitParams(TypedDict, total=False):
    namespace: Required[str]

    repo: Required[str]

    create_pr: object
    """Whether to create a pull request from the commit"""
