# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hfpy import HuggingFace, AsyncHuggingFace
from tests.utils import assert_matches_type
from hfpy.types.api import DocSearchResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search(self, client: HuggingFace) -> None:
        doc = client.api.docs.search(
            q="q",
        )
        assert_matches_type(DocSearchResponse, doc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: HuggingFace) -> None:
        doc = client.api.docs.search(
            q="q",
            limit=1,
            product="hub",
        )
        assert_matches_type(DocSearchResponse, doc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: HuggingFace) -> None:
        response = client.api.docs.with_raw_response.search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        doc = response.parse()
        assert_matches_type(DocSearchResponse, doc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: HuggingFace) -> None:
        with client.api.docs.with_streaming_response.search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            doc = response.parse()
            assert_matches_type(DocSearchResponse, doc, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDocs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncHuggingFace) -> None:
        doc = await async_client.api.docs.search(
            q="q",
        )
        assert_matches_type(DocSearchResponse, doc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        doc = await async_client.api.docs.search(
            q="q",
            limit=1,
            product="hub",
        )
        assert_matches_type(DocSearchResponse, doc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.docs.with_raw_response.search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        doc = await response.parse()
        assert_matches_type(DocSearchResponse, doc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.docs.with_streaming_response.search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            doc = await response.parse()
            assert_matches_type(DocSearchResponse, doc, path=["response"])

        assert cast(Any, response.is_closed) is True
