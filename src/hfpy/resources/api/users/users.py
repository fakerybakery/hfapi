# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .billing.billing import (
    BillingResource,
    AsyncBillingResource,
    BillingResourceWithRawResponse,
    AsyncBillingResourceWithRawResponse,
    BillingResourceWithStreamingResponse,
    AsyncBillingResourceWithStreamingResponse,
)

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def billing(self) -> BillingResource:
        return BillingResource(self._client)

    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def billing(self) -> AsyncBillingResource:
        return AsyncBillingResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

    @cached_property
    def billing(self) -> BillingResourceWithRawResponse:
        return BillingResourceWithRawResponse(self._users.billing)


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

    @cached_property
    def billing(self) -> AsyncBillingResourceWithRawResponse:
        return AsyncBillingResourceWithRawResponse(self._users.billing)


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

    @cached_property
    def billing(self) -> BillingResourceWithStreamingResponse:
        return BillingResourceWithStreamingResponse(self._users.billing)


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

    @cached_property
    def billing(self) -> AsyncBillingResourceWithStreamingResponse:
        return AsyncBillingResourceWithStreamingResponse(self._users.billing)
