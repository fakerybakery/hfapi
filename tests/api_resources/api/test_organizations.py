# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hfpy import HuggingFace, AsyncHuggingFace
from tests.utils import assert_matches_type
from hfpy.types.api import (
    OrganizationListMembersResponse,
    OrganizationRetrieveAvatarResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrganizations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_members(self, client: HuggingFace) -> None:
        organization = client.api.organizations.list_members(
            name="name",
        )
        assert_matches_type(OrganizationListMembersResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_members_with_all_params(self, client: HuggingFace) -> None:
        organization = client.api.organizations.list_members(
            name="name",
            cursor="cursor",
            limit=10,
            search="search",
        )
        assert_matches_type(OrganizationListMembersResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_members(self, client: HuggingFace) -> None:
        response = client.api.organizations.with_raw_response.list_members(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationListMembersResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_members(self, client: HuggingFace) -> None:
        with client.api.organizations.with_streaming_response.list_members(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationListMembersResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_members(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.api.organizations.with_raw_response.list_members(
                name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_avatar(self, client: HuggingFace) -> None:
        organization = client.api.organizations.retrieve_avatar(
            name="name",
        )
        assert_matches_type(OrganizationRetrieveAvatarResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_avatar_with_all_params(self, client: HuggingFace) -> None:
        organization = client.api.organizations.retrieve_avatar(
            name="name",
            redirect={},
        )
        assert_matches_type(OrganizationRetrieveAvatarResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_avatar(self, client: HuggingFace) -> None:
        response = client.api.organizations.with_raw_response.retrieve_avatar(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationRetrieveAvatarResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_avatar(self, client: HuggingFace) -> None:
        with client.api.organizations.with_streaming_response.retrieve_avatar(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationRetrieveAvatarResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_avatar(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.api.organizations.with_raw_response.retrieve_avatar(
                name="",
            )


class TestAsyncOrganizations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_members(self, async_client: AsyncHuggingFace) -> None:
        organization = await async_client.api.organizations.list_members(
            name="name",
        )
        assert_matches_type(OrganizationListMembersResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_members_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        organization = await async_client.api.organizations.list_members(
            name="name",
            cursor="cursor",
            limit=10,
            search="search",
        )
        assert_matches_type(OrganizationListMembersResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_members(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.organizations.with_raw_response.list_members(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationListMembersResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_members(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.organizations.with_streaming_response.list_members(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationListMembersResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_members(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.api.organizations.with_raw_response.list_members(
                name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_avatar(self, async_client: AsyncHuggingFace) -> None:
        organization = await async_client.api.organizations.retrieve_avatar(
            name="name",
        )
        assert_matches_type(OrganizationRetrieveAvatarResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_avatar_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        organization = await async_client.api.organizations.retrieve_avatar(
            name="name",
            redirect={},
        )
        assert_matches_type(OrganizationRetrieveAvatarResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_avatar(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.organizations.with_raw_response.retrieve_avatar(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationRetrieveAvatarResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_avatar(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.organizations.with_streaming_response.retrieve_avatar(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationRetrieveAvatarResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_avatar(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.api.organizations.with_raw_response.retrieve_avatar(
                name="",
            )
