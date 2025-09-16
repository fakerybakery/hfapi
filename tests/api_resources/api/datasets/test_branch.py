# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyhfapi import HuggingFace, AsyncHuggingFace

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBranch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HuggingFace) -> None:
        branch = client.api.datasets.branch.create(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )
        assert branch is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HuggingFace) -> None:
        branch = client.api.datasets.branch.create(
            rev="rev",
            namespace="namespace",
            repo="repo",
            empty_branch=True,
            overwrite=True,
            starting_point="startingPoint",
        )
        assert branch is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HuggingFace) -> None:
        response = client.api.datasets.branch.with_raw_response.create(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        branch = response.parse()
        assert branch is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HuggingFace) -> None:
        with client.api.datasets.branch.with_streaming_response.create(
            rev="rev",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            branch = response.parse()
            assert branch is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.datasets.branch.with_raw_response.create(
                rev="rev",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.datasets.branch.with_raw_response.create(
                rev="rev",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            client.api.datasets.branch.with_raw_response.create(
                rev="",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HuggingFace) -> None:
        branch = client.api.datasets.branch.delete(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )
        assert branch is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HuggingFace) -> None:
        response = client.api.datasets.branch.with_raw_response.delete(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        branch = response.parse()
        assert branch is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HuggingFace) -> None:
        with client.api.datasets.branch.with_streaming_response.delete(
            rev="rev",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            branch = response.parse()
            assert branch is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.datasets.branch.with_raw_response.delete(
                rev="rev",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            client.api.datasets.branch.with_raw_response.delete(
                rev="rev",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            client.api.datasets.branch.with_raw_response.delete(
                rev="",
                namespace="namespace",
                repo="repo",
            )


class TestAsyncBranch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHuggingFace) -> None:
        branch = await async_client.api.datasets.branch.create(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )
        assert branch is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        branch = await async_client.api.datasets.branch.create(
            rev="rev",
            namespace="namespace",
            repo="repo",
            empty_branch=True,
            overwrite=True,
            starting_point="startingPoint",
        )
        assert branch is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.datasets.branch.with_raw_response.create(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        branch = await response.parse()
        assert branch is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.datasets.branch.with_streaming_response.create(
            rev="rev",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            branch = await response.parse()
            assert branch is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.datasets.branch.with_raw_response.create(
                rev="rev",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.datasets.branch.with_raw_response.create(
                rev="rev",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            await async_client.api.datasets.branch.with_raw_response.create(
                rev="",
                namespace="namespace",
                repo="repo",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHuggingFace) -> None:
        branch = await async_client.api.datasets.branch.delete(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )
        assert branch is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.datasets.branch.with_raw_response.delete(
            rev="rev",
            namespace="namespace",
            repo="repo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        branch = await response.parse()
        assert branch is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.datasets.branch.with_streaming_response.delete(
            rev="rev",
            namespace="namespace",
            repo="repo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            branch = await response.parse()
            assert branch is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.datasets.branch.with_raw_response.delete(
                rev="rev",
                namespace="",
                repo="repo",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repo` but received ''"):
            await async_client.api.datasets.branch.with_raw_response.delete(
                rev="rev",
                namespace="namespace",
                repo="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rev` but received ''"):
            await async_client.api.datasets.branch.with_raw_response.delete(
                rev="",
                namespace="namespace",
                repo="repo",
            )
