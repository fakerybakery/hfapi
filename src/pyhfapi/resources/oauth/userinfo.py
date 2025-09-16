# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.oauth.userinfo_update_response import UserinfoUpdateResponse
from ...types.oauth.userinfo_retrieve_response import UserinfoRetrieveResponse

__all__ = ["UserinfoResource", "AsyncUserinfoResource"]


class UserinfoResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UserinfoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return UserinfoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserinfoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return UserinfoResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserinfoRetrieveResponse:
        """Get information about the user.

        Only available through oauth access tokens.
        Information varies depending on the scope of the oauth app and what permissions
        the user granted to the oauth app.
        """
        return self._get(
            "/oauth/userinfo",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserinfoRetrieveResponse,
        )

    def update(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserinfoUpdateResponse:
        """Get information about the user.

        Only available through oauth access tokens.
        Information varies depending on the scope of the oauth app and what permissions
        the user granted to the oauth app.
        """
        return self._post(
            "/oauth/userinfo",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserinfoUpdateResponse,
        )


class AsyncUserinfoResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUserinfoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return AsyncUserinfoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserinfoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return AsyncUserinfoResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserinfoRetrieveResponse:
        """Get information about the user.

        Only available through oauth access tokens.
        Information varies depending on the scope of the oauth app and what permissions
        the user granted to the oauth app.
        """
        return await self._get(
            "/oauth/userinfo",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserinfoRetrieveResponse,
        )

    async def update(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserinfoUpdateResponse:
        """Get information about the user.

        Only available through oauth access tokens.
        Information varies depending on the scope of the oauth app and what permissions
        the user granted to the oauth app.
        """
        return await self._post(
            "/oauth/userinfo",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserinfoUpdateResponse,
        )


class UserinfoResourceWithRawResponse:
    def __init__(self, userinfo: UserinfoResource) -> None:
        self._userinfo = userinfo

        self.retrieve = to_raw_response_wrapper(
            userinfo.retrieve,
        )
        self.update = to_raw_response_wrapper(
            userinfo.update,
        )


class AsyncUserinfoResourceWithRawResponse:
    def __init__(self, userinfo: AsyncUserinfoResource) -> None:
        self._userinfo = userinfo

        self.retrieve = async_to_raw_response_wrapper(
            userinfo.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            userinfo.update,
        )


class UserinfoResourceWithStreamingResponse:
    def __init__(self, userinfo: UserinfoResource) -> None:
        self._userinfo = userinfo

        self.retrieve = to_streamed_response_wrapper(
            userinfo.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            userinfo.update,
        )


class AsyncUserinfoResourceWithStreamingResponse:
    def __init__(self, userinfo: AsyncUserinfoResource) -> None:
        self._userinfo = userinfo

        self.retrieve = async_to_streamed_response_wrapper(
            userinfo.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            userinfo.update,
        )
