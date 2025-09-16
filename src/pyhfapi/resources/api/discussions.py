# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven, SequenceNotStr
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.api import (
    discussion_pin_params,
    discussion_list_params,
    discussion_merge_params,
    discussion_create_params,
    discussion_add_comment_params,
    discussion_change_title_params,
    discussion_mark_as_read_params,
    discussion_change_status_params,
)
from ..._base_client import make_request_options
from ...types.api.discussion_list_response import DiscussionListResponse
from ...types.api.discussion_create_response import DiscussionCreateResponse
from ...types.api.discussion_retrieve_response import DiscussionRetrieveResponse
from ...types.api.discussion_add_comment_response import DiscussionAddCommentResponse
from ...types.api.discussion_change_title_response import DiscussionChangeTitleResponse
from ...types.api.discussion_change_status_response import DiscussionChangeStatusResponse

__all__ = ["DiscussionsResource", "AsyncDiscussionsResource"]


class DiscussionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DiscussionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return DiscussionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DiscussionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return DiscussionsResourceWithStreamingResponse(self)

    def create(
        self,
        repo: str,
        *,
        repo_type: Literal["models", "spaces", "datasets"],
        namespace: str,
        description: str,
        title: str,
        pull_request: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DiscussionCreateResponse:
        """
        Create a new discussion

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not repo_type:
            raise ValueError(f"Expected a non-empty value for `repo_type` but received {repo_type!r}")
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._post(
            f"/api/{repo_type}/{namespace}/{repo}/discussions",
            body=maybe_transform(
                {
                    "description": description,
                    "title": title,
                    "pull_request": pull_request,
                },
                discussion_create_params.DiscussionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DiscussionCreateResponse,
        )

    def retrieve(
        self,
        num: str,
        *,
        repo_type: Literal["models", "spaces", "datasets"],
        namespace: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DiscussionRetrieveResponse:
        """
        Get discussion details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not repo_type:
            raise ValueError(f"Expected a non-empty value for `repo_type` but received {repo_type!r}")
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not num:
            raise ValueError(f"Expected a non-empty value for `num` but received {num!r}")
        return cast(
            DiscussionRetrieveResponse,
            self._get(
                f"/api/{repo_type}/{namespace}/{repo}/discussions/{num}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, DiscussionRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        repo: str,
        *,
        repo_type: Literal["models", "spaces", "datasets"],
        namespace: str,
        author: str | NotGiven = NOT_GIVEN,
        p: int | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        sort: Literal["recently-created", "trending", "reactions"] | NotGiven = NOT_GIVEN,
        status: Literal["all", "open", "closed"] | NotGiven = NOT_GIVEN,
        type: Literal["all", "discussion", "pull_request"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DiscussionListResponse:
        """
        Get discussions for a repo

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not repo_type:
            raise ValueError(f"Expected a non-empty value for `repo_type` but received {repo_type!r}")
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._get(
            f"/api/{repo_type}/{namespace}/{repo}/discussions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "author": author,
                        "p": p,
                        "search": search,
                        "sort": sort,
                        "status": status,
                        "type": type,
                    },
                    discussion_list_params.DiscussionListParams,
                ),
            ),
            cast_to=DiscussionListResponse,
        )

    def delete(
        self,
        num: str,
        *,
        repo_type: Literal["models", "spaces", "datasets"],
        namespace: str,
        repo: str,
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
        if not repo_type:
            raise ValueError(f"Expected a non-empty value for `repo_type` but received {repo_type!r}")
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not num:
            raise ValueError(f"Expected a non-empty value for `num` but received {num!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/{repo_type}/{namespace}/{repo}/discussions/{num}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def add_comment(
        self,
        num: str,
        *,
        repo_type: Literal["models", "spaces", "datasets"],
        namespace: str,
        repo: str,
        comment: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DiscussionAddCommentResponse:
        """
        Create a new comment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not repo_type:
            raise ValueError(f"Expected a non-empty value for `repo_type` but received {repo_type!r}")
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not num:
            raise ValueError(f"Expected a non-empty value for `num` but received {num!r}")
        return self._post(
            f"/api/{repo_type}/{namespace}/{repo}/discussions/{num}/comment",
            body=maybe_transform({"comment": comment}, discussion_add_comment_params.DiscussionAddCommentParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DiscussionAddCommentResponse,
        )

    def change_status(
        self,
        num: str,
        *,
        repo_type: Literal["models", "spaces", "datasets"],
        namespace: str,
        repo: str,
        status: Literal["open", "closed"],
        comment: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DiscussionChangeStatusResponse:
        """
        Change the status of a discussion

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not repo_type:
            raise ValueError(f"Expected a non-empty value for `repo_type` but received {repo_type!r}")
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not num:
            raise ValueError(f"Expected a non-empty value for `num` but received {num!r}")
        return self._post(
            f"/api/{repo_type}/{namespace}/{repo}/discussions/{num}/status",
            body=maybe_transform(
                {
                    "status": status,
                    "comment": comment,
                },
                discussion_change_status_params.DiscussionChangeStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DiscussionChangeStatusResponse,
        )

    def change_title(
        self,
        num: str,
        *,
        repo_type: Literal["models", "spaces", "datasets"],
        namespace: str,
        repo: str,
        title: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DiscussionChangeTitleResponse:
        """
        Change the title of a discussion

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not repo_type:
            raise ValueError(f"Expected a non-empty value for `repo_type` but received {repo_type!r}")
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not num:
            raise ValueError(f"Expected a non-empty value for `num` but received {num!r}")
        return self._post(
            f"/api/{repo_type}/{namespace}/{repo}/discussions/{num}/title",
            body=maybe_transform({"title": title}, discussion_change_title_params.DiscussionChangeTitleParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DiscussionChangeTitleResponse,
        )

    def mark_as_read(
        self,
        *,
        apply_to_all: object | NotGiven = NOT_GIVEN,
        article_id: str | NotGiven = NOT_GIVEN,
        last_update: Union[str, datetime] | NotGiven = NOT_GIVEN,
        mention: Literal["all", "participating", "mentions"] | NotGiven = NOT_GIVEN,
        p: int | NotGiven = NOT_GIVEN,
        paper_id: str | NotGiven = NOT_GIVEN,
        post_author: str | NotGiven = NOT_GIVEN,
        read_status: Literal["all", "unread"] | NotGiven = NOT_GIVEN,
        repo_name: str | NotGiven = NOT_GIVEN,
        repo_type: Literal["dataset", "model", "space"] | NotGiven = NOT_GIVEN,
        discussion_ids: SequenceNotStr[str] | NotGiven = NOT_GIVEN,
        read: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Mark discussions as read or unread.

        If `applyToAll` is true, all notifications
        for the user matching the search parameters will be marked as read or unread.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/api/discussions/mark-as-read",
            body=maybe_transform(
                {
                    "discussion_ids": discussion_ids,
                    "read": read,
                },
                discussion_mark_as_read_params.DiscussionMarkAsReadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "apply_to_all": apply_to_all,
                        "article_id": article_id,
                        "last_update": last_update,
                        "mention": mention,
                        "p": p,
                        "paper_id": paper_id,
                        "post_author": post_author,
                        "read_status": read_status,
                        "repo_name": repo_name,
                        "repo_type": repo_type,
                    },
                    discussion_mark_as_read_params.DiscussionMarkAsReadParams,
                ),
            ),
            cast_to=NoneType,
        )

    def merge(
        self,
        num: str,
        *,
        repo_type: Literal["models", "spaces", "datasets"],
        namespace: str,
        repo: str,
        comment: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Merge a pull request

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not repo_type:
            raise ValueError(f"Expected a non-empty value for `repo_type` but received {repo_type!r}")
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not num:
            raise ValueError(f"Expected a non-empty value for `num` but received {num!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/api/{repo_type}/{namespace}/{repo}/discussions/{num}/merge",
            body=maybe_transform({"comment": comment}, discussion_merge_params.DiscussionMergeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def pin(
        self,
        num: str,
        *,
        repo_type: Literal["models", "spaces", "datasets"],
        namespace: str,
        repo: str,
        pinned: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Pin a discussion

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not repo_type:
            raise ValueError(f"Expected a non-empty value for `repo_type` but received {repo_type!r}")
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not num:
            raise ValueError(f"Expected a non-empty value for `num` but received {num!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/api/{repo_type}/{namespace}/{repo}/discussions/{num}/pin",
            body=maybe_transform({"pinned": pinned}, discussion_pin_params.DiscussionPinParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncDiscussionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDiscussionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return AsyncDiscussionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDiscussionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return AsyncDiscussionsResourceWithStreamingResponse(self)

    async def create(
        self,
        repo: str,
        *,
        repo_type: Literal["models", "spaces", "datasets"],
        namespace: str,
        description: str,
        title: str,
        pull_request: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DiscussionCreateResponse:
        """
        Create a new discussion

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not repo_type:
            raise ValueError(f"Expected a non-empty value for `repo_type` but received {repo_type!r}")
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._post(
            f"/api/{repo_type}/{namespace}/{repo}/discussions",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "title": title,
                    "pull_request": pull_request,
                },
                discussion_create_params.DiscussionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DiscussionCreateResponse,
        )

    async def retrieve(
        self,
        num: str,
        *,
        repo_type: Literal["models", "spaces", "datasets"],
        namespace: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DiscussionRetrieveResponse:
        """
        Get discussion details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not repo_type:
            raise ValueError(f"Expected a non-empty value for `repo_type` but received {repo_type!r}")
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not num:
            raise ValueError(f"Expected a non-empty value for `num` but received {num!r}")
        return cast(
            DiscussionRetrieveResponse,
            await self._get(
                f"/api/{repo_type}/{namespace}/{repo}/discussions/{num}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, DiscussionRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def list(
        self,
        repo: str,
        *,
        repo_type: Literal["models", "spaces", "datasets"],
        namespace: str,
        author: str | NotGiven = NOT_GIVEN,
        p: int | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        sort: Literal["recently-created", "trending", "reactions"] | NotGiven = NOT_GIVEN,
        status: Literal["all", "open", "closed"] | NotGiven = NOT_GIVEN,
        type: Literal["all", "discussion", "pull_request"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DiscussionListResponse:
        """
        Get discussions for a repo

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not repo_type:
            raise ValueError(f"Expected a non-empty value for `repo_type` but received {repo_type!r}")
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._get(
            f"/api/{repo_type}/{namespace}/{repo}/discussions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "author": author,
                        "p": p,
                        "search": search,
                        "sort": sort,
                        "status": status,
                        "type": type,
                    },
                    discussion_list_params.DiscussionListParams,
                ),
            ),
            cast_to=DiscussionListResponse,
        )

    async def delete(
        self,
        num: str,
        *,
        repo_type: Literal["models", "spaces", "datasets"],
        namespace: str,
        repo: str,
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
        if not repo_type:
            raise ValueError(f"Expected a non-empty value for `repo_type` but received {repo_type!r}")
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not num:
            raise ValueError(f"Expected a non-empty value for `num` but received {num!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/{repo_type}/{namespace}/{repo}/discussions/{num}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def add_comment(
        self,
        num: str,
        *,
        repo_type: Literal["models", "spaces", "datasets"],
        namespace: str,
        repo: str,
        comment: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DiscussionAddCommentResponse:
        """
        Create a new comment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not repo_type:
            raise ValueError(f"Expected a non-empty value for `repo_type` but received {repo_type!r}")
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not num:
            raise ValueError(f"Expected a non-empty value for `num` but received {num!r}")
        return await self._post(
            f"/api/{repo_type}/{namespace}/{repo}/discussions/{num}/comment",
            body=await async_maybe_transform(
                {"comment": comment}, discussion_add_comment_params.DiscussionAddCommentParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DiscussionAddCommentResponse,
        )

    async def change_status(
        self,
        num: str,
        *,
        repo_type: Literal["models", "spaces", "datasets"],
        namespace: str,
        repo: str,
        status: Literal["open", "closed"],
        comment: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DiscussionChangeStatusResponse:
        """
        Change the status of a discussion

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not repo_type:
            raise ValueError(f"Expected a non-empty value for `repo_type` but received {repo_type!r}")
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not num:
            raise ValueError(f"Expected a non-empty value for `num` but received {num!r}")
        return await self._post(
            f"/api/{repo_type}/{namespace}/{repo}/discussions/{num}/status",
            body=await async_maybe_transform(
                {
                    "status": status,
                    "comment": comment,
                },
                discussion_change_status_params.DiscussionChangeStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DiscussionChangeStatusResponse,
        )

    async def change_title(
        self,
        num: str,
        *,
        repo_type: Literal["models", "spaces", "datasets"],
        namespace: str,
        repo: str,
        title: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DiscussionChangeTitleResponse:
        """
        Change the title of a discussion

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not repo_type:
            raise ValueError(f"Expected a non-empty value for `repo_type` but received {repo_type!r}")
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not num:
            raise ValueError(f"Expected a non-empty value for `num` but received {num!r}")
        return await self._post(
            f"/api/{repo_type}/{namespace}/{repo}/discussions/{num}/title",
            body=await async_maybe_transform(
                {"title": title}, discussion_change_title_params.DiscussionChangeTitleParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DiscussionChangeTitleResponse,
        )

    async def mark_as_read(
        self,
        *,
        apply_to_all: object | NotGiven = NOT_GIVEN,
        article_id: str | NotGiven = NOT_GIVEN,
        last_update: Union[str, datetime] | NotGiven = NOT_GIVEN,
        mention: Literal["all", "participating", "mentions"] | NotGiven = NOT_GIVEN,
        p: int | NotGiven = NOT_GIVEN,
        paper_id: str | NotGiven = NOT_GIVEN,
        post_author: str | NotGiven = NOT_GIVEN,
        read_status: Literal["all", "unread"] | NotGiven = NOT_GIVEN,
        repo_name: str | NotGiven = NOT_GIVEN,
        repo_type: Literal["dataset", "model", "space"] | NotGiven = NOT_GIVEN,
        discussion_ids: SequenceNotStr[str] | NotGiven = NOT_GIVEN,
        read: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Mark discussions as read or unread.

        If `applyToAll` is true, all notifications
        for the user matching the search parameters will be marked as read or unread.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/api/discussions/mark-as-read",
            body=await async_maybe_transform(
                {
                    "discussion_ids": discussion_ids,
                    "read": read,
                },
                discussion_mark_as_read_params.DiscussionMarkAsReadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "apply_to_all": apply_to_all,
                        "article_id": article_id,
                        "last_update": last_update,
                        "mention": mention,
                        "p": p,
                        "paper_id": paper_id,
                        "post_author": post_author,
                        "read_status": read_status,
                        "repo_name": repo_name,
                        "repo_type": repo_type,
                    },
                    discussion_mark_as_read_params.DiscussionMarkAsReadParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def merge(
        self,
        num: str,
        *,
        repo_type: Literal["models", "spaces", "datasets"],
        namespace: str,
        repo: str,
        comment: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Merge a pull request

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not repo_type:
            raise ValueError(f"Expected a non-empty value for `repo_type` but received {repo_type!r}")
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not num:
            raise ValueError(f"Expected a non-empty value for `num` but received {num!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/api/{repo_type}/{namespace}/{repo}/discussions/{num}/merge",
            body=await async_maybe_transform({"comment": comment}, discussion_merge_params.DiscussionMergeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def pin(
        self,
        num: str,
        *,
        repo_type: Literal["models", "spaces", "datasets"],
        namespace: str,
        repo: str,
        pinned: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Pin a discussion

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not repo_type:
            raise ValueError(f"Expected a non-empty value for `repo_type` but received {repo_type!r}")
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not num:
            raise ValueError(f"Expected a non-empty value for `num` but received {num!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/api/{repo_type}/{namespace}/{repo}/discussions/{num}/pin",
            body=await async_maybe_transform({"pinned": pinned}, discussion_pin_params.DiscussionPinParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DiscussionsResourceWithRawResponse:
    def __init__(self, discussions: DiscussionsResource) -> None:
        self._discussions = discussions

        self.create = to_raw_response_wrapper(
            discussions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            discussions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            discussions.list,
        )
        self.delete = to_raw_response_wrapper(
            discussions.delete,
        )
        self.add_comment = to_raw_response_wrapper(
            discussions.add_comment,
        )
        self.change_status = to_raw_response_wrapper(
            discussions.change_status,
        )
        self.change_title = to_raw_response_wrapper(
            discussions.change_title,
        )
        self.mark_as_read = to_raw_response_wrapper(
            discussions.mark_as_read,
        )
        self.merge = to_raw_response_wrapper(
            discussions.merge,
        )
        self.pin = to_raw_response_wrapper(
            discussions.pin,
        )


class AsyncDiscussionsResourceWithRawResponse:
    def __init__(self, discussions: AsyncDiscussionsResource) -> None:
        self._discussions = discussions

        self.create = async_to_raw_response_wrapper(
            discussions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            discussions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            discussions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            discussions.delete,
        )
        self.add_comment = async_to_raw_response_wrapper(
            discussions.add_comment,
        )
        self.change_status = async_to_raw_response_wrapper(
            discussions.change_status,
        )
        self.change_title = async_to_raw_response_wrapper(
            discussions.change_title,
        )
        self.mark_as_read = async_to_raw_response_wrapper(
            discussions.mark_as_read,
        )
        self.merge = async_to_raw_response_wrapper(
            discussions.merge,
        )
        self.pin = async_to_raw_response_wrapper(
            discussions.pin,
        )


class DiscussionsResourceWithStreamingResponse:
    def __init__(self, discussions: DiscussionsResource) -> None:
        self._discussions = discussions

        self.create = to_streamed_response_wrapper(
            discussions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            discussions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            discussions.list,
        )
        self.delete = to_streamed_response_wrapper(
            discussions.delete,
        )
        self.add_comment = to_streamed_response_wrapper(
            discussions.add_comment,
        )
        self.change_status = to_streamed_response_wrapper(
            discussions.change_status,
        )
        self.change_title = to_streamed_response_wrapper(
            discussions.change_title,
        )
        self.mark_as_read = to_streamed_response_wrapper(
            discussions.mark_as_read,
        )
        self.merge = to_streamed_response_wrapper(
            discussions.merge,
        )
        self.pin = to_streamed_response_wrapper(
            discussions.pin,
        )


class AsyncDiscussionsResourceWithStreamingResponse:
    def __init__(self, discussions: AsyncDiscussionsResource) -> None:
        self._discussions = discussions

        self.create = async_to_streamed_response_wrapper(
            discussions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            discussions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            discussions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            discussions.delete,
        )
        self.add_comment = async_to_streamed_response_wrapper(
            discussions.add_comment,
        )
        self.change_status = async_to_streamed_response_wrapper(
            discussions.change_status,
        )
        self.change_title = async_to_streamed_response_wrapper(
            discussions.change_title,
        )
        self.mark_as_read = async_to_streamed_response_wrapper(
            discussions.mark_as_read,
        )
        self.merge = async_to_streamed_response_wrapper(
            discussions.merge,
        )
        self.pin = async_to_streamed_response_wrapper(
            discussions.pin,
        )
