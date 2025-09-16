# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .reply import (
    ReplyResource,
    AsyncReplyResource,
    ReplyResourceWithRawResponse,
    AsyncReplyResourceWithRawResponse,
    ReplyResourceWithStreamingResponse,
    AsyncReplyResourceWithStreamingResponse,
)
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
from .....types.api.blog import comment_create_params, comment_create_with_namespace_params
from .....types.api.blog.comment_create_response import CommentCreateResponse
from .....types.api.blog.comment_create_with_namespace_response import CommentCreateWithNamespaceResponse

__all__ = ["CommentResource", "AsyncCommentResource"]


class CommentResource(SyncAPIResource):
    @cached_property
    def reply(self) -> ReplyResource:
        return ReplyResource(self._client)

    @cached_property
    def with_raw_response(self) -> CommentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return CommentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CommentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return CommentResourceWithStreamingResponse(self)

    def create(
        self,
        slug: str,
        *,
        comment: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommentCreateResponse:
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
        return self._post(
            f"/api/blog/{slug}/comment",
            body=maybe_transform({"comment": comment}, comment_create_params.CommentCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommentCreateResponse,
        )

    def create_with_namespace(
        self,
        slug: str,
        *,
        namespace: str,
        comment: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommentCreateWithNamespaceResponse:
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
        return self._post(
            f"/api/blog/{namespace}/{slug}/comment",
            body=maybe_transform(
                {"comment": comment}, comment_create_with_namespace_params.CommentCreateWithNamespaceParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommentCreateWithNamespaceResponse,
        )


class AsyncCommentResource(AsyncAPIResource):
    @cached_property
    def reply(self) -> AsyncReplyResource:
        return AsyncReplyResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCommentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return AsyncCommentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCommentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return AsyncCommentResourceWithStreamingResponse(self)

    async def create(
        self,
        slug: str,
        *,
        comment: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommentCreateResponse:
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
        return await self._post(
            f"/api/blog/{slug}/comment",
            body=await async_maybe_transform({"comment": comment}, comment_create_params.CommentCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommentCreateResponse,
        )

    async def create_with_namespace(
        self,
        slug: str,
        *,
        namespace: str,
        comment: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommentCreateWithNamespaceResponse:
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
        return await self._post(
            f"/api/blog/{namespace}/{slug}/comment",
            body=await async_maybe_transform(
                {"comment": comment}, comment_create_with_namespace_params.CommentCreateWithNamespaceParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommentCreateWithNamespaceResponse,
        )


class CommentResourceWithRawResponse:
    def __init__(self, comment: CommentResource) -> None:
        self._comment = comment

        self.create = to_raw_response_wrapper(
            comment.create,
        )
        self.create_with_namespace = to_raw_response_wrapper(
            comment.create_with_namespace,
        )

    @cached_property
    def reply(self) -> ReplyResourceWithRawResponse:
        return ReplyResourceWithRawResponse(self._comment.reply)


class AsyncCommentResourceWithRawResponse:
    def __init__(self, comment: AsyncCommentResource) -> None:
        self._comment = comment

        self.create = async_to_raw_response_wrapper(
            comment.create,
        )
        self.create_with_namespace = async_to_raw_response_wrapper(
            comment.create_with_namespace,
        )

    @cached_property
    def reply(self) -> AsyncReplyResourceWithRawResponse:
        return AsyncReplyResourceWithRawResponse(self._comment.reply)


class CommentResourceWithStreamingResponse:
    def __init__(self, comment: CommentResource) -> None:
        self._comment = comment

        self.create = to_streamed_response_wrapper(
            comment.create,
        )
        self.create_with_namespace = to_streamed_response_wrapper(
            comment.create_with_namespace,
        )

    @cached_property
    def reply(self) -> ReplyResourceWithStreamingResponse:
        return ReplyResourceWithStreamingResponse(self._comment.reply)


class AsyncCommentResourceWithStreamingResponse:
    def __init__(self, comment: AsyncCommentResource) -> None:
        self._comment = comment

        self.create = async_to_streamed_response_wrapper(
            comment.create,
        )
        self.create_with_namespace = async_to_streamed_response_wrapper(
            comment.create_with_namespace,
        )

    @cached_property
    def reply(self) -> AsyncReplyResourceWithStreamingResponse:
        return AsyncReplyResourceWithStreamingResponse(self._comment.reply)
