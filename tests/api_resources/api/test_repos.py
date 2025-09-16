# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pyhfapi import HuggingFace, AsyncHuggingFace
from tests.utils import assert_matches_type
from pyhfapi.types.api import RepoCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRepos:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: HuggingFace) -> None:
        repo = client.api.repos.create(
            type="dataset",
        )
        assert_matches_type(RepoCreateResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: HuggingFace) -> None:
        repo = client.api.repos.create(
            type="dataset",
            files=[
                {
                    "content": "content",
                    "path": "path",
                    "encoding": "utf-8",
                }
            ],
            license="apache-2.0",
            license_link="LICENSE",
            license_name="26f1kl-.n.71",
            name="name",
            organization="organization",
            private=True,
            resource_group_id="ecc2efdd09bd231a9ad9bd2a",
        )
        assert_matches_type(RepoCreateResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: HuggingFace) -> None:
        response = client.api.repos.with_raw_response.create(
            type="dataset",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        repo = response.parse()
        assert_matches_type(RepoCreateResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: HuggingFace) -> None:
        with client.api.repos.with_streaming_response.create(
            type="dataset",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            repo = response.parse()
            assert_matches_type(RepoCreateResponse, repo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: HuggingFace) -> None:
        repo = client.api.repos.create()
        assert_matches_type(RepoCreateResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: HuggingFace) -> None:
        repo = client.api.repos.create(
            files=[
                {
                    "content": "content",
                    "path": "path",
                    "encoding": "utf-8",
                }
            ],
            license="apache-2.0",
            license_link="LICENSE",
            license_name="26f1kl-.n.71",
            name="name",
            organization="organization",
            private=True,
            resource_group_id="ecc2efdd09bd231a9ad9bd2a",
            type="model",
        )
        assert_matches_type(RepoCreateResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: HuggingFace) -> None:
        response = client.api.repos.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        repo = response.parse()
        assert_matches_type(RepoCreateResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: HuggingFace) -> None:
        with client.api.repos.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            repo = response.parse()
            assert_matches_type(RepoCreateResponse, repo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_3(self, client: HuggingFace) -> None:
        repo = client.api.repos.create(
            sdk="gradio",
            type="space",
        )
        assert_matches_type(RepoCreateResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: HuggingFace) -> None:
        repo = client.api.repos.create(
            sdk="gradio",
            type="space",
            dev_mode_enabled=True,
            files=[
                {
                    "content": "content",
                    "path": "path",
                    "encoding": "utf-8",
                }
            ],
            hardware="cpu-basic",
            license="apache-2.0",
            license_link="LICENSE",
            license_name="26f1kl-.n.71",
            name="name",
            organization="organization",
            private=True,
            resource_group_id="ecc2efdd09bd231a9ad9bd2a",
            sdk_version="sdkVersion",
            secrets=[
                {
                    "key": "key",
                    "value": "value",
                    "description": "description",
                }
            ],
            short_description="short_description",
            sleep_time_seconds=1,
            storage_tier="small",
            template="template",
            variables=[
                {
                    "key": "key",
                    "value": "value",
                    "description": "description",
                }
            ],
        )
        assert_matches_type(RepoCreateResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_3(self, client: HuggingFace) -> None:
        response = client.api.repos.with_raw_response.create(
            sdk="gradio",
            type="space",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        repo = response.parse()
        assert_matches_type(RepoCreateResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_3(self, client: HuggingFace) -> None:
        with client.api.repos.with_streaming_response.create(
            sdk="gradio",
            type="space",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            repo = response.parse()
            assert_matches_type(RepoCreateResponse, repo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_move(self, client: HuggingFace) -> None:
        repo = client.api.repos.move(
            from_repo="black-forest-labs/FLUX.1-dev",
            to_repo="toRepo",
        )
        assert repo is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_move_with_all_params(self, client: HuggingFace) -> None:
        repo = client.api.repos.move(
            from_repo="black-forest-labs/FLUX.1-dev",
            to_repo="toRepo",
            type="dataset",
        )
        assert repo is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_move(self, client: HuggingFace) -> None:
        response = client.api.repos.with_raw_response.move(
            from_repo="black-forest-labs/FLUX.1-dev",
            to_repo="toRepo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        repo = response.parse()
        assert repo is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_move(self, client: HuggingFace) -> None:
        with client.api.repos.with_streaming_response.move(
            from_repo="black-forest-labs/FLUX.1-dev",
            to_repo="toRepo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            repo = response.parse()
            assert repo is None

        assert cast(Any, response.is_closed) is True


class TestAsyncRepos:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncHuggingFace) -> None:
        repo = await async_client.api.repos.create(
            type="dataset",
        )
        assert_matches_type(RepoCreateResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncHuggingFace) -> None:
        repo = await async_client.api.repos.create(
            type="dataset",
            files=[
                {
                    "content": "content",
                    "path": "path",
                    "encoding": "utf-8",
                }
            ],
            license="apache-2.0",
            license_link="LICENSE",
            license_name="26f1kl-.n.71",
            name="name",
            organization="organization",
            private=True,
            resource_group_id="ecc2efdd09bd231a9ad9bd2a",
        )
        assert_matches_type(RepoCreateResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.repos.with_raw_response.create(
            type="dataset",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        repo = await response.parse()
        assert_matches_type(RepoCreateResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.repos.with_streaming_response.create(
            type="dataset",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            repo = await response.parse()
            assert_matches_type(RepoCreateResponse, repo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncHuggingFace) -> None:
        repo = await async_client.api.repos.create()
        assert_matches_type(RepoCreateResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncHuggingFace) -> None:
        repo = await async_client.api.repos.create(
            files=[
                {
                    "content": "content",
                    "path": "path",
                    "encoding": "utf-8",
                }
            ],
            license="apache-2.0",
            license_link="LICENSE",
            license_name="26f1kl-.n.71",
            name="name",
            organization="organization",
            private=True,
            resource_group_id="ecc2efdd09bd231a9ad9bd2a",
            type="model",
        )
        assert_matches_type(RepoCreateResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.repos.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        repo = await response.parse()
        assert_matches_type(RepoCreateResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.repos.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            repo = await response.parse()
            assert_matches_type(RepoCreateResponse, repo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncHuggingFace) -> None:
        repo = await async_client.api.repos.create(
            sdk="gradio",
            type="space",
        )
        assert_matches_type(RepoCreateResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncHuggingFace) -> None:
        repo = await async_client.api.repos.create(
            sdk="gradio",
            type="space",
            dev_mode_enabled=True,
            files=[
                {
                    "content": "content",
                    "path": "path",
                    "encoding": "utf-8",
                }
            ],
            hardware="cpu-basic",
            license="apache-2.0",
            license_link="LICENSE",
            license_name="26f1kl-.n.71",
            name="name",
            organization="organization",
            private=True,
            resource_group_id="ecc2efdd09bd231a9ad9bd2a",
            sdk_version="sdkVersion",
            secrets=[
                {
                    "key": "key",
                    "value": "value",
                    "description": "description",
                }
            ],
            short_description="short_description",
            sleep_time_seconds=1,
            storage_tier="small",
            template="template",
            variables=[
                {
                    "key": "key",
                    "value": "value",
                    "description": "description",
                }
            ],
        )
        assert_matches_type(RepoCreateResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.repos.with_raw_response.create(
            sdk="gradio",
            type="space",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        repo = await response.parse()
        assert_matches_type(RepoCreateResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.repos.with_streaming_response.create(
            sdk="gradio",
            type="space",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            repo = await response.parse()
            assert_matches_type(RepoCreateResponse, repo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_move(self, async_client: AsyncHuggingFace) -> None:
        repo = await async_client.api.repos.move(
            from_repo="black-forest-labs/FLUX.1-dev",
            to_repo="toRepo",
        )
        assert repo is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_move_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        repo = await async_client.api.repos.move(
            from_repo="black-forest-labs/FLUX.1-dev",
            to_repo="toRepo",
            type="dataset",
        )
        assert repo is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_move(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.repos.with_raw_response.move(
            from_repo="black-forest-labs/FLUX.1-dev",
            to_repo="toRepo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        repo = await response.parse()
        assert repo is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_move(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.repos.with_streaming_response.move(
            from_repo="black-forest-labs/FLUX.1-dev",
            to_repo="toRepo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            repo = await response.parse()
            assert repo is None

        assert cast(Any, response.is_closed) is True
