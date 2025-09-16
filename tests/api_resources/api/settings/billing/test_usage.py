# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hfpy import HuggingFace, AsyncHuggingFace
from tests.utils import assert_matches_type
from hfpy.types.api.settings.billing import UsageGetResponse, UsageGetJobsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: HuggingFace) -> None:
        usage = client.api.settings.billing.usage.get()
        assert_matches_type(UsageGetResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: HuggingFace) -> None:
        usage = client.api.settings.billing.usage.get(
            period_id="ecc2efdd09bd231a9ad9bd2a",
        )
        assert_matches_type(UsageGetResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: HuggingFace) -> None:
        response = client.api.settings.billing.usage.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageGetResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: HuggingFace) -> None:
        with client.api.settings.billing.usage.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageGetResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_jobs(self, client: HuggingFace) -> None:
        usage = client.api.settings.billing.usage.get_jobs()
        assert_matches_type(UsageGetJobsResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_jobs(self, client: HuggingFace) -> None:
        response = client.api.settings.billing.usage.with_raw_response.get_jobs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageGetJobsResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_jobs(self, client: HuggingFace) -> None:
        with client.api.settings.billing.usage.with_streaming_response.get_jobs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageGetJobsResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_live(self, client: HuggingFace) -> None:
        usage = client.api.settings.billing.usage.get_live()
        assert usage is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_live(self, client: HuggingFace) -> None:
        response = client.api.settings.billing.usage.with_raw_response.get_live()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert usage is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_live(self, client: HuggingFace) -> None:
        with client.api.settings.billing.usage.with_streaming_response.get_live() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert usage is None

        assert cast(Any, response.is_closed) is True


class TestAsyncUsage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHuggingFace) -> None:
        usage = await async_client.api.settings.billing.usage.get()
        assert_matches_type(UsageGetResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        usage = await async_client.api.settings.billing.usage.get(
            period_id="ecc2efdd09bd231a9ad9bd2a",
        )
        assert_matches_type(UsageGetResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.settings.billing.usage.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageGetResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.settings.billing.usage.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageGetResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_jobs(self, async_client: AsyncHuggingFace) -> None:
        usage = await async_client.api.settings.billing.usage.get_jobs()
        assert_matches_type(UsageGetJobsResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_jobs(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.settings.billing.usage.with_raw_response.get_jobs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageGetJobsResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_jobs(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.settings.billing.usage.with_streaming_response.get_jobs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageGetJobsResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_live(self, async_client: AsyncHuggingFace) -> None:
        usage = await async_client.api.settings.billing.usage.get_live()
        assert usage is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_live(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.settings.billing.usage.with_raw_response.get_live()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert usage is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_live(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.settings.billing.usage.with_streaming_response.get_live() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert usage is None

        assert cast(Any, response.is_closed) is True
