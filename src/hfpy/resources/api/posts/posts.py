# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .comment import (
    CommentResource,
    AsyncCommentResource,
    CommentResourceWithRawResponse,
    AsyncCommentResourceWithRawResponse,
    CommentResourceWithStreamingResponse,
    AsyncCommentResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options

__all__ = ["PostsResource", "AsyncPostsResource"]


class PostsResource(SyncAPIResource):
    @cached_property
    def comment(self) -> CommentResource:
        return CommentResource(self._client)

    @cached_property
    def with_raw_response(self) -> PostsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return PostsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PostsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return PostsResourceWithStreamingResponse(self)

    def delete(
        self,
        post_slug: str,
        *,
        username: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a discussion

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/posts/{username}/{post_slug}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncPostsResource(AsyncAPIResource):
    @cached_property
    def comment(self) -> AsyncCommentResource:
        return AsyncCommentResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPostsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return AsyncPostsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPostsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return AsyncPostsResourceWithStreamingResponse(self)

    async def delete(
        self,
        post_slug: str,
        *,
        username: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a discussion

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/posts/{username}/{post_slug}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class PostsResourceWithRawResponse:
    def __init__(self, posts: PostsResource) -> None:
        self._posts = posts

        self.delete = to_raw_response_wrapper(
            posts.delete,
        )

    @cached_property
    def comment(self) -> CommentResourceWithRawResponse:
        return CommentResourceWithRawResponse(self._posts.comment)


class AsyncPostsResourceWithRawResponse:
    def __init__(self, posts: AsyncPostsResource) -> None:
        self._posts = posts

        self.delete = async_to_raw_response_wrapper(
            posts.delete,
        )

    @cached_property
    def comment(self) -> AsyncCommentResourceWithRawResponse:
        return AsyncCommentResourceWithRawResponse(self._posts.comment)


class PostsResourceWithStreamingResponse:
    def __init__(self, posts: PostsResource) -> None:
        self._posts = posts

        self.delete = to_streamed_response_wrapper(
            posts.delete,
        )

    @cached_property
    def comment(self) -> CommentResourceWithStreamingResponse:
        return CommentResourceWithStreamingResponse(self._posts.comment)


class AsyncPostsResourceWithStreamingResponse:
    def __init__(self, posts: AsyncPostsResource) -> None:
        self._posts = posts

        self.delete = async_to_streamed_response_wrapper(
            posts.delete,
        )

    @cached_property
    def comment(self) -> AsyncCommentResourceWithStreamingResponse:
        return AsyncCommentResourceWithStreamingResponse(self._posts.comment)
