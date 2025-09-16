# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hfpy import HuggingFace, AsyncHuggingFace

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPapers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search(self, client: HuggingFace) -> None:
        paper = client.api.papers.search()
        assert paper is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: HuggingFace) -> None:
        paper = client.api.papers.search(
            q="q",
        )
        assert paper is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: HuggingFace) -> None:
        response = client.api.papers.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = response.parse()
        assert paper is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: HuggingFace) -> None:
        with client.api.papers.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = response.parse()
            assert paper is None

        assert cast(Any, response.is_closed) is True


class TestAsyncPapers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncHuggingFace) -> None:
        paper = await async_client.api.papers.search()
        assert paper is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        paper = await async_client.api.papers.search(
            q="q",
        )
        assert paper is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.papers.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = await response.parse()
        assert paper is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.papers.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = await response.parse()
            assert paper is None

        assert cast(Any, response.is_closed) is True
