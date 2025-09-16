# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyhfapi import HuggingFace, AsyncHuggingFace
from tests.utils import assert_matches_type
from pyhfapi.types.api.spaces import ResourceGroupAddResponse, ResourceGroupGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResourceGroup:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add(self, client: HuggingFace) -> None:
        resource_group = client.api.spaces.resource_group.add(
            repo="repo",
            namespace="namespace",
            resource_group_id="ecc2efdd09bd231a9ad9bd2a",
        )
        assert_matches_type(ResourceGroupAddResponse, resource_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: HuggingFace) -> None:
        response = client.api.spaces.resource_group.with_raw_response.add(
            repo="repo",
            namespace="namespace",
            resource_group_id="ecc2efdd09bd231a9ad9bd2a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_group = response.parse()
        assert_matches_type(ResourceGroupAddResponse, resource_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: HuggingFace) -> None:
        with client.api.spaces.resource_group.with_streaming_response.add(
            repo="repo",
            namespace="namespace",
            resource_group_id="ecc2efdd09bd231a9ad9bd2a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_group = response.parse()
            assert_matches_type(ResourceGroupAddResponse, resource_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_add(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.spaces.resource_group.with_raw_response.add(
                repo="repo",
                namespace="",
                resource_group_id="ecc2efdd09bd231a9ad9bd2a",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.spaces.resource_group.with_raw_response.add(
                repo="",
                namespace="namespace",
                resource_group_id="ecc2efdd09bd231a9ad9bd2a",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: HuggingFace) -> None:
        resource_group = client.api.spaces.resource_group.get(
            repo="repo",
            namespace="namespace",
        )
        assert_matches_type(ResourceGroupGetResponse, resource_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: HuggingFace) -> None:
        response = client.api.spaces.resource_group.with_raw_response.get(
            repo="repo",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_group = response.parse()
        assert_matches_type(ResourceGroupGetResponse, resource_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: HuggingFace) -> None:
        with client.api.spaces.resource_group.with_streaming_response.get(
            repo="repo",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_group = response.parse()
            assert_matches_type(ResourceGroupGetResponse, resource_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.spaces.resource_group.with_raw_response.get(
                repo="repo",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.spaces.resource_group.with_raw_response.get(
                repo="",
                namespace="namespace",
            )


class TestAsyncResourceGroup:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncHuggingFace) -> None:
        resource_group = await async_client.api.spaces.resource_group.add(
            repo="repo",
            namespace="namespace",
            resource_group_id="ecc2efdd09bd231a9ad9bd2a",
        )
        assert_matches_type(ResourceGroupAddResponse, resource_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.spaces.resource_group.with_raw_response.add(
            repo="repo",
            namespace="namespace",
            resource_group_id="ecc2efdd09bd231a9ad9bd2a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_group = await response.parse()
        assert_matches_type(ResourceGroupAddResponse, resource_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.spaces.resource_group.with_streaming_response.add(
            repo="repo",
            namespace="namespace",
            resource_group_id="ecc2efdd09bd231a9ad9bd2a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_group = await response.parse()
            assert_matches_type(ResourceGroupAddResponse, resource_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.spaces.resource_group.with_raw_response.add(
                repo="repo",
                namespace="",
                resource_group_id="ecc2efdd09bd231a9ad9bd2a",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.spaces.resource_group.with_raw_response.add(
                repo="",
                namespace="namespace",
                resource_group_id="ecc2efdd09bd231a9ad9bd2a",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHuggingFace) -> None:
        resource_group = await async_client.api.spaces.resource_group.get(
            repo="repo",
            namespace="namespace",
        )
        assert_matches_type(ResourceGroupGetResponse, resource_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.spaces.resource_group.with_raw_response.get(
            repo="repo",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_group = await response.parse()
        assert_matches_type(ResourceGroupGetResponse, resource_group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.spaces.resource_group.with_streaming_response.get(
            repo="repo",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_group = await response.parse()
            assert_matches_type(ResourceGroupGetResponse, resource_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.spaces.resource_group.with_raw_response.get(
                repo="repo",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.spaces.resource_group.with_raw_response.get(
                repo="",
                namespace="namespace",
            )
