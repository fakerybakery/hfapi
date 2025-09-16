# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hfpy import HuggingFace, AsyncHuggingFace
from tests.utils import assert_matches_type
from hfpy.types.api.organizations import (
    ResourceGroupListResponse,
    ResourceGroupCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResourceGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HuggingFace) -> None:
        resource_group = client.api.organizations.resource_groups.create(
            path_name="name",
            body_name="x",
        )
        assert_matches_type(ResourceGroupCreateResponse, resource_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HuggingFace) -> None:
        resource_group = client.api.organizations.resource_groups.create(
            path_name="name",
            body_name="x",
            auto_join={
                "enabled": True,
                "role": "admin",
            },
            description="description",
            repos=[
                {
                    "name": "deepseek-ai/DeepSeek-R1",
                    "type": "dataset",
                }
            ],
            users=[
                {
                    "role": "admin",
                    "user": "user",
                }
            ],
        )
        assert_matches_type(ResourceGroupCreateResponse, resource_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HuggingFace) -> None:
        response = client.api.organizations.resource_groups.with_raw_response.create(
            path_name="name",
            body_name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_group = response.parse()
        assert_matches_type(ResourceGroupCreateResponse, resource_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HuggingFace) -> None:
        with client.api.organizations.resource_groups.with_streaming_response.create(
            path_name="name",
            body_name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_group = response.parse()
            assert_matches_type(ResourceGroupCreateResponse, resource_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_name` but received ''"):
            client.api.organizations.resource_groups.with_raw_response.create(
                path_name="",
                body_name="x",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HuggingFace) -> None:
        resource_group = client.api.organizations.resource_groups.list(
            "name",
        )
        assert_matches_type(ResourceGroupListResponse, resource_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HuggingFace) -> None:
        response = client.api.organizations.resource_groups.with_raw_response.list(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_group = response.parse()
        assert_matches_type(ResourceGroupListResponse, resource_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HuggingFace) -> None:
        with client.api.organizations.resource_groups.with_streaming_response.list(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_group = response.parse()
            assert_matches_type(ResourceGroupListResponse, resource_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.api.organizations.resource_groups.with_raw_response.list(
                "",
            )


class TestAsyncResourceGroups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHuggingFace) -> None:
        resource_group = await async_client.api.organizations.resource_groups.create(
            path_name="name",
            body_name="x",
        )
        assert_matches_type(ResourceGroupCreateResponse, resource_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        resource_group = await async_client.api.organizations.resource_groups.create(
            path_name="name",
            body_name="x",
            auto_join={
                "enabled": True,
                "role": "admin",
            },
            description="description",
            repos=[
                {
                    "name": "deepseek-ai/DeepSeek-R1",
                    "type": "dataset",
                }
            ],
            users=[
                {
                    "role": "admin",
                    "user": "user",
                }
            ],
        )
        assert_matches_type(ResourceGroupCreateResponse, resource_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.organizations.resource_groups.with_raw_response.create(
            path_name="name",
            body_name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_group = await response.parse()
        assert_matches_type(ResourceGroupCreateResponse, resource_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.organizations.resource_groups.with_streaming_response.create(
            path_name="name",
            body_name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_group = await response.parse()
            assert_matches_type(ResourceGroupCreateResponse, resource_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_name` but received ''"):
            await async_client.api.organizations.resource_groups.with_raw_response.create(
                path_name="",
                body_name="x",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHuggingFace) -> None:
        resource_group = await async_client.api.organizations.resource_groups.list(
            "name",
        )
        assert_matches_type(ResourceGroupListResponse, resource_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.organizations.resource_groups.with_raw_response.list(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_group = await response.parse()
        assert_matches_type(ResourceGroupListResponse, resource_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.organizations.resource_groups.with_streaming_response.list(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_group = await response.parse()
            assert_matches_type(ResourceGroupListResponse, resource_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.api.organizations.resource_groups.with_raw_response.list(
                "",
            )
