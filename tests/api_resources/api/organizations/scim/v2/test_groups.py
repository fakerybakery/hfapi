# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyhfapi import HuggingFace, AsyncHuggingFace
from tests.utils import assert_matches_type
from pyhfapi.types.api.organizations.scim.v2 import (
    GroupListResponse,
    GroupCreateResponse,
    GroupUpdateResponse,
    GroupRetrieveResponse,
    GroupUpdateAttributesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HuggingFace) -> None:
        group = client.api.organizations.scim.v2.groups.create(
            name="name",
            display_name="displayName",
            members=[{"value": "ecc2efdd09bd231a9ad9bd2a"}],
        )
        assert_matches_type(GroupCreateResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HuggingFace) -> None:
        group = client.api.organizations.scim.v2.groups.create(
            name="name",
            display_name="displayName",
            members=[{"value": "ecc2efdd09bd231a9ad9bd2a"}],
            external_id="externalId",
        )
        assert_matches_type(GroupCreateResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HuggingFace) -> None:
        response = client.api.organizations.scim.v2.groups.with_raw_response.create(
            name="name",
            display_name="displayName",
            members=[{"value": "ecc2efdd09bd231a9ad9bd2a"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(GroupCreateResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HuggingFace) -> None:
        with client.api.organizations.scim.v2.groups.with_streaming_response.create(
            name="name",
            display_name="displayName",
            members=[{"value": "ecc2efdd09bd231a9ad9bd2a"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(GroupCreateResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.api.organizations.scim.v2.groups.with_raw_response.create(
                name="",
                display_name="displayName",
                members=[{"value": "ecc2efdd09bd231a9ad9bd2a"}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: HuggingFace) -> None:
        group = client.api.organizations.scim.v2.groups.retrieve(
            group_id="groupId",
            name="name",
        )
        assert_matches_type(GroupRetrieveResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: HuggingFace) -> None:
        group = client.api.organizations.scim.v2.groups.retrieve(
            group_id="groupId",
            name="name",
            excluded_attributes="members",
        )
        assert_matches_type(GroupRetrieveResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: HuggingFace) -> None:
        response = client.api.organizations.scim.v2.groups.with_raw_response.retrieve(
            group_id="groupId",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(GroupRetrieveResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: HuggingFace) -> None:
        with client.api.organizations.scim.v2.groups.with_streaming_response.retrieve(
            group_id="groupId",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(GroupRetrieveResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.api.organizations.scim.v2.groups.with_raw_response.retrieve(
                group_id="groupId",
                name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.api.organizations.scim.v2.groups.with_raw_response.retrieve(
                group_id="",
                name="name",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: HuggingFace) -> None:
        group = client.api.organizations.scim.v2.groups.update(
            group_id="groupId",
            name="name",
            display_name="displayName",
            members=[{"value": "ecc2efdd09bd231a9ad9bd2a"}],
            schemas=["urn:ietf:params:scim:schemas:core:2.0:Group"],
        )
        assert_matches_type(GroupUpdateResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: HuggingFace) -> None:
        group = client.api.organizations.scim.v2.groups.update(
            group_id="groupId",
            name="name",
            display_name="displayName",
            members=[{"value": "ecc2efdd09bd231a9ad9bd2a"}],
            schemas=["urn:ietf:params:scim:schemas:core:2.0:Group"],
            external_id="externalId",
        )
        assert_matches_type(GroupUpdateResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HuggingFace) -> None:
        response = client.api.organizations.scim.v2.groups.with_raw_response.update(
            group_id="groupId",
            name="name",
            display_name="displayName",
            members=[{"value": "ecc2efdd09bd231a9ad9bd2a"}],
            schemas=["urn:ietf:params:scim:schemas:core:2.0:Group"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(GroupUpdateResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HuggingFace) -> None:
        with client.api.organizations.scim.v2.groups.with_streaming_response.update(
            group_id="groupId",
            name="name",
            display_name="displayName",
            members=[{"value": "ecc2efdd09bd231a9ad9bd2a"}],
            schemas=["urn:ietf:params:scim:schemas:core:2.0:Group"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(GroupUpdateResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.api.organizations.scim.v2.groups.with_raw_response.update(
                group_id="groupId",
                name="",
                display_name="displayName",
                members=[{"value": "ecc2efdd09bd231a9ad9bd2a"}],
                schemas=["urn:ietf:params:scim:schemas:core:2.0:Group"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.api.organizations.scim.v2.groups.with_raw_response.update(
                group_id="",
                name="name",
                display_name="displayName",
                members=[{"value": "ecc2efdd09bd231a9ad9bd2a"}],
                schemas=["urn:ietf:params:scim:schemas:core:2.0:Group"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HuggingFace) -> None:
        group = client.api.organizations.scim.v2.groups.list(
            name="name",
        )
        assert_matches_type(GroupListResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HuggingFace) -> None:
        group = client.api.organizations.scim.v2.groups.list(
            name="name",
            count=1,
            excluded_attributes="members",
            filter="filter",
            start_index=1,
        )
        assert_matches_type(GroupListResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HuggingFace) -> None:
        response = client.api.organizations.scim.v2.groups.with_raw_response.list(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(GroupListResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HuggingFace) -> None:
        with client.api.organizations.scim.v2.groups.with_streaming_response.list(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(GroupListResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.api.organizations.scim.v2.groups.with_raw_response.list(
                name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HuggingFace) -> None:
        group = client.api.organizations.scim.v2.groups.delete(
            group_id="groupId",
            name="name",
        )
        assert_matches_type(object, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HuggingFace) -> None:
        response = client.api.organizations.scim.v2.groups.with_raw_response.delete(
            group_id="groupId",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(object, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HuggingFace) -> None:
        with client.api.organizations.scim.v2.groups.with_streaming_response.delete(
            group_id="groupId",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(object, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.api.organizations.scim.v2.groups.with_raw_response.delete(
                group_id="groupId",
                name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.api.organizations.scim.v2.groups.with_raw_response.delete(
                group_id="",
                name="name",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_attributes(self, client: HuggingFace) -> None:
        group = client.api.organizations.scim.v2.groups.update_attributes(
            group_id="groupId",
            name="name",
            operations=[
                {
                    "op": "op",
                    "path": "path",
                }
            ],
            schemas=["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
        )
        assert_matches_type(GroupUpdateAttributesResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_attributes(self, client: HuggingFace) -> None:
        response = client.api.organizations.scim.v2.groups.with_raw_response.update_attributes(
            group_id="groupId",
            name="name",
            operations=[
                {
                    "op": "op",
                    "path": "path",
                }
            ],
            schemas=["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(GroupUpdateAttributesResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_attributes(self, client: HuggingFace) -> None:
        with client.api.organizations.scim.v2.groups.with_streaming_response.update_attributes(
            group_id="groupId",
            name="name",
            operations=[
                {
                    "op": "op",
                    "path": "path",
                }
            ],
            schemas=["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(GroupUpdateAttributesResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_attributes(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.api.organizations.scim.v2.groups.with_raw_response.update_attributes(
                group_id="groupId",
                name="",
                operations=[
                    {
                        "op": "op",
                        "path": "path",
                    }
                ],
                schemas=["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.api.organizations.scim.v2.groups.with_raw_response.update_attributes(
                group_id="",
                name="name",
                operations=[
                    {
                        "op": "op",
                        "path": "path",
                    }
                ],
                schemas=["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
            )


class TestAsyncGroups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHuggingFace) -> None:
        group = await async_client.api.organizations.scim.v2.groups.create(
            name="name",
            display_name="displayName",
            members=[{"value": "ecc2efdd09bd231a9ad9bd2a"}],
        )
        assert_matches_type(GroupCreateResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        group = await async_client.api.organizations.scim.v2.groups.create(
            name="name",
            display_name="displayName",
            members=[{"value": "ecc2efdd09bd231a9ad9bd2a"}],
            external_id="externalId",
        )
        assert_matches_type(GroupCreateResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.organizations.scim.v2.groups.with_raw_response.create(
            name="name",
            display_name="displayName",
            members=[{"value": "ecc2efdd09bd231a9ad9bd2a"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(GroupCreateResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.organizations.scim.v2.groups.with_streaming_response.create(
            name="name",
            display_name="displayName",
            members=[{"value": "ecc2efdd09bd231a9ad9bd2a"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(GroupCreateResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.api.organizations.scim.v2.groups.with_raw_response.create(
                name="",
                display_name="displayName",
                members=[{"value": "ecc2efdd09bd231a9ad9bd2a"}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncHuggingFace) -> None:
        group = await async_client.api.organizations.scim.v2.groups.retrieve(
            group_id="groupId",
            name="name",
        )
        assert_matches_type(GroupRetrieveResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        group = await async_client.api.organizations.scim.v2.groups.retrieve(
            group_id="groupId",
            name="name",
            excluded_attributes="members",
        )
        assert_matches_type(GroupRetrieveResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.organizations.scim.v2.groups.with_raw_response.retrieve(
            group_id="groupId",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(GroupRetrieveResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.organizations.scim.v2.groups.with_streaming_response.retrieve(
            group_id="groupId",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(GroupRetrieveResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.api.organizations.scim.v2.groups.with_raw_response.retrieve(
                group_id="groupId",
                name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.api.organizations.scim.v2.groups.with_raw_response.retrieve(
                group_id="",
                name="name",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHuggingFace) -> None:
        group = await async_client.api.organizations.scim.v2.groups.update(
            group_id="groupId",
            name="name",
            display_name="displayName",
            members=[{"value": "ecc2efdd09bd231a9ad9bd2a"}],
            schemas=["urn:ietf:params:scim:schemas:core:2.0:Group"],
        )
        assert_matches_type(GroupUpdateResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        group = await async_client.api.organizations.scim.v2.groups.update(
            group_id="groupId",
            name="name",
            display_name="displayName",
            members=[{"value": "ecc2efdd09bd231a9ad9bd2a"}],
            schemas=["urn:ietf:params:scim:schemas:core:2.0:Group"],
            external_id="externalId",
        )
        assert_matches_type(GroupUpdateResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.organizations.scim.v2.groups.with_raw_response.update(
            group_id="groupId",
            name="name",
            display_name="displayName",
            members=[{"value": "ecc2efdd09bd231a9ad9bd2a"}],
            schemas=["urn:ietf:params:scim:schemas:core:2.0:Group"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(GroupUpdateResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.organizations.scim.v2.groups.with_streaming_response.update(
            group_id="groupId",
            name="name",
            display_name="displayName",
            members=[{"value": "ecc2efdd09bd231a9ad9bd2a"}],
            schemas=["urn:ietf:params:scim:schemas:core:2.0:Group"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(GroupUpdateResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.api.organizations.scim.v2.groups.with_raw_response.update(
                group_id="groupId",
                name="",
                display_name="displayName",
                members=[{"value": "ecc2efdd09bd231a9ad9bd2a"}],
                schemas=["urn:ietf:params:scim:schemas:core:2.0:Group"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.api.organizations.scim.v2.groups.with_raw_response.update(
                group_id="",
                name="name",
                display_name="displayName",
                members=[{"value": "ecc2efdd09bd231a9ad9bd2a"}],
                schemas=["urn:ietf:params:scim:schemas:core:2.0:Group"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHuggingFace) -> None:
        group = await async_client.api.organizations.scim.v2.groups.list(
            name="name",
        )
        assert_matches_type(GroupListResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        group = await async_client.api.organizations.scim.v2.groups.list(
            name="name",
            count=1,
            excluded_attributes="members",
            filter="filter",
            start_index=1,
        )
        assert_matches_type(GroupListResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.organizations.scim.v2.groups.with_raw_response.list(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(GroupListResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.organizations.scim.v2.groups.with_streaming_response.list(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(GroupListResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.api.organizations.scim.v2.groups.with_raw_response.list(
                name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHuggingFace) -> None:
        group = await async_client.api.organizations.scim.v2.groups.delete(
            group_id="groupId",
            name="name",
        )
        assert_matches_type(object, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.organizations.scim.v2.groups.with_raw_response.delete(
            group_id="groupId",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(object, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.organizations.scim.v2.groups.with_streaming_response.delete(
            group_id="groupId",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(object, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.api.organizations.scim.v2.groups.with_raw_response.delete(
                group_id="groupId",
                name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.api.organizations.scim.v2.groups.with_raw_response.delete(
                group_id="",
                name="name",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_attributes(self, async_client: AsyncHuggingFace) -> None:
        group = await async_client.api.organizations.scim.v2.groups.update_attributes(
            group_id="groupId",
            name="name",
            operations=[
                {
                    "op": "op",
                    "path": "path",
                }
            ],
            schemas=["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
        )
        assert_matches_type(GroupUpdateAttributesResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_attributes(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.organizations.scim.v2.groups.with_raw_response.update_attributes(
            group_id="groupId",
            name="name",
            operations=[
                {
                    "op": "op",
                    "path": "path",
                }
            ],
            schemas=["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(GroupUpdateAttributesResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_attributes(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.organizations.scim.v2.groups.with_streaming_response.update_attributes(
            group_id="groupId",
            name="name",
            operations=[
                {
                    "op": "op",
                    "path": "path",
                }
            ],
            schemas=["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(GroupUpdateAttributesResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_attributes(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.api.organizations.scim.v2.groups.with_raw_response.update_attributes(
                group_id="groupId",
                name="",
                operations=[
                    {
                        "op": "op",
                        "path": "path",
                    }
                ],
                schemas=["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.api.organizations.scim.v2.groups.with_raw_response.update_attributes(
                group_id="",
                name="name",
                operations=[
                    {
                        "op": "op",
                        "path": "path",
                    }
                ],
                schemas=["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
            )
