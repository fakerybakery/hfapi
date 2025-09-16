# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.api.posts import comment_reply_params, comment_create_params
from ....types.api.posts.comment_reply_response import CommentReplyResponse
from ....types.api.posts.comment_create_response import CommentCreateResponse

__all__ = ["CommentResource", "AsyncCommentResource"]


class CommentResource(SyncAPIResource):
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
        post_slug: str,
        *,
        username: str,
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
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        if not post_slug:
            raise ValueError(f"Expected a non-empty value for `post_slug` but received {post_slug!r}")
        return self._post(
            f"/api/posts/{username}/{post_slug}/comment",
            body=maybe_transform({"comment": comment}, comment_create_params.CommentCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommentCreateResponse,
        )

    def reply(
        self,
        comment_id: str,
        *,
        username: str,
        post_slug: str,
        comment: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommentReplyResponse:
        """
        Create a new comment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        if not post_slug:
            raise ValueError(f"Expected a non-empty value for `post_slug` but received {post_slug!r}")
        if not comment_id:
            raise ValueError(f"Expected a non-empty value for `comment_id` but received {comment_id!r}")
        return self._post(
            f"/api/posts/{username}/{post_slug}/comment/{comment_id}/reply",
            body=maybe_transform({"comment": comment}, comment_reply_params.CommentReplyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommentReplyResponse,
        )


class AsyncCommentResource(AsyncAPIResource):
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
        post_slug: str,
        *,
        username: str,
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
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        if not post_slug:
            raise ValueError(f"Expected a non-empty value for `post_slug` but received {post_slug!r}")
        return await self._post(
            f"/api/posts/{username}/{post_slug}/comment",
            body=await async_maybe_transform({"comment": comment}, comment_create_params.CommentCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommentCreateResponse,
        )

    async def reply(
        self,
        comment_id: str,
        *,
        username: str,
        post_slug: str,
        comment: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommentReplyResponse:
        """
        Create a new comment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        if not post_slug:
            raise ValueError(f"Expected a non-empty value for `post_slug` but received {post_slug!r}")
        if not comment_id:
            raise ValueError(f"Expected a non-empty value for `comment_id` but received {comment_id!r}")
        return await self._post(
            f"/api/posts/{username}/{post_slug}/comment/{comment_id}/reply",
            body=await async_maybe_transform({"comment": comment}, comment_reply_params.CommentReplyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommentReplyResponse,
        )


class CommentResourceWithRawResponse:
    def __init__(self, comment: CommentResource) -> None:
        self._comment = comment

        self.create = to_raw_response_wrapper(
            comment.create,
        )
        self.reply = to_raw_response_wrapper(
            comment.reply,
        )


class AsyncCommentResourceWithRawResponse:
    def __init__(self, comment: AsyncCommentResource) -> None:
        self._comment = comment

        self.create = async_to_raw_response_wrapper(
            comment.create,
        )
        self.reply = async_to_raw_response_wrapper(
            comment.reply,
        )


class CommentResourceWithStreamingResponse:
    def __init__(self, comment: CommentResource) -> None:
        self._comment = comment

        self.create = to_streamed_response_wrapper(
            comment.create,
        )
        self.reply = to_streamed_response_wrapper(
            comment.reply,
        )


class AsyncCommentResourceWithStreamingResponse:
    def __init__(self, comment: AsyncCommentResource) -> None:
        self._comment = comment

        self.create = async_to_streamed_response_wrapper(
            comment.create,
        )
        self.reply = async_to_streamed_response_wrapper(
            comment.reply,
        )
