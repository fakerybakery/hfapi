# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.api.blog.comment import reply_create_params, reply_create_with_namespace_params
from .....types.api.blog.comment.reply_create_response import ReplyCreateResponse
from .....types.api.blog.comment.reply_create_with_namespace_response import ReplyCreateWithNamespaceResponse

__all__ = ["ReplyResource", "AsyncReplyResource"]


class ReplyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReplyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return ReplyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReplyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return ReplyResourceWithStreamingResponse(self)

    def create(
        self,
        comment_id: str,
        *,
        slug: str,
        comment: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReplyCreateResponse:
        """
        Create a new comment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if not comment_id:
            raise ValueError(f"Expected a non-empty value for `comment_id` but received {comment_id!r}")
        return self._post(
            f"/api/blog/{slug}/comment/{comment_id}/reply",
            body=maybe_transform({"comment": comment}, reply_create_params.ReplyCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReplyCreateResponse,
        )

    def create_with_namespace(
        self,
        comment_id: str,
        *,
        namespace: str,
        slug: str,
        comment: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReplyCreateWithNamespaceResponse:
        """
        Create a new comment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if not comment_id:
            raise ValueError(f"Expected a non-empty value for `comment_id` but received {comment_id!r}")
        return self._post(
            f"/api/blog/{namespace}/{slug}/comment/{comment_id}/reply",
            body=maybe_transform(
                {"comment": comment}, reply_create_with_namespace_params.ReplyCreateWithNamespaceParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReplyCreateWithNamespaceResponse,
        )


class AsyncReplyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReplyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return AsyncReplyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReplyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return AsyncReplyResourceWithStreamingResponse(self)

    async def create(
        self,
        comment_id: str,
        *,
        slug: str,
        comment: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReplyCreateResponse:
        """
        Create a new comment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if not comment_id:
            raise ValueError(f"Expected a non-empty value for `comment_id` but received {comment_id!r}")
        return await self._post(
            f"/api/blog/{slug}/comment/{comment_id}/reply",
            body=await async_maybe_transform({"comment": comment}, reply_create_params.ReplyCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReplyCreateResponse,
        )

    async def create_with_namespace(
        self,
        comment_id: str,
        *,
        namespace: str,
        slug: str,
        comment: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReplyCreateWithNamespaceResponse:
        """
        Create a new comment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if not comment_id:
            raise ValueError(f"Expected a non-empty value for `comment_id` but received {comment_id!r}")
        return await self._post(
            f"/api/blog/{namespace}/{slug}/comment/{comment_id}/reply",
            body=await async_maybe_transform(
                {"comment": comment}, reply_create_with_namespace_params.ReplyCreateWithNamespaceParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReplyCreateWithNamespaceResponse,
        )


class ReplyResourceWithRawResponse:
    def __init__(self, reply: ReplyResource) -> None:
        self._reply = reply

        self.create = to_raw_response_wrapper(
            reply.create,
        )
        self.create_with_namespace = to_raw_response_wrapper(
            reply.create_with_namespace,
        )


class AsyncReplyResourceWithRawResponse:
    def __init__(self, reply: AsyncReplyResource) -> None:
        self._reply = reply

        self.create = async_to_raw_response_wrapper(
            reply.create,
        )
        self.create_with_namespace = async_to_raw_response_wrapper(
            reply.create_with_namespace,
        )


class ReplyResourceWithStreamingResponse:
    def __init__(self, reply: ReplyResource) -> None:
        self._reply = reply

        self.create = to_streamed_response_wrapper(
            reply.create,
        )
        self.create_with_namespace = to_streamed_response_wrapper(
            reply.create_with_namespace,
        )


class AsyncReplyResourceWithStreamingResponse:
    def __init__(self, reply: AsyncReplyResource) -> None:
        self._reply = reply

        self.create = async_to_streamed_response_wrapper(
            reply.create,
        )
        self.create_with_namespace = async_to_streamed_response_wrapper(
            reply.create_with_namespace,
        )
