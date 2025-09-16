# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
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
from ...types.api import notification_list_params, notification_delete_params
from ..._base_client import make_request_options
from ...types.api.notification_list_response import NotificationListResponse

__all__ = ["NotificationsResource", "AsyncNotificationsResource"]


class NotificationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NotificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return NotificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NotificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return NotificationsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        article_id: str | NotGiven = NOT_GIVEN,
        last_update: Union[str, datetime] | NotGiven = NOT_GIVEN,
        mention: Literal["all", "participating", "mentions"] | NotGiven = NOT_GIVEN,
        p: int | NotGiven = NOT_GIVEN,
        paper_id: str | NotGiven = NOT_GIVEN,
        post_author: str | NotGiven = NOT_GIVEN,
        read_status: Literal["all", "unread"] | NotGiven = NOT_GIVEN,
        repo_name: str | NotGiven = NOT_GIVEN,
        repo_type: Literal["dataset", "model", "space"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NotificationListResponse:
        """
        List notifications for the user

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/notifications",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
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
                    notification_list_params.NotificationListParams,
                ),
            ),
            cast_to=NotificationListResponse,
        )

    def delete(
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete notifications, either by specifying discussionIds or by applying to all
        notifications with search parameters

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/api/notifications",
            body=maybe_transform(
                {"discussion_ids": discussion_ids}, notification_delete_params.NotificationDeleteParams
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
                    notification_delete_params.NotificationDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncNotificationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNotificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return AsyncNotificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNotificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return AsyncNotificationsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        article_id: str | NotGiven = NOT_GIVEN,
        last_update: Union[str, datetime] | NotGiven = NOT_GIVEN,
        mention: Literal["all", "participating", "mentions"] | NotGiven = NOT_GIVEN,
        p: int | NotGiven = NOT_GIVEN,
        paper_id: str | NotGiven = NOT_GIVEN,
        post_author: str | NotGiven = NOT_GIVEN,
        read_status: Literal["all", "unread"] | NotGiven = NOT_GIVEN,
        repo_name: str | NotGiven = NOT_GIVEN,
        repo_type: Literal["dataset", "model", "space"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NotificationListResponse:
        """
        List notifications for the user

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/notifications",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
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
                    notification_list_params.NotificationListParams,
                ),
            ),
            cast_to=NotificationListResponse,
        )

    async def delete(
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete notifications, either by specifying discussionIds or by applying to all
        notifications with search parameters

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/api/notifications",
            body=await async_maybe_transform(
                {"discussion_ids": discussion_ids}, notification_delete_params.NotificationDeleteParams
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
                    notification_delete_params.NotificationDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )


class NotificationsResourceWithRawResponse:
    def __init__(self, notifications: NotificationsResource) -> None:
        self._notifications = notifications

        self.list = to_raw_response_wrapper(
            notifications.list,
        )
        self.delete = to_raw_response_wrapper(
            notifications.delete,
        )


class AsyncNotificationsResourceWithRawResponse:
    def __init__(self, notifications: AsyncNotificationsResource) -> None:
        self._notifications = notifications

        self.list = async_to_raw_response_wrapper(
            notifications.list,
        )
        self.delete = async_to_raw_response_wrapper(
            notifications.delete,
        )


class NotificationsResourceWithStreamingResponse:
    def __init__(self, notifications: NotificationsResource) -> None:
        self._notifications = notifications

        self.list = to_streamed_response_wrapper(
            notifications.list,
        )
        self.delete = to_streamed_response_wrapper(
            notifications.delete,
        )


class AsyncNotificationsResourceWithStreamingResponse:
    def __init__(self, notifications: AsyncNotificationsResource) -> None:
        self._notifications = notifications

        self.list = async_to_streamed_response_wrapper(
            notifications.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            notifications.delete,
        )
