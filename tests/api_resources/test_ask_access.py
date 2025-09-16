# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hfpy import HuggingFace, AsyncHuggingFace

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAskAccess:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    def test_method_request(self, client: HuggingFace) -> None:
        ask_access = client.ask_access.request(
            repo="repo",
            namespace="namespace",
        )
        assert ask_access is None

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    def test_method_request_with_all_params(self, client: HuggingFace) -> None:
        ask_access = client.ask_access.request(
            repo="repo",
            namespace="namespace",
            body={"foo": "bar"},
        )
        assert ask_access is None

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    def test_raw_response_request(self, client: HuggingFace) -> None:
        response = client.ask_access.with_raw_response.request(
            repo="repo",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ask_access = response.parse()
        assert ask_access is None

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    def test_streaming_response_request(self, client: HuggingFace) -> None:
        with client.ask_access.with_streaming_response.request(
            repo="repo",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ask_access = response.parse()
            assert ask_access is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    def test_path_params_request(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.ask_access.with_raw_response.request(
                repo="repo",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.ask_access.with_raw_response.request(
                repo="",
                namespace="namespace",
            )


class TestAsyncAskAccess:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    async def test_method_request(self, async_client: AsyncHuggingFace) -> None:
        ask_access = await async_client.ask_access.request(
            repo="repo",
            namespace="namespace",
        )
        assert ask_access is None

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    async def test_method_request_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        ask_access = await async_client.ask_access.request(
            repo="repo",
            namespace="namespace",
            body={"foo": "bar"},
        )
        assert ask_access is None

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    async def test_raw_response_request(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.ask_access.with_raw_response.request(
            repo="repo",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ask_access = await response.parse()
        assert ask_access is None

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    async def test_streaming_response_request(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.ask_access.with_streaming_response.request(
            repo="repo",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ask_access = await response.parse()
            assert ask_access is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    async def test_path_params_request(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.ask_access.with_raw_response.request(
                repo="repo",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.ask_access.with_raw_response.request(
                repo="",
                namespace="namespace",
            )
