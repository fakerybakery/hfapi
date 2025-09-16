# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hfpy import HuggingFace, AsyncHuggingFace
from tests.utils import assert_matches_type
from hfpy.types.oauth import UserinfoUpdateResponse, UserinfoRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUserinfo:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: HuggingFace) -> None:
        userinfo = client.oauth.userinfo.retrieve()
        assert_matches_type(UserinfoRetrieveResponse, userinfo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: HuggingFace) -> None:
        response = client.oauth.userinfo.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        userinfo = response.parse()
        assert_matches_type(UserinfoRetrieveResponse, userinfo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: HuggingFace) -> None:
        with client.oauth.userinfo.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            userinfo = response.parse()
            assert_matches_type(UserinfoRetrieveResponse, userinfo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: HuggingFace) -> None:
        userinfo = client.oauth.userinfo.update()
        assert_matches_type(UserinfoUpdateResponse, userinfo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HuggingFace) -> None:
        response = client.oauth.userinfo.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        userinfo = response.parse()
        assert_matches_type(UserinfoUpdateResponse, userinfo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HuggingFace) -> None:
        with client.oauth.userinfo.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            userinfo = response.parse()
            assert_matches_type(UserinfoUpdateResponse, userinfo, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUserinfo:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncHuggingFace) -> None:
        userinfo = await async_client.oauth.userinfo.retrieve()
        assert_matches_type(UserinfoRetrieveResponse, userinfo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.oauth.userinfo.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        userinfo = await response.parse()
        assert_matches_type(UserinfoRetrieveResponse, userinfo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.oauth.userinfo.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            userinfo = await response.parse()
            assert_matches_type(UserinfoRetrieveResponse, userinfo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHuggingFace) -> None:
        userinfo = await async_client.oauth.userinfo.update()
        assert_matches_type(UserinfoUpdateResponse, userinfo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.oauth.userinfo.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        userinfo = await response.parse()
        assert_matches_type(UserinfoUpdateResponse, userinfo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.oauth.userinfo.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            userinfo = await response.parse()
            assert_matches_type(UserinfoUpdateResponse, userinfo, path=["response"])

        assert cast(Any, response.is_closed) is True
