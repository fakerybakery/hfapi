# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["UserAccessReportResource", "AsyncUserAccessReportResource"]


class UserAccessReportResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UserAccessReportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return UserAccessReportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserAccessReportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return UserAccessReportResourceWithStreamingResponse(self)

    def export(
        self,
        repo: str,
        *,
        namespace: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Export a report of all access requests for a gated repository

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._get(
            f"/{namespace}/{repo}/user-access-report",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncUserAccessReportResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUserAccessReportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return AsyncUserAccessReportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserAccessReportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return AsyncUserAccessReportResourceWithStreamingResponse(self)

    async def export(
        self,
        repo: str,
        *,
        namespace: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Export a report of all access requests for a gated repository

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._get(
            f"/{namespace}/{repo}/user-access-report",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class UserAccessReportResourceWithRawResponse:
    def __init__(self, user_access_report: UserAccessReportResource) -> None:
        self._user_access_report = user_access_report

        self.export = to_raw_response_wrapper(
            user_access_report.export,
        )


class AsyncUserAccessReportResourceWithRawResponse:
    def __init__(self, user_access_report: AsyncUserAccessReportResource) -> None:
        self._user_access_report = user_access_report

        self.export = async_to_raw_response_wrapper(
            user_access_report.export,
        )


class UserAccessReportResourceWithStreamingResponse:
    def __init__(self, user_access_report: UserAccessReportResource) -> None:
        self._user_access_report = user_access_report

        self.export = to_streamed_response_wrapper(
            user_access_report.export,
        )


class AsyncUserAccessReportResourceWithStreamingResponse:
    def __init__(self, user_access_report: AsyncUserAccessReportResource) -> None:
        self._user_access_report = user_access_report

        self.export = async_to_streamed_response_wrapper(
            user_access_report.export,
        )
