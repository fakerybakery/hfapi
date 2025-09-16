# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyhfapi import HuggingFace, AsyncHuggingFace
from tests.utils import assert_matches_type
from pyhfapi.types import ResolveFileResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResolve:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_file(self, client: HuggingFace) -> None:
        resolve = client.resolve.file(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )
        assert_matches_type(ResolveFileResponse, resolve, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_file_with_all_params(self, client: HuggingFace) -> None:
        resolve = client.resolve.file(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
            accept="application/vnd.xet-fileinfo+json",
            range="Range",
        )
        assert_matches_type(ResolveFileResponse, resolve, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_file(self, client: HuggingFace) -> None:
        response = client.resolve.with_raw_response.file(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolve = response.parse()
        assert_matches_type(ResolveFileResponse, resolve, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_file(self, client: HuggingFace) -> None:
        with client.resolve.with_streaming_response.file(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolve = response.parse()
            assert_matches_type(ResolveFileResponse, resolve, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_file(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.resolve.with_raw_response.file(
                path="path",
                namespace="",
                repo="repo",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.resolve.with_raw_response.file(
                path="path",
                namespace="namespace",
                repo="",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            client.resolve.with_raw_response.file(
                path="path",
                namespace="namespace",
                repo="repo",
                rev="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            client.resolve.with_raw_response.file(
                path="",
                namespace="namespace",
                repo="repo",
                rev="rev",
            )


class TestAsyncResolve:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_file(self, async_client: AsyncHuggingFace) -> None:
        resolve = await async_client.resolve.file(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )
        assert_matches_type(ResolveFileResponse, resolve, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_file_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        resolve = await async_client.resolve.file(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
            accept="application/vnd.xet-fileinfo+json",
            range="Range",
        )
        assert_matches_type(ResolveFileResponse, resolve, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_file(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.resolve.with_raw_response.file(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolve = await response.parse()
        assert_matches_type(ResolveFileResponse, resolve, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_file(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.resolve.with_streaming_response.file(
            path="path",
            namespace="namespace",
            repo="repo",
            rev="rev",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolve = await response.parse()
            assert_matches_type(ResolveFileResponse, resolve, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_file(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.resolve.with_raw_response.file(
                path="path",
                namespace="",
                repo="repo",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.resolve.with_raw_response.file(
                path="path",
                namespace="namespace",
                repo="",
                rev="rev",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            await async_client.resolve.with_raw_response.file(
                path="path",
                namespace="namespace",
                repo="repo",
                rev="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            await async_client.resolve.with_raw_response.file(
                path="",
                namespace="namespace",
                repo="repo",
                rev="rev",
            )
