# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal

import httpx

from ......_types import NOT_GIVEN, Body, Query, Headers, NotGiven, SequenceNotStr
from ......_utils import maybe_transform, async_maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_base_client import make_request_options
from ......types.api.organizations.scim.v2 import (
    user_list_params,
    user_create_params,
    user_update_params,
    user_update_attributes_params,
)
from ......types.api.organizations.scim.v2.user_list_response import UserListResponse
from ......types.api.organizations.scim.v2.user_create_response import UserCreateResponse
from ......types.api.organizations.scim.v2.user_update_response import UserUpdateResponse
from ......types.api.organizations.scim.v2.user_retrieve_response import UserRetrieveResponse
from ......types.api.organizations.scim.v2.user_update_attributes_response import UserUpdateAttributesResponse

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
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

    def create(
        self,
        path_name: str,
        *,
        emails: Iterable[user_create_params.Email],
        external_id: str,
        body_name: user_create_params.Name,
        schemas: SequenceNotStr[str],
        user_name: str,
        active: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserCreateResponse:
        """Creates a new user in the organization.

        If the user already exists, only
        `active` field will be updated to provision the user.

        Args:
          user_name: Username for the user, it should respect the hub rules: No consecutive dashes,
              No digit-only, Does not start or end with a dash, Only dashes, letters or
              numbers, Not 24 chars hex string

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_name:
            raise ValueError(f"Expected a non-empty value for `path_name` but received {path_name!r}")
        return self._post(
            f"/api/organizations/{path_name}/scim/v2/Users",
            body=maybe_transform(
                {
                    "emails": emails,
                    "external_id": external_id,
                    "body_name": body_name,
                    "schemas": schemas,
                    "user_name": user_name,
                    "active": active,
                },
                user_create_params.UserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserCreateResponse,
        )

    def retrieve(
        self,
        user_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserRetrieveResponse:
        """
        Retrieves a SCIM user by their ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            f"/api/organizations/{name}/scim/v2/Users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRetrieveResponse,
        )

    def update(
        self,
        user_id: str,
        *,
        path_name: str,
        emails: Iterable[user_update_params.Email],
        external_id: str,
        body_name: user_update_params.Name,
        schemas: SequenceNotStr[str],
        user_name: str,
        active: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserUpdateResponse:
        """
        Updates a provisioned user, you'll need to provide all their information fresh -
        just like setting them up for the first time. Any details you don't include will
        be automatically removed, so make sure to include everything they need to keep
        their account running smoothly. Setting `active` to `false` will deprovision the
        user from the organization.

        Args:
          user_name: Username for the user, it should respect the hub rules: No consecutive dashes,
              No digit-only, Does not start or end with a dash, Only dashes, letters or
              numbers, Not 24 chars hex string

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_name:
            raise ValueError(f"Expected a non-empty value for `path_name` but received {path_name!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._put(
            f"/api/organizations/{path_name}/scim/v2/Users/{user_id}",
            body=maybe_transform(
                {
                    "emails": emails,
                    "external_id": external_id,
                    "body_name": body_name,
                    "schemas": schemas,
                    "user_name": user_name,
                    "active": active,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserUpdateResponse,
        )

    def list(
        self,
        name: str,
        *,
        count: float | NotGiven = NOT_GIVEN,
        filter: str | NotGiven = NOT_GIVEN,
        start_index: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListResponse:
        """
        Retrieves a paginated list of all organization members who have been set up,
        including disabled users. If you provide the filter parameter, the resources for
        all matching members are returned.

        Args:
          filter: You can filter results using the equals operator (eq) to find items that match
              specific values like `id`, `userName`, `emails`, and `externalId`. For example,
              to find a user named Bob, use this search: `?filter=userName%20eq%20Bob`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            f"/api/organizations/{name}/scim/v2/Users",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "count": count,
                        "filter": filter,
                        "start_index": start_index,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            cast_to=UserListResponse,
        )

    def delete(
        self,
        user_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete a SCIM user

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._delete(
            f"/api/organizations/{name}/scim/v2/Users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def update_attributes(
        self,
        user_id: str,
        *,
        name: str,
        operations: Iterable[user_update_attributes_params.Operation],
        schemas: List[Literal["urn:ietf:params:scim:api:messages:2.0:PatchOp"]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserUpdateAttributesResponse:
        """Modify individual attributes using Operations format.

        Just provide the changes
        you want to make using add, remove (only `externalId` is supported), or replace
        operations. If you set `active` to `false`, the user will be deprovisioned from
        the organization. Complicated SCIM `path` values are not supported like
        `emails[type eq 'work'].value`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._patch(
            f"/api/organizations/{name}/scim/v2/Users/{user_id}",
            body=maybe_transform(
                {
                    "operations": operations,
                    "schemas": schemas,
                },
                user_update_attributes_params.UserUpdateAttributesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserUpdateAttributesResponse,
        )


class AsyncUsersResource(AsyncAPIResource):
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

    async def create(
        self,
        path_name: str,
        *,
        emails: Iterable[user_create_params.Email],
        external_id: str,
        body_name: user_create_params.Name,
        schemas: SequenceNotStr[str],
        user_name: str,
        active: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserCreateResponse:
        """Creates a new user in the organization.

        If the user already exists, only
        `active` field will be updated to provision the user.

        Args:
          user_name: Username for the user, it should respect the hub rules: No consecutive dashes,
              No digit-only, Does not start or end with a dash, Only dashes, letters or
              numbers, Not 24 chars hex string

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_name:
            raise ValueError(f"Expected a non-empty value for `path_name` but received {path_name!r}")
        return await self._post(
            f"/api/organizations/{path_name}/scim/v2/Users",
            body=await async_maybe_transform(
                {
                    "emails": emails,
                    "external_id": external_id,
                    "body_name": body_name,
                    "schemas": schemas,
                    "user_name": user_name,
                    "active": active,
                },
                user_create_params.UserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserCreateResponse,
        )

    async def retrieve(
        self,
        user_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserRetrieveResponse:
        """
        Retrieves a SCIM user by their ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            f"/api/organizations/{name}/scim/v2/Users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRetrieveResponse,
        )

    async def update(
        self,
        user_id: str,
        *,
        path_name: str,
        emails: Iterable[user_update_params.Email],
        external_id: str,
        body_name: user_update_params.Name,
        schemas: SequenceNotStr[str],
        user_name: str,
        active: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserUpdateResponse:
        """
        Updates a provisioned user, you'll need to provide all their information fresh -
        just like setting them up for the first time. Any details you don't include will
        be automatically removed, so make sure to include everything they need to keep
        their account running smoothly. Setting `active` to `false` will deprovision the
        user from the organization.

        Args:
          user_name: Username for the user, it should respect the hub rules: No consecutive dashes,
              No digit-only, Does not start or end with a dash, Only dashes, letters or
              numbers, Not 24 chars hex string

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_name:
            raise ValueError(f"Expected a non-empty value for `path_name` but received {path_name!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._put(
            f"/api/organizations/{path_name}/scim/v2/Users/{user_id}",
            body=await async_maybe_transform(
                {
                    "emails": emails,
                    "external_id": external_id,
                    "body_name": body_name,
                    "schemas": schemas,
                    "user_name": user_name,
                    "active": active,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserUpdateResponse,
        )

    async def list(
        self,
        name: str,
        *,
        count: float | NotGiven = NOT_GIVEN,
        filter: str | NotGiven = NOT_GIVEN,
        start_index: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListResponse:
        """
        Retrieves a paginated list of all organization members who have been set up,
        including disabled users. If you provide the filter parameter, the resources for
        all matching members are returned.

        Args:
          filter: You can filter results using the equals operator (eq) to find items that match
              specific values like `id`, `userName`, `emails`, and `externalId`. For example,
              to find a user named Bob, use this search: `?filter=userName%20eq%20Bob`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            f"/api/organizations/{name}/scim/v2/Users",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "count": count,
                        "filter": filter,
                        "start_index": start_index,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            cast_to=UserListResponse,
        )

    async def delete(
        self,
        user_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete a SCIM user

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._delete(
            f"/api/organizations/{name}/scim/v2/Users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def update_attributes(
        self,
        user_id: str,
        *,
        name: str,
        operations: Iterable[user_update_attributes_params.Operation],
        schemas: List[Literal["urn:ietf:params:scim:api:messages:2.0:PatchOp"]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserUpdateAttributesResponse:
        """Modify individual attributes using Operations format.

        Just provide the changes
        you want to make using add, remove (only `externalId` is supported), or replace
        operations. If you set `active` to `false`, the user will be deprovisioned from
        the organization. Complicated SCIM `path` values are not supported like
        `emails[type eq 'work'].value`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._patch(
            f"/api/organizations/{name}/scim/v2/Users/{user_id}",
            body=await async_maybe_transform(
                {
                    "operations": operations,
                    "schemas": schemas,
                },
                user_update_attributes_params.UserUpdateAttributesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserUpdateAttributesResponse,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.create = to_raw_response_wrapper(
            users.create,
        )
        self.retrieve = to_raw_response_wrapper(
            users.retrieve,
        )
        self.update = to_raw_response_wrapper(
            users.update,
        )
        self.list = to_raw_response_wrapper(
            users.list,
        )
        self.delete = to_raw_response_wrapper(
            users.delete,
        )
        self.update_attributes = to_raw_response_wrapper(
            users.update_attributes,
        )


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_raw_response_wrapper(
            users.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            users.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            users.update,
        )
        self.list = async_to_raw_response_wrapper(
            users.list,
        )
        self.delete = async_to_raw_response_wrapper(
            users.delete,
        )
        self.update_attributes = async_to_raw_response_wrapper(
            users.update_attributes,
        )


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.create = to_streamed_response_wrapper(
            users.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            users.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            users.update,
        )
        self.list = to_streamed_response_wrapper(
            users.list,
        )
        self.delete = to_streamed_response_wrapper(
            users.delete,
        )
        self.update_attributes = to_streamed_response_wrapper(
            users.update_attributes,
        )


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_streamed_response_wrapper(
            users.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            users.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            users.update,
        )
        self.list = async_to_streamed_response_wrapper(
            users.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            users.delete,
        )
        self.update_attributes = async_to_streamed_response_wrapper(
            users.update_attributes,
        )
