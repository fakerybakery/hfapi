# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyhfapi import HuggingFace, AsyncHuggingFace
from tests.utils import assert_matches_type
from pyhfapi._utils import parse_datetime
from pyhfapi.types.api import SettingGetMcpResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_mcp(self, client: HuggingFace) -> None:
        setting = client.api.settings.get_mcp()
        assert_matches_type(SettingGetMcpResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_mcp(self, client: HuggingFace) -> None:
        response = client.api.settings.with_raw_response.get_mcp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(SettingGetMcpResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_mcp(self, client: HuggingFace) -> None:
        with client.api.settings.with_streaming_response.get_mcp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(SettingGetMcpResponse, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_notifications(self, client: HuggingFace) -> None:
        setting = client.api.settings.update_notifications(
            notifications={},
        )
        assert setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_notifications_with_all_params(self, client: HuggingFace) -> None:
        setting = client.api.settings.update_notifications(
            notifications={
                "announcements": True,
                "arxiv_paper_activity": True,
                "daily_papers_digest": True,
                "discussions_participating": True,
                "discussions_watched": True,
                "gated_user_access_request": True,
                "launch_autonlp": True,
                "launch_prepaid_credits": True,
                "launch_spaces": True,
                "launch_training_cluster": True,
                "org_request": True,
                "org_suggestions": True,
                "org_suggestions_to_create": True,
                "org_verified_suggestions": True,
                "posts_participating": True,
                "product_updates_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "secret_detected": True,
                "user_follows": True,
                "web_discussions_participating": True,
                "web_discussions_watched": True,
                "web_posts_participating": True,
            },
            prepaid_amount="prepaidAmount",
        )
        assert setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_notifications(self, client: HuggingFace) -> None:
        response = client.api.settings.with_raw_response.update_notifications(
            notifications={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_notifications(self, client: HuggingFace) -> None:
        with client.api.settings.with_streaming_response.update_notifications(
            notifications={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_watch(self, client: HuggingFace) -> None:
        setting = client.api.settings.update_watch()
        assert setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_watch_with_all_params(self, client: HuggingFace) -> None:
        setting = client.api.settings.update_watch(
            add=[
                {
                    "id": "id",
                    "type": "org",
                }
            ],
            delete=[
                {
                    "id": "id",
                    "type": "org",
                }
            ],
        )
        assert setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_watch(self, client: HuggingFace) -> None:
        response = client.api.settings.with_raw_response.update_watch()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_watch(self, client: HuggingFace) -> None:
        with client.api.settings.with_streaming_response.update_watch() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True


class TestAsyncSettings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_mcp(self, async_client: AsyncHuggingFace) -> None:
        setting = await async_client.api.settings.get_mcp()
        assert_matches_type(SettingGetMcpResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_mcp(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.settings.with_raw_response.get_mcp()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(SettingGetMcpResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_mcp(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.settings.with_streaming_response.get_mcp() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(SettingGetMcpResponse, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_notifications(self, async_client: AsyncHuggingFace) -> None:
        setting = await async_client.api.settings.update_notifications(
            notifications={},
        )
        assert setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_notifications_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        setting = await async_client.api.settings.update_notifications(
            notifications={
                "announcements": True,
                "arxiv_paper_activity": True,
                "daily_papers_digest": True,
                "discussions_participating": True,
                "discussions_watched": True,
                "gated_user_access_request": True,
                "launch_autonlp": True,
                "launch_prepaid_credits": True,
                "launch_spaces": True,
                "launch_training_cluster": True,
                "org_request": True,
                "org_suggestions": True,
                "org_suggestions_to_create": True,
                "org_verified_suggestions": True,
                "posts_participating": True,
                "product_updates_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "secret_detected": True,
                "user_follows": True,
                "web_discussions_participating": True,
                "web_discussions_watched": True,
                "web_posts_participating": True,
            },
            prepaid_amount="prepaidAmount",
        )
        assert setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_notifications(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.settings.with_raw_response.update_notifications(
            notifications={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_notifications(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.settings.with_streaming_response.update_notifications(
            notifications={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_watch(self, async_client: AsyncHuggingFace) -> None:
        setting = await async_client.api.settings.update_watch()
        assert setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_watch_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        setting = await async_client.api.settings.update_watch(
            add=[
                {
                    "id": "id",
                    "type": "org",
                }
            ],
            delete=[
                {
                    "id": "id",
                    "type": "org",
                }
            ],
        )
        assert setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_watch(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.settings.with_raw_response.update_watch()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_watch(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.settings.with_streaming_response.update_watch() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True
