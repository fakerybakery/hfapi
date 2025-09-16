# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal

import httpx

from ......_types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
    group_list_params,
    group_create_params,
    group_update_params,
    group_retrieve_params,
    group_update_attributes_params,
)
from ......types.api.organizations.scim.v2.group_list_response import GroupListResponse
from ......types.api.organizations.scim.v2.group_create_response import GroupCreateResponse
from ......types.api.organizations.scim.v2.group_update_response import GroupUpdateResponse
from ......types.api.organizations.scim.v2.group_retrieve_response import GroupRetrieveResponse
from ......types.api.organizations.scim.v2.group_update_attributes_response import GroupUpdateAttributesResponse

__all__ = ["GroupsResource", "AsyncGroupsResource"]


class GroupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return GroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return GroupsResourceWithStreamingResponse(self)

    def create(
        self,
        name: str,
        *,
        display_name: str,
        members: Iterable[group_create_params.Member],
        external_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupCreateResponse:
        """Creates a new group in the organization.

        The group name must be unique within
        the organization.

        Args:
          members: Array of SCIM user ids

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._post(
            f"/api/organizations/{name}/scim/v2/Groups",
            body=maybe_transform(
                {
                    "display_name": display_name,
                    "members": members,
                    "external_id": external_id,
                },
                group_create_params.GroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupCreateResponse,
        )

    def retrieve(
        self,
        group_id: str,
        *,
        name: str,
        excluded_attributes: Literal["members"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupRetrieveResponse:
        """Retrieves a group by its ID.

        If you provide the `excludedAttributes` parameter,
        the `members` attribute is not returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._get(
            f"/api/organizations/{name}/scim/v2/Groups/{group_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"excluded_attributes": excluded_attributes}, group_retrieve_params.GroupRetrieveParams
                ),
            ),
            cast_to=GroupRetrieveResponse,
        )

    def update(
        self,
        group_id: str,
        *,
        name: str,
        display_name: str,
        members: Iterable[group_update_params.Member],
        schemas: List[Literal["urn:ietf:params:scim:schemas:core:2.0:Group"]],
        external_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupUpdateResponse:
        """Updates a group by its ID.

        The group name must be unique within the
        organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._put(
            f"/api/organizations/{name}/scim/v2/Groups/{group_id}",
            body=maybe_transform(
                {
                    "display_name": display_name,
                    "members": members,
                    "schemas": schemas,
                    "external_id": external_id,
                },
                group_update_params.GroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupUpdateResponse,
        )

    def list(
        self,
        name: str,
        *,
        count: float | NotGiven = NOT_GIVEN,
        excluded_attributes: Literal["members"] | NotGiven = NOT_GIVEN,
        filter: str | NotGiven = NOT_GIVEN,
        start_index: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupListResponse:
        """Retrieves a paginated list of all organization groups.

        If you provide the filter
        parameter, the resources for all matching groups are returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            f"/api/organizations/{name}/scim/v2/Groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "count": count,
                        "excluded_attributes": excluded_attributes,
                        "filter": filter,
                        "start_index": start_index,
                    },
                    group_list_params.GroupListParams,
                ),
            ),
            cast_to=GroupListResponse,
        )

    def delete(
        self,
        group_id: str,
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
        Delete a SCIM group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._delete(
            f"/api/organizations/{name}/scim/v2/Groups/{group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def update_attributes(
        self,
        group_id: str,
        *,
        name: str,
        operations: Iterable[group_update_attributes_params.Operation],
        schemas: List[Literal["urn:ietf:params:scim:api:messages:2.0:PatchOp"]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupUpdateAttributesResponse:
        """Updates individual attributes using Operations format.

        Just provide the changes
        you want to make using add, remove (only `members` is supported), or replace
        operations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._patch(
            f"/api/organizations/{name}/scim/v2/Groups/{group_id}",
            body=maybe_transform(
                {
                    "operations": operations,
                    "schemas": schemas,
                },
                group_update_attributes_params.GroupUpdateAttributesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupUpdateAttributesResponse,
        )


class AsyncGroupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return AsyncGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return AsyncGroupsResourceWithStreamingResponse(self)

    async def create(
        self,
        name: str,
        *,
        display_name: str,
        members: Iterable[group_create_params.Member],
        external_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupCreateResponse:
        """Creates a new group in the organization.

        The group name must be unique within
        the organization.

        Args:
          members: Array of SCIM user ids

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._post(
            f"/api/organizations/{name}/scim/v2/Groups",
            body=await async_maybe_transform(
                {
                    "display_name": display_name,
                    "members": members,
                    "external_id": external_id,
                },
                group_create_params.GroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupCreateResponse,
        )

    async def retrieve(
        self,
        group_id: str,
        *,
        name: str,
        excluded_attributes: Literal["members"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupRetrieveResponse:
        """Retrieves a group by its ID.

        If you provide the `excludedAttributes` parameter,
        the `members` attribute is not returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._get(
            f"/api/organizations/{name}/scim/v2/Groups/{group_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"excluded_attributes": excluded_attributes}, group_retrieve_params.GroupRetrieveParams
                ),
            ),
            cast_to=GroupRetrieveResponse,
        )

    async def update(
        self,
        group_id: str,
        *,
        name: str,
        display_name: str,
        members: Iterable[group_update_params.Member],
        schemas: List[Literal["urn:ietf:params:scim:schemas:core:2.0:Group"]],
        external_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupUpdateResponse:
        """Updates a group by its ID.

        The group name must be unique within the
        organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._put(
            f"/api/organizations/{name}/scim/v2/Groups/{group_id}",
            body=await async_maybe_transform(
                {
                    "display_name": display_name,
                    "members": members,
                    "schemas": schemas,
                    "external_id": external_id,
                },
                group_update_params.GroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupUpdateResponse,
        )

    async def list(
        self,
        name: str,
        *,
        count: float | NotGiven = NOT_GIVEN,
        excluded_attributes: Literal["members"] | NotGiven = NOT_GIVEN,
        filter: str | NotGiven = NOT_GIVEN,
        start_index: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupListResponse:
        """Retrieves a paginated list of all organization groups.

        If you provide the filter
        parameter, the resources for all matching groups are returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            f"/api/organizations/{name}/scim/v2/Groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "count": count,
                        "excluded_attributes": excluded_attributes,
                        "filter": filter,
                        "start_index": start_index,
                    },
                    group_list_params.GroupListParams,
                ),
            ),
            cast_to=GroupListResponse,
        )

    async def delete(
        self,
        group_id: str,
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
        Delete a SCIM group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._delete(
            f"/api/organizations/{name}/scim/v2/Groups/{group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def update_attributes(
        self,
        group_id: str,
        *,
        name: str,
        operations: Iterable[group_update_attributes_params.Operation],
        schemas: List[Literal["urn:ietf:params:scim:api:messages:2.0:PatchOp"]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupUpdateAttributesResponse:
        """Updates individual attributes using Operations format.

        Just provide the changes
        you want to make using add, remove (only `members` is supported), or replace
        operations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._patch(
            f"/api/organizations/{name}/scim/v2/Groups/{group_id}",
            body=await async_maybe_transform(
                {
                    "operations": operations,
                    "schemas": schemas,
                },
                group_update_attributes_params.GroupUpdateAttributesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupUpdateAttributesResponse,
        )


class GroupsResourceWithRawResponse:
    def __init__(self, groups: GroupsResource) -> None:
        self._groups = groups

        self.create = to_raw_response_wrapper(
            groups.create,
        )
        self.retrieve = to_raw_response_wrapper(
            groups.retrieve,
        )
        self.update = to_raw_response_wrapper(
            groups.update,
        )
        self.list = to_raw_response_wrapper(
            groups.list,
        )
        self.delete = to_raw_response_wrapper(
            groups.delete,
        )
        self.update_attributes = to_raw_response_wrapper(
            groups.update_attributes,
        )


class AsyncGroupsResourceWithRawResponse:
    def __init__(self, groups: AsyncGroupsResource) -> None:
        self._groups = groups

        self.create = async_to_raw_response_wrapper(
            groups.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            groups.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            groups.update,
        )
        self.list = async_to_raw_response_wrapper(
            groups.list,
        )
        self.delete = async_to_raw_response_wrapper(
            groups.delete,
        )
        self.update_attributes = async_to_raw_response_wrapper(
            groups.update_attributes,
        )


class GroupsResourceWithStreamingResponse:
    def __init__(self, groups: GroupsResource) -> None:
        self._groups = groups

        self.create = to_streamed_response_wrapper(
            groups.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            groups.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            groups.update,
        )
        self.list = to_streamed_response_wrapper(
            groups.list,
        )
        self.delete = to_streamed_response_wrapper(
            groups.delete,
        )
        self.update_attributes = to_streamed_response_wrapper(
            groups.update_attributes,
        )


class AsyncGroupsResourceWithStreamingResponse:
    def __init__(self, groups: AsyncGroupsResource) -> None:
        self._groups = groups

        self.create = async_to_streamed_response_wrapper(
            groups.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            groups.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            groups.update,
        )
        self.list = async_to_streamed_response_wrapper(
            groups.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            groups.delete,
        )
        self.update_attributes = async_to_streamed_response_wrapper(
            groups.update_attributes,
        )
