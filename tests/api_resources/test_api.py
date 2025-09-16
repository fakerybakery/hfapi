# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hfpy import HuggingFace, AsyncHuggingFace
from hfpy.types import (
    APIGetUserInfoResponse,
    APIGetModelTagsResponse,
    APIGetDailyPapersResponse,
    APIGetDatasetTagsResponse,
)
from hfpy._utils import parse_date
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPI:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_daily_papers(self, client: HuggingFace) -> None:
        api = client.api.get_daily_papers()
        assert_matches_type(APIGetDailyPapersResponse, api, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_daily_papers_with_all_params(self, client: HuggingFace) -> None:
        api = client.api.get_daily_papers(
            date=parse_date("2019-12-27"),
            limit=1,
            p=0,
            sort="publishedAt",
            submitter="submitter",
        )
        assert_matches_type(APIGetDailyPapersResponse, api, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_daily_papers(self, client: HuggingFace) -> None:
        response = client.api.with_raw_response.get_daily_papers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = response.parse()
        assert_matches_type(APIGetDailyPapersResponse, api, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_daily_papers(self, client: HuggingFace) -> None:
        with client.api.with_streaming_response.get_daily_papers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = response.parse()
            assert_matches_type(APIGetDailyPapersResponse, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_dataset_tags(self, client: HuggingFace) -> None:
        api = client.api.get_dataset_tags()
        assert_matches_type(APIGetDatasetTagsResponse, api, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_dataset_tags_with_all_params(self, client: HuggingFace) -> None:
        api = client.api.get_dataset_tags(
            type="task_categories",
        )
        assert_matches_type(APIGetDatasetTagsResponse, api, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_dataset_tags(self, client: HuggingFace) -> None:
        response = client.api.with_raw_response.get_dataset_tags()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = response.parse()
        assert_matches_type(APIGetDatasetTagsResponse, api, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_dataset_tags(self, client: HuggingFace) -> None:
        with client.api.with_streaming_response.get_dataset_tags() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = response.parse()
            assert_matches_type(APIGetDatasetTagsResponse, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_model_tags(self, client: HuggingFace) -> None:
        api = client.api.get_model_tags()
        assert_matches_type(APIGetModelTagsResponse, api, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_model_tags_with_all_params(self, client: HuggingFace) -> None:
        api = client.api.get_model_tags(
            type="pipeline_tag",
        )
        assert_matches_type(APIGetModelTagsResponse, api, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_model_tags(self, client: HuggingFace) -> None:
        response = client.api.with_raw_response.get_model_tags()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = response.parse()
        assert_matches_type(APIGetModelTagsResponse, api, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_model_tags(self, client: HuggingFace) -> None:
        with client.api.with_streaming_response.get_model_tags() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = response.parse()
            assert_matches_type(APIGetModelTagsResponse, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_user_info(self, client: HuggingFace) -> None:
        api = client.api.get_user_info()
        assert_matches_type(APIGetUserInfoResponse, api, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_user_info(self, client: HuggingFace) -> None:
        response = client.api.with_raw_response.get_user_info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = response.parse()
        assert_matches_type(APIGetUserInfoResponse, api, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_user_info(self, client: HuggingFace) -> None:
        with client.api.with_streaming_response.get_user_info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = response.parse()
            assert_matches_type(APIGetUserInfoResponse, api, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAPI:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_daily_papers(self, async_client: AsyncHuggingFace) -> None:
        api = await async_client.api.get_daily_papers()
        assert_matches_type(APIGetDailyPapersResponse, api, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_daily_papers_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        api = await async_client.api.get_daily_papers(
            date=parse_date("2019-12-27"),
            limit=1,
            p=0,
            sort="publishedAt",
            submitter="submitter",
        )
        assert_matches_type(APIGetDailyPapersResponse, api, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_daily_papers(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.with_raw_response.get_daily_papers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = await response.parse()
        assert_matches_type(APIGetDailyPapersResponse, api, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_daily_papers(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.with_streaming_response.get_daily_papers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = await response.parse()
            assert_matches_type(APIGetDailyPapersResponse, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_dataset_tags(self, async_client: AsyncHuggingFace) -> None:
        api = await async_client.api.get_dataset_tags()
        assert_matches_type(APIGetDatasetTagsResponse, api, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_dataset_tags_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        api = await async_client.api.get_dataset_tags(
            type="task_categories",
        )
        assert_matches_type(APIGetDatasetTagsResponse, api, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_dataset_tags(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.with_raw_response.get_dataset_tags()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = await response.parse()
        assert_matches_type(APIGetDatasetTagsResponse, api, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_dataset_tags(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.with_streaming_response.get_dataset_tags() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = await response.parse()
            assert_matches_type(APIGetDatasetTagsResponse, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_model_tags(self, async_client: AsyncHuggingFace) -> None:
        api = await async_client.api.get_model_tags()
        assert_matches_type(APIGetModelTagsResponse, api, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_model_tags_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        api = await async_client.api.get_model_tags(
            type="pipeline_tag",
        )
        assert_matches_type(APIGetModelTagsResponse, api, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_model_tags(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.with_raw_response.get_model_tags()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = await response.parse()
        assert_matches_type(APIGetModelTagsResponse, api, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_model_tags(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.with_streaming_response.get_model_tags() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = await response.parse()
            assert_matches_type(APIGetModelTagsResponse, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_user_info(self, async_client: AsyncHuggingFace) -> None:
        api = await async_client.api.get_user_info()
        assert_matches_type(APIGetUserInfoResponse, api, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_user_info(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.with_raw_response.get_user_info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = await response.parse()
        assert_matches_type(APIGetUserInfoResponse, api, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_user_info(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.with_streaming_response.get_user_info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = await response.parse()
            assert_matches_type(APIGetUserInfoResponse, api, path=["response"])

        assert cast(Any, response.is_closed) is True
