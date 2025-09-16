# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, overload

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.api import repo_move_params, repo_create_params
from ..._base_client import make_request_options
from ...types.api.repo_create_response import RepoCreateResponse

__all__ = ["ReposResource", "AsyncReposResource"]


class ReposResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReposResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return ReposResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReposResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return ReposResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        type: Literal["dataset"],
        files: Iterable[repo_create_params.Variant0File] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        license_link: Union[Literal["LICENSE", "LICENSE.md"], str] | NotGiven = NOT_GIVEN,
        license_name: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        organization: Optional[str] | NotGiven = NOT_GIVEN,
        private: Optional[bool] | NotGiven = NOT_GIVEN,
        resource_group_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepoCreateResponse:
        """Create a new repository

        Args:
          license: The license of the repository.

        You can select 'Other' if your license is not in
              the list

          private: Repository visibility. Defaults to public

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        files: Iterable[repo_create_params.Variant1File] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        license_link: Union[Literal["LICENSE", "LICENSE.md"], str] | NotGiven = NOT_GIVEN,
        license_name: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        organization: Optional[str] | NotGiven = NOT_GIVEN,
        private: Optional[bool] | NotGiven = NOT_GIVEN,
        resource_group_id: Optional[str] | NotGiven = NOT_GIVEN,
        type: Literal["model"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepoCreateResponse:
        """Create a new repository

        Args:
          license: The license of the repository.

        You can select 'Other' if your license is not in
              the list

          private: Repository visibility. Defaults to public

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        sdk: Literal["gradio", "docker", "static", "streamlit"],
        type: Literal["space"],
        dev_mode_enabled: bool | NotGiven = NOT_GIVEN,
        files: Iterable[repo_create_params.Variant2File] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        license_link: Union[Literal["LICENSE", "LICENSE.md"], str] | NotGiven = NOT_GIVEN,
        license_name: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        organization: Optional[str] | NotGiven = NOT_GIVEN,
        private: Optional[bool] | NotGiven = NOT_GIVEN,
        resource_group_id: Optional[str] | NotGiven = NOT_GIVEN,
        sdk_version: Optional[str] | NotGiven = NOT_GIVEN,
        secrets: Iterable[repo_create_params.Variant2Secret] | NotGiven = NOT_GIVEN,
        short_description: str | NotGiven = NOT_GIVEN,
        sleep_time_seconds: Union[int, Literal[-1]] | NotGiven = NOT_GIVEN,
        storage_tier: Optional[Literal["small", "medium", "large"]] | NotGiven = NOT_GIVEN,
        template: str | NotGiven = NOT_GIVEN,
        variables: Iterable[repo_create_params.Variant2Variable] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepoCreateResponse:
        """Create a new repository

        Args:
          hardware: The hardware flavor of the space.

        If you select 'zero-a10g' or 'zerogpu', the
              SDK must be Gradio.

          license: The license of the repository. You can select 'Other' if your license is not in
              the list

          private: Repository visibility. Defaults to public

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    def create(
        self,
        *,
        type: Literal["dataset"] | Literal["model"] | Literal["space"] | NotGiven = NOT_GIVEN,
        files: Iterable[repo_create_params.Variant0File]
        | Iterable[repo_create_params.Variant1File]
        | Iterable[repo_create_params.Variant2File]
        | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        license_link: Union[Literal["LICENSE", "LICENSE.md"], str] | NotGiven = NOT_GIVEN,
        license_name: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        organization: Optional[str] | NotGiven = NOT_GIVEN,
        private: Optional[bool] | NotGiven = NOT_GIVEN,
        resource_group_id: Optional[str] | NotGiven = NOT_GIVEN,
        sdk: Literal["gradio", "docker", "static", "streamlit"] | NotGiven = NOT_GIVEN,
        dev_mode_enabled: bool | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        sdk_version: Optional[str] | NotGiven = NOT_GIVEN,
        secrets: Iterable[repo_create_params.Variant2Secret] | NotGiven = NOT_GIVEN,
        short_description: str | NotGiven = NOT_GIVEN,
        sleep_time_seconds: Union[int, Literal[-1]] | NotGiven = NOT_GIVEN,
        storage_tier: Optional[Literal["small", "medium", "large"]] | NotGiven = NOT_GIVEN,
        template: str | NotGiven = NOT_GIVEN,
        variables: Iterable[repo_create_params.Variant2Variable] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepoCreateResponse:
        return self._post(
            "/api/repos/create",
            body=maybe_transform(
                {
                    "type": type,
                    "files": files,
                    "license": license,
                    "license_link": license_link,
                    "license_name": license_name,
                    "name": name,
                    "organization": organization,
                    "private": private,
                    "resource_group_id": resource_group_id,
                    "sdk": sdk,
                    "dev_mode_enabled": dev_mode_enabled,
                    "hardware": hardware,
                    "sdk_version": sdk_version,
                    "secrets": secrets,
                    "short_description": short_description,
                    "sleep_time_seconds": sleep_time_seconds,
                    "storage_tier": storage_tier,
                    "template": template,
                    "variables": variables,
                },
                repo_create_params.RepoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RepoCreateResponse,
        )

    def move(
        self,
        *,
        from_repo: str,
        to_repo: str,
        type: Literal["dataset", "model", "space"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Move or rename a repo.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/api/repos/move",
            body=maybe_transform(
                {
                    "from_repo": from_repo,
                    "to_repo": to_repo,
                    "type": type,
                },
                repo_move_params.RepoMoveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncReposResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReposResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return AsyncReposResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReposResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return AsyncReposResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        type: Literal["dataset"],
        files: Iterable[repo_create_params.Variant0File] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        license_link: Union[Literal["LICENSE", "LICENSE.md"], str] | NotGiven = NOT_GIVEN,
        license_name: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        organization: Optional[str] | NotGiven = NOT_GIVEN,
        private: Optional[bool] | NotGiven = NOT_GIVEN,
        resource_group_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepoCreateResponse:
        """Create a new repository

        Args:
          license: The license of the repository.

        You can select 'Other' if your license is not in
              the list

          private: Repository visibility. Defaults to public

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        files: Iterable[repo_create_params.Variant1File] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        license_link: Union[Literal["LICENSE", "LICENSE.md"], str] | NotGiven = NOT_GIVEN,
        license_name: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        organization: Optional[str] | NotGiven = NOT_GIVEN,
        private: Optional[bool] | NotGiven = NOT_GIVEN,
        resource_group_id: Optional[str] | NotGiven = NOT_GIVEN,
        type: Literal["model"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepoCreateResponse:
        """Create a new repository

        Args:
          license: The license of the repository.

        You can select 'Other' if your license is not in
              the list

          private: Repository visibility. Defaults to public

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        sdk: Literal["gradio", "docker", "static", "streamlit"],
        type: Literal["space"],
        dev_mode_enabled: bool | NotGiven = NOT_GIVEN,
        files: Iterable[repo_create_params.Variant2File] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        license_link: Union[Literal["LICENSE", "LICENSE.md"], str] | NotGiven = NOT_GIVEN,
        license_name: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        organization: Optional[str] | NotGiven = NOT_GIVEN,
        private: Optional[bool] | NotGiven = NOT_GIVEN,
        resource_group_id: Optional[str] | NotGiven = NOT_GIVEN,
        sdk_version: Optional[str] | NotGiven = NOT_GIVEN,
        secrets: Iterable[repo_create_params.Variant2Secret] | NotGiven = NOT_GIVEN,
        short_description: str | NotGiven = NOT_GIVEN,
        sleep_time_seconds: Union[int, Literal[-1]] | NotGiven = NOT_GIVEN,
        storage_tier: Optional[Literal["small", "medium", "large"]] | NotGiven = NOT_GIVEN,
        template: str | NotGiven = NOT_GIVEN,
        variables: Iterable[repo_create_params.Variant2Variable] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepoCreateResponse:
        """Create a new repository

        Args:
          hardware: The hardware flavor of the space.

        If you select 'zero-a10g' or 'zerogpu', the
              SDK must be Gradio.

          license: The license of the repository. You can select 'Other' if your license is not in
              the list

          private: Repository visibility. Defaults to public

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    async def create(
        self,
        *,
        type: Literal["dataset"] | Literal["model"] | Literal["space"] | NotGiven = NOT_GIVEN,
        files: Iterable[repo_create_params.Variant0File]
        | Iterable[repo_create_params.Variant1File]
        | Iterable[repo_create_params.Variant2File]
        | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        license_link: Union[Literal["LICENSE", "LICENSE.md"], str] | NotGiven = NOT_GIVEN,
        license_name: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        organization: Optional[str] | NotGiven = NOT_GIVEN,
        private: Optional[bool] | NotGiven = NOT_GIVEN,
        resource_group_id: Optional[str] | NotGiven = NOT_GIVEN,
        sdk: Literal["gradio", "docker", "static", "streamlit"] | NotGiven = NOT_GIVEN,
        dev_mode_enabled: bool | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        sdk_version: Optional[str] | NotGiven = NOT_GIVEN,
        secrets: Iterable[repo_create_params.Variant2Secret] | NotGiven = NOT_GIVEN,
        short_description: str | NotGiven = NOT_GIVEN,
        sleep_time_seconds: Union[int, Literal[-1]] | NotGiven = NOT_GIVEN,
        storage_tier: Optional[Literal["small", "medium", "large"]] | NotGiven = NOT_GIVEN,
        template: str | NotGiven = NOT_GIVEN,
        variables: Iterable[repo_create_params.Variant2Variable] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepoCreateResponse:
        return await self._post(
            "/api/repos/create",
            body=await async_maybe_transform(
                {
                    "type": type,
                    "files": files,
                    "license": license,
                    "license_link": license_link,
                    "license_name": license_name,
                    "name": name,
                    "organization": organization,
                    "private": private,
                    "resource_group_id": resource_group_id,
                    "sdk": sdk,
                    "dev_mode_enabled": dev_mode_enabled,
                    "hardware": hardware,
                    "sdk_version": sdk_version,
                    "secrets": secrets,
                    "short_description": short_description,
                    "sleep_time_seconds": sleep_time_seconds,
                    "storage_tier": storage_tier,
                    "template": template,
                    "variables": variables,
                },
                repo_create_params.RepoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RepoCreateResponse,
        )

    async def move(
        self,
        *,
        from_repo: str,
        to_repo: str,
        type: Literal["dataset", "model", "space"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Move or rename a repo.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/api/repos/move",
            body=await async_maybe_transform(
                {
                    "from_repo": from_repo,
                    "to_repo": to_repo,
                    "type": type,
                },
                repo_move_params.RepoMoveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ReposResourceWithRawResponse:
    def __init__(self, repos: ReposResource) -> None:
        self._repos = repos

        self.create = to_raw_response_wrapper(
            repos.create,
        )
        self.move = to_raw_response_wrapper(
            repos.move,
        )


class AsyncReposResourceWithRawResponse:
    def __init__(self, repos: AsyncReposResource) -> None:
        self._repos = repos

        self.create = async_to_raw_response_wrapper(
            repos.create,
        )
        self.move = async_to_raw_response_wrapper(
            repos.move,
        )


class ReposResourceWithStreamingResponse:
    def __init__(self, repos: ReposResource) -> None:
        self._repos = repos

        self.create = to_streamed_response_wrapper(
            repos.create,
        )
        self.move = to_streamed_response_wrapper(
            repos.move,
        )


class AsyncReposResourceWithStreamingResponse:
    def __init__(self, repos: AsyncReposResource) -> None:
        self._repos = repos

        self.create = async_to_streamed_response_wrapper(
            repos.create,
        )
        self.move = async_to_streamed_response_wrapper(
            repos.move,
        )
