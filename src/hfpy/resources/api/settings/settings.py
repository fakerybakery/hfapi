# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from .webhooks import (
    WebhooksResource,
    AsyncWebhooksResource,
    WebhooksResourceWithRawResponse,
    AsyncWebhooksResourceWithRawResponse,
    WebhooksResourceWithStreamingResponse,
    AsyncWebhooksResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.api import setting_update_watch_params, setting_update_notifications_params
from ...._base_client import make_request_options
from .billing.billing import (
    BillingResource,
    AsyncBillingResource,
    BillingResourceWithRawResponse,
    AsyncBillingResourceWithRawResponse,
    BillingResourceWithStreamingResponse,
    AsyncBillingResourceWithStreamingResponse,
)
from ....types.api.setting_get_mcp_response import SettingGetMcpResponse

__all__ = ["SettingsResource", "AsyncSettingsResource"]


class SettingsResource(SyncAPIResource):
    @cached_property
    def webhooks(self) -> WebhooksResource:
        return WebhooksResource(self._client)

    @cached_property
    def billing(self) -> BillingResource:
        return BillingResource(self._client)

    @cached_property
    def with_raw_response(self) -> SettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return SettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return SettingsResourceWithStreamingResponse(self)

    def get_mcp(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SettingGetMcpResponse:
        """Get the MCP tools for the current user"""
        return self._get(
            "/api/settings/mcp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingGetMcpResponse,
        )

    def update_notifications(
        self,
        *,
        notifications: setting_update_notifications_params.Notifications,
        prepaid_amount: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Update notification settings for the user

        Args:
          prepaid_amount: To be provided when enabling launch_prepaid_credits

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            "/api/settings/notifications",
            body=maybe_transform(
                {
                    "notifications": notifications,
                    "prepaid_amount": prepaid_amount,
                },
                setting_update_notifications_params.SettingUpdateNotificationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update_watch(
        self,
        *,
        add: Iterable[setting_update_watch_params.Add] | NotGiven = NOT_GIVEN,
        delete: Iterable[setting_update_watch_params.Delete] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Update watch settings for the user.

        Get notified when discussions happen on your
        watched items.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            "/api/settings/watch",
            body=maybe_transform(
                {
                    "add": add,
                    "delete": delete,
                },
                setting_update_watch_params.SettingUpdateWatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSettingsResource(AsyncAPIResource):
    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        return AsyncWebhooksResource(self._client)

    @cached_property
    def billing(self) -> AsyncBillingResource:
        return AsyncBillingResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return AsyncSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return AsyncSettingsResourceWithStreamingResponse(self)

    async def get_mcp(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SettingGetMcpResponse:
        """Get the MCP tools for the current user"""
        return await self._get(
            "/api/settings/mcp",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingGetMcpResponse,
        )

    async def update_notifications(
        self,
        *,
        notifications: setting_update_notifications_params.Notifications,
        prepaid_amount: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Update notification settings for the user

        Args:
          prepaid_amount: To be provided when enabling launch_prepaid_credits

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            "/api/settings/notifications",
            body=await async_maybe_transform(
                {
                    "notifications": notifications,
                    "prepaid_amount": prepaid_amount,
                },
                setting_update_notifications_params.SettingUpdateNotificationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update_watch(
        self,
        *,
        add: Iterable[setting_update_watch_params.Add] | NotGiven = NOT_GIVEN,
        delete: Iterable[setting_update_watch_params.Delete] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Update watch settings for the user.

        Get notified when discussions happen on your
        watched items.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            "/api/settings/watch",
            body=await async_maybe_transform(
                {
                    "add": add,
                    "delete": delete,
                },
                setting_update_watch_params.SettingUpdateWatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SettingsResourceWithRawResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

        self.get_mcp = to_raw_response_wrapper(
            settings.get_mcp,
        )
        self.update_notifications = to_raw_response_wrapper(
            settings.update_notifications,
        )
        self.update_watch = to_raw_response_wrapper(
            settings.update_watch,
        )

    @cached_property
    def webhooks(self) -> WebhooksResourceWithRawResponse:
        return WebhooksResourceWithRawResponse(self._settings.webhooks)

    @cached_property
    def billing(self) -> BillingResourceWithRawResponse:
        return BillingResourceWithRawResponse(self._settings.billing)


class AsyncSettingsResourceWithRawResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

        self.get_mcp = async_to_raw_response_wrapper(
            settings.get_mcp,
        )
        self.update_notifications = async_to_raw_response_wrapper(
            settings.update_notifications,
        )
        self.update_watch = async_to_raw_response_wrapper(
            settings.update_watch,
        )

    @cached_property
    def webhooks(self) -> AsyncWebhooksResourceWithRawResponse:
        return AsyncWebhooksResourceWithRawResponse(self._settings.webhooks)

    @cached_property
    def billing(self) -> AsyncBillingResourceWithRawResponse:
        return AsyncBillingResourceWithRawResponse(self._settings.billing)


class SettingsResourceWithStreamingResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

        self.get_mcp = to_streamed_response_wrapper(
            settings.get_mcp,
        )
        self.update_notifications = to_streamed_response_wrapper(
            settings.update_notifications,
        )
        self.update_watch = to_streamed_response_wrapper(
            settings.update_watch,
        )

    @cached_property
    def webhooks(self) -> WebhooksResourceWithStreamingResponse:
        return WebhooksResourceWithStreamingResponse(self._settings.webhooks)

    @cached_property
    def billing(self) -> BillingResourceWithStreamingResponse:
        return BillingResourceWithStreamingResponse(self._settings.billing)


class AsyncSettingsResourceWithStreamingResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

        self.get_mcp = async_to_streamed_response_wrapper(
            settings.get_mcp,
        )
        self.update_notifications = async_to_streamed_response_wrapper(
            settings.update_notifications,
        )
        self.update_watch = async_to_streamed_response_wrapper(
            settings.update_watch,
        )

    @cached_property
    def webhooks(self) -> AsyncWebhooksResourceWithStreamingResponse:
        return AsyncWebhooksResourceWithStreamingResponse(self._settings.webhooks)

    @cached_property
    def billing(self) -> AsyncBillingResourceWithStreamingResponse:
        return AsyncBillingResourceWithStreamingResponse(self._settings.billing)
