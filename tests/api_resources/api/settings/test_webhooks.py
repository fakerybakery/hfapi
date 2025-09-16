# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hfpy import HuggingFace, AsyncHuggingFace
from tests.utils import assert_matches_type
from hfpy.types.api.settings import (
    WebhookListResponse,
    WebhookCreateResponse,
    WebhookToggleResponse,
    WebhookUpdateResponse,
    WebhookRetrieveResponse,
    WebhookReplayLogResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HuggingFace) -> None:
        webhook = client.api.settings.webhooks.create(
            domains=["repo"],
            watched=[
                {
                    "name": "name",
                    "type": "dataset",
                }
            ],
        )
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HuggingFace) -> None:
        webhook = client.api.settings.webhooks.create(
            domains=["repo"],
            watched=[
                {
                    "name": "name",
                    "type": "dataset",
                }
            ],
            job={
                "flavor": "cpu-basic",
                "arch": "amd64",
                "arguments": ["string"],
                "command": ["string"],
                "docker_image": "dockerImage",
                "environment": {"foo": "string"},
                "secrets": {"foo": "bar"},
                "space_id": "spaceId",
                "tags": ["string"],
                "timeout": 0,
            },
            secret="secret",
            url="url",
        )
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HuggingFace) -> None:
        response = client.api.settings.webhooks.with_raw_response.create(
            domains=["repo"],
            watched=[
                {
                    "name": "name",
                    "type": "dataset",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HuggingFace) -> None:
        with client.api.settings.webhooks.with_streaming_response.create(
            domains=["repo"],
            watched=[
                {
                    "name": "name",
                    "type": "dataset",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: HuggingFace) -> None:
        webhook = client.api.settings.webhooks.retrieve(
            "webhookId",
        )
        assert_matches_type(WebhookRetrieveResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: HuggingFace) -> None:
        response = client.api.settings.webhooks.with_raw_response.retrieve(
            "webhookId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookRetrieveResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: HuggingFace) -> None:
        with client.api.settings.webhooks.with_streaming_response.retrieve(
            "webhookId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookRetrieveResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.api.settings.webhooks.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: HuggingFace) -> None:
        webhook = client.api.settings.webhooks.update(
            webhook_id="webhookId",
            domains=["repo"],
            watched=[
                {
                    "name": "name",
                    "type": "dataset",
                }
            ],
        )
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: HuggingFace) -> None:
        webhook = client.api.settings.webhooks.update(
            webhook_id="webhookId",
            domains=["repo"],
            watched=[
                {
                    "name": "name",
                    "type": "dataset",
                }
            ],
            job={
                "flavor": "cpu-basic",
                "arch": "amd64",
                "arguments": ["string"],
                "command": ["string"],
                "docker_image": "dockerImage",
                "environment": {"foo": "string"},
                "secrets": {"foo": "bar"},
                "space_id": "spaceId",
                "tags": ["string"],
                "timeout": 0,
            },
            secret="secret",
            url="url",
        )
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HuggingFace) -> None:
        response = client.api.settings.webhooks.with_raw_response.update(
            webhook_id="webhookId",
            domains=["repo"],
            watched=[
                {
                    "name": "name",
                    "type": "dataset",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HuggingFace) -> None:
        with client.api.settings.webhooks.with_streaming_response.update(
            webhook_id="webhookId",
            domains=["repo"],
            watched=[
                {
                    "name": "name",
                    "type": "dataset",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.api.settings.webhooks.with_raw_response.update(
                webhook_id="",
                domains=["repo"],
                watched=[
                    {
                        "name": "name",
                        "type": "dataset",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HuggingFace) -> None:
        webhook = client.api.settings.webhooks.list()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HuggingFace) -> None:
        response = client.api.settings.webhooks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HuggingFace) -> None:
        with client.api.settings.webhooks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookListResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HuggingFace) -> None:
        webhook = client.api.settings.webhooks.delete(
            "webhookId",
        )
        assert_matches_type(object, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HuggingFace) -> None:
        response = client.api.settings.webhooks.with_raw_response.delete(
            "webhookId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(object, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HuggingFace) -> None:
        with client.api.settings.webhooks.with_streaming_response.delete(
            "webhookId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(object, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.api.settings.webhooks.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_replay_log(self, client: HuggingFace) -> None:
        webhook = client.api.settings.webhooks.replay_log(
            log_id="logId",
            webhook_id="webhookId",
        )
        assert_matches_type(WebhookReplayLogResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_replay_log(self, client: HuggingFace) -> None:
        response = client.api.settings.webhooks.with_raw_response.replay_log(
            log_id="logId",
            webhook_id="webhookId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookReplayLogResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_replay_log(self, client: HuggingFace) -> None:
        with client.api.settings.webhooks.with_streaming_response.replay_log(
            log_id="logId",
            webhook_id="webhookId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookReplayLogResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_replay_log(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.api.settings.webhooks.with_raw_response.replay_log(
                log_id="logId",
                webhook_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `log_id` but received ''"):
            client.api.settings.webhooks.with_raw_response.replay_log(
                log_id="",
                webhook_id="webhookId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_toggle(self, client: HuggingFace) -> None:
        webhook = client.api.settings.webhooks.toggle(
            action="enable",
            webhook_id="webhookId",
        )
        assert_matches_type(WebhookToggleResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_toggle(self, client: HuggingFace) -> None:
        response = client.api.settings.webhooks.with_raw_response.toggle(
            action="enable",
            webhook_id="webhookId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookToggleResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_toggle(self, client: HuggingFace) -> None:
        with client.api.settings.webhooks.with_streaming_response.toggle(
            action="enable",
            webhook_id="webhookId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookToggleResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_toggle(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.api.settings.webhooks.with_raw_response.toggle(
                action="enable",
                webhook_id="",
            )


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHuggingFace) -> None:
        webhook = await async_client.api.settings.webhooks.create(
            domains=["repo"],
            watched=[
                {
                    "name": "name",
                    "type": "dataset",
                }
            ],
        )
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        webhook = await async_client.api.settings.webhooks.create(
            domains=["repo"],
            watched=[
                {
                    "name": "name",
                    "type": "dataset",
                }
            ],
            job={
                "flavor": "cpu-basic",
                "arch": "amd64",
                "arguments": ["string"],
                "command": ["string"],
                "docker_image": "dockerImage",
                "environment": {"foo": "string"},
                "secrets": {"foo": "bar"},
                "space_id": "spaceId",
                "tags": ["string"],
                "timeout": 0,
            },
            secret="secret",
            url="url",
        )
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.settings.webhooks.with_raw_response.create(
            domains=["repo"],
            watched=[
                {
                    "name": "name",
                    "type": "dataset",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.settings.webhooks.with_streaming_response.create(
            domains=["repo"],
            watched=[
                {
                    "name": "name",
                    "type": "dataset",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncHuggingFace) -> None:
        webhook = await async_client.api.settings.webhooks.retrieve(
            "webhookId",
        )
        assert_matches_type(WebhookRetrieveResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.settings.webhooks.with_raw_response.retrieve(
            "webhookId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookRetrieveResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.settings.webhooks.with_streaming_response.retrieve(
            "webhookId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookRetrieveResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.api.settings.webhooks.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHuggingFace) -> None:
        webhook = await async_client.api.settings.webhooks.update(
            webhook_id="webhookId",
            domains=["repo"],
            watched=[
                {
                    "name": "name",
                    "type": "dataset",
                }
            ],
        )
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        webhook = await async_client.api.settings.webhooks.update(
            webhook_id="webhookId",
            domains=["repo"],
            watched=[
                {
                    "name": "name",
                    "type": "dataset",
                }
            ],
            job={
                "flavor": "cpu-basic",
                "arch": "amd64",
                "arguments": ["string"],
                "command": ["string"],
                "docker_image": "dockerImage",
                "environment": {"foo": "string"},
                "secrets": {"foo": "bar"},
                "space_id": "spaceId",
                "tags": ["string"],
                "timeout": 0,
            },
            secret="secret",
            url="url",
        )
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.settings.webhooks.with_raw_response.update(
            webhook_id="webhookId",
            domains=["repo"],
            watched=[
                {
                    "name": "name",
                    "type": "dataset",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.settings.webhooks.with_streaming_response.update(
            webhook_id="webhookId",
            domains=["repo"],
            watched=[
                {
                    "name": "name",
                    "type": "dataset",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.api.settings.webhooks.with_raw_response.update(
                webhook_id="",
                domains=["repo"],
                watched=[
                    {
                        "name": "name",
                        "type": "dataset",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHuggingFace) -> None:
        webhook = await async_client.api.settings.webhooks.list()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.settings.webhooks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.settings.webhooks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookListResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHuggingFace) -> None:
        webhook = await async_client.api.settings.webhooks.delete(
            "webhookId",
        )
        assert_matches_type(object, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.settings.webhooks.with_raw_response.delete(
            "webhookId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(object, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.settings.webhooks.with_streaming_response.delete(
            "webhookId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(object, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.api.settings.webhooks.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_replay_log(self, async_client: AsyncHuggingFace) -> None:
        webhook = await async_client.api.settings.webhooks.replay_log(
            log_id="logId",
            webhook_id="webhookId",
        )
        assert_matches_type(WebhookReplayLogResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_replay_log(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.settings.webhooks.with_raw_response.replay_log(
            log_id="logId",
            webhook_id="webhookId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookReplayLogResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_replay_log(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.settings.webhooks.with_streaming_response.replay_log(
            log_id="logId",
            webhook_id="webhookId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookReplayLogResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_replay_log(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.api.settings.webhooks.with_raw_response.replay_log(
                log_id="logId",
                webhook_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `log_id` but received ''"):
            await async_client.api.settings.webhooks.with_raw_response.replay_log(
                log_id="",
                webhook_id="webhookId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_toggle(self, async_client: AsyncHuggingFace) -> None:
        webhook = await async_client.api.settings.webhooks.toggle(
            action="enable",
            webhook_id="webhookId",
        )
        assert_matches_type(WebhookToggleResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_toggle(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.settings.webhooks.with_raw_response.toggle(
            action="enable",
            webhook_id="webhookId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookToggleResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_toggle(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.settings.webhooks.with_streaming_response.toggle(
            action="enable",
            webhook_id="webhookId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookToggleResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_toggle(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.api.settings.webhooks.with_raw_response.toggle(
                action="enable",
                webhook_id="",
            )
