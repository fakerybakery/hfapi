# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyhfapi import HuggingFace, AsyncHuggingFace
from tests.utils import assert_matches_type
from pyhfapi._utils import parse_datetime
from pyhfapi.types.api import NotificationListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNotifications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HuggingFace) -> None:
        notification = client.api.notifications.list()
        assert_matches_type(NotificationListResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HuggingFace) -> None:
        notification = client.api.notifications.list(
            article_id="articleId",
            last_update=parse_datetime("2019-12-27T18:11:19.117Z"),
            mention="all",
            p=0,
            paper_id="paperId",
            post_author="postAuthor",
            read_status="all",
            repo_name="repoName",
            repo_type="dataset",
        )
        assert_matches_type(NotificationListResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HuggingFace) -> None:
        response = client.api.notifications.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert_matches_type(NotificationListResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HuggingFace) -> None:
        with client.api.notifications.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert_matches_type(NotificationListResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HuggingFace) -> None:
        notification = client.api.notifications.delete()
        assert notification is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: HuggingFace) -> None:
        notification = client.api.notifications.delete(
            apply_to_all={},
            article_id="articleId",
            last_update=parse_datetime("2019-12-27T18:11:19.117Z"),
            mention="all",
            p=0,
            paper_id="paperId",
            post_author="postAuthor",
            read_status="all",
            repo_name="repoName",
            repo_type="dataset",
            discussion_ids=["ecc2efdd09bd231a9ad9bd2a"],
        )
        assert notification is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HuggingFace) -> None:
        response = client.api.notifications.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert notification is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HuggingFace) -> None:
        with client.api.notifications.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert notification is None

        assert cast(Any, response.is_closed) is True


class TestAsyncNotifications:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHuggingFace) -> None:
        notification = await async_client.api.notifications.list()
        assert_matches_type(NotificationListResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        notification = await async_client.api.notifications.list(
            article_id="articleId",
            last_update=parse_datetime("2019-12-27T18:11:19.117Z"),
            mention="all",
            p=0,
            paper_id="paperId",
            post_author="postAuthor",
            read_status="all",
            repo_name="repoName",
            repo_type="dataset",
        )
        assert_matches_type(NotificationListResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.notifications.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert_matches_type(NotificationListResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.notifications.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert_matches_type(NotificationListResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHuggingFace) -> None:
        notification = await async_client.api.notifications.delete()
        assert notification is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        notification = await async_client.api.notifications.delete(
            apply_to_all={},
            article_id="articleId",
            last_update=parse_datetime("2019-12-27T18:11:19.117Z"),
            mention="all",
            p=0,
            paper_id="paperId",
            post_author="postAuthor",
            read_status="all",
            repo_name="repoName",
            repo_type="dataset",
            discussion_ids=["ecc2efdd09bd231a9ad9bd2a"],
        )
        assert notification is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.notifications.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert notification is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.notifications.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert notification is None

        assert cast(Any, response.is_closed) is True
