# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hfpy import HuggingFace, AsyncHuggingFace

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVariables:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HuggingFace) -> None:
        variable = client.api.spaces.variables.delete(
            repo="repo",
            namespace="namespace",
            key="key",
        )
        assert variable is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HuggingFace) -> None:
        response = client.api.spaces.variables.with_raw_response.delete(
            repo="repo",
            namespace="namespace",
            key="key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variable = response.parse()
        assert variable is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HuggingFace) -> None:
        with client.api.spaces.variables.with_streaming_response.delete(
            repo="repo",
            namespace="namespace",
            key="key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variable = response.parse()
            assert variable is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.spaces.variables.with_raw_response.delete(
                repo="repo",
                namespace="",
                key="key",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.spaces.variables.with_raw_response.delete(
                repo="",
                namespace="namespace",
                key="key",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upsert(self, client: HuggingFace) -> None:
        variable = client.api.spaces.variables.upsert(
            repo="repo",
            namespace="namespace",
            key="key",
        )
        assert variable is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upsert_with_all_params(self, client: HuggingFace) -> None:
        variable = client.api.spaces.variables.upsert(
            repo="repo",
            namespace="namespace",
            key="key",
            description="description",
            value="value",
        )
        assert variable is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upsert(self, client: HuggingFace) -> None:
        response = client.api.spaces.variables.with_raw_response.upsert(
            repo="repo",
            namespace="namespace",
            key="key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variable = response.parse()
        assert variable is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upsert(self, client: HuggingFace) -> None:
        with client.api.spaces.variables.with_streaming_response.upsert(
            repo="repo",
            namespace="namespace",
            key="key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variable = response.parse()
            assert variable is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_upsert(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.spaces.variables.with_raw_response.upsert(
                repo="repo",
                namespace="",
                key="key",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.spaces.variables.with_raw_response.upsert(
                repo="",
                namespace="namespace",
                key="key",
            )


class TestAsyncVariables:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHuggingFace) -> None:
        variable = await async_client.api.spaces.variables.delete(
            repo="repo",
            namespace="namespace",
            key="key",
        )
        assert variable is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.spaces.variables.with_raw_response.delete(
            repo="repo",
            namespace="namespace",
            key="key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variable = await response.parse()
        assert variable is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.spaces.variables.with_streaming_response.delete(
            repo="repo",
            namespace="namespace",
            key="key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variable = await response.parse()
            assert variable is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.spaces.variables.with_raw_response.delete(
                repo="repo",
                namespace="",
                key="key",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.spaces.variables.with_raw_response.delete(
                repo="",
                namespace="namespace",
                key="key",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncHuggingFace) -> None:
        variable = await async_client.api.spaces.variables.upsert(
            repo="repo",
            namespace="namespace",
            key="key",
        )
        assert variable is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        variable = await async_client.api.spaces.variables.upsert(
            repo="repo",
            namespace="namespace",
            key="key",
            description="description",
            value="value",
        )
        assert variable is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.spaces.variables.with_raw_response.upsert(
            repo="repo",
            namespace="namespace",
            key="key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variable = await response.parse()
        assert variable is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.spaces.variables.with_streaming_response.upsert(
            repo="repo",
            namespace="namespace",
            key="key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variable = await response.parse()
            assert variable is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_upsert(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.spaces.variables.with_raw_response.upsert(
                repo="repo",
                namespace="",
                key="key",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.spaces.variables.with_raw_response.upsert(
                repo="",
                namespace="namespace",
                key="key",
            )
