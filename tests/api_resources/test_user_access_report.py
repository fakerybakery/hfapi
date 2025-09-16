# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyhfapi import HuggingFace, AsyncHuggingFace
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUserAccessReport:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_export(self, client: HuggingFace) -> None:
        user_access_report = client.user_access_report.export(
            repo="repo",
            namespace="namespace",
        )
        assert_matches_type(str, user_access_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_export(self, client: HuggingFace) -> None:
        response = client.user_access_report.with_raw_response.export(
            repo="repo",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_access_report = response.parse()
        assert_matches_type(str, user_access_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_export(self, client: HuggingFace) -> None:
        with client.user_access_report.with_streaming_response.export(
            repo="repo",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_access_report = response.parse()
            assert_matches_type(str, user_access_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_export(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.user_access_report.with_raw_response.export(
                repo="repo",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.user_access_report.with_raw_response.export(
                repo="",
                namespace="namespace",
            )


class TestAsyncUserAccessReport:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_export(self, async_client: AsyncHuggingFace) -> None:
        user_access_report = await async_client.user_access_report.export(
            repo="repo",
            namespace="namespace",
        )
        assert_matches_type(str, user_access_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_export(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.user_access_report.with_raw_response.export(
            repo="repo",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_access_report = await response.parse()
        assert_matches_type(str, user_access_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_export(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.user_access_report.with_streaming_response.export(
            repo="repo",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_access_report = await response.parse()
            assert_matches_type(str, user_access_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_export(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.user_access_report.with_raw_response.export(
                repo="repo",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.user_access_report.with_raw_response.export(
                repo="",
                namespace="namespace",
            )
