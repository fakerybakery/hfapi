# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..types import ask_access_request_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["AskAccessResource", "AsyncAskAccessResource"]


class AskAccessResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AskAccessResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return AskAccessResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AskAccessResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return AskAccessResourceWithStreamingResponse(self)

    def request(
        self,
        repo: str,
        *,
        namespace: str,
        body: Dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        The fields requested by repository card metadata
        (https://huggingface.co/docs/hub/en/models-gated#customize-requested-information)

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/{namespace}/{repo}/ask-access",
            body=maybe_transform(body, ask_access_request_params.AskAccessRequestParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAskAccessResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAskAccessResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return AsyncAskAccessResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAskAccessResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return AsyncAskAccessResourceWithStreamingResponse(self)

    async def request(
        self,
        repo: str,
        *,
        namespace: str,
        body: Dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        The fields requested by repository card metadata
        (https://huggingface.co/docs/hub/en/models-gated#customize-requested-information)

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/{namespace}/{repo}/ask-access",
            body=await async_maybe_transform(body, ask_access_request_params.AskAccessRequestParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AskAccessResourceWithRawResponse:
    def __init__(self, ask_access: AskAccessResource) -> None:
        self._ask_access = ask_access

        self.request = to_raw_response_wrapper(
            ask_access.request,
        )


class AsyncAskAccessResourceWithRawResponse:
    def __init__(self, ask_access: AsyncAskAccessResource) -> None:
        self._ask_access = ask_access

        self.request = async_to_raw_response_wrapper(
            ask_access.request,
        )


class AskAccessResourceWithStreamingResponse:
    def __init__(self, ask_access: AskAccessResource) -> None:
        self._ask_access = ask_access

        self.request = to_streamed_response_wrapper(
            ask_access.request,
        )


class AsyncAskAccessResourceWithStreamingResponse:
    def __init__(self, ask_access: AsyncAskAccessResource) -> None:
        self._ask_access = ask_access

        self.request = async_to_streamed_response_wrapper(
            ask_access.request,
        )
