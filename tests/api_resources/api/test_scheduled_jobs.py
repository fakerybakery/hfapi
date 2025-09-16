# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hfpy import HuggingFace, AsyncHuggingFace
from tests.utils import assert_matches_type
from hfpy.types.api import (
    ScheduledJobListResponse,
    ScheduledJobCreateResponse,
    ScheduledJobRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScheduledJobs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HuggingFace) -> None:
        scheduled_job = client.api.scheduled_jobs.create(
            namespace="namespace",
            job_spec={"flavor": "cpu-basic"},
            schedule='S?oC"** * * * *',
        )
        assert_matches_type(ScheduledJobCreateResponse, scheduled_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HuggingFace) -> None:
        scheduled_job = client.api.scheduled_jobs.create(
            namespace="namespace",
            job_spec={
                "flavor": "cpu-basic",
                "arch": "amd64",
                "command": ["x"],
                "docker_image": "dockerImage",
                "environment": {"foo": "string"},
                "secrets": {"foo": "string"},
                "space_id": "spaceId",
                "timeout": 1,
            },
            schedule='S?oC"** * * * *',
            concurrency=True,
            suspend=True,
        )
        assert_matches_type(ScheduledJobCreateResponse, scheduled_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HuggingFace) -> None:
        response = client.api.scheduled_jobs.with_raw_response.create(
            namespace="namespace",
            job_spec={"flavor": "cpu-basic"},
            schedule='S?oC"** * * * *',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled_job = response.parse()
        assert_matches_type(ScheduledJobCreateResponse, scheduled_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HuggingFace) -> None:
        with client.api.scheduled_jobs.with_streaming_response.create(
            namespace="namespace",
            job_spec={"flavor": "cpu-basic"},
            schedule='S?oC"** * * * *',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled_job = response.parse()
            assert_matches_type(ScheduledJobCreateResponse, scheduled_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.scheduled_jobs.with_raw_response.create(
                namespace="",
                job_spec={"flavor": "cpu-basic"},
                schedule='S?oC"** * * * *',
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: HuggingFace) -> None:
        scheduled_job = client.api.scheduled_jobs.retrieve(
            scheduled_job_id="scheduledJobId",
            namespace="namespace",
        )
        assert_matches_type(ScheduledJobRetrieveResponse, scheduled_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: HuggingFace) -> None:
        response = client.api.scheduled_jobs.with_raw_response.retrieve(
            scheduled_job_id="scheduledJobId",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled_job = response.parse()
        assert_matches_type(ScheduledJobRetrieveResponse, scheduled_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: HuggingFace) -> None:
        with client.api.scheduled_jobs.with_streaming_response.retrieve(
            scheduled_job_id="scheduledJobId",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled_job = response.parse()
            assert_matches_type(ScheduledJobRetrieveResponse, scheduled_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.scheduled_jobs.with_raw_response.retrieve(
                scheduled_job_id="scheduledJobId",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scheduled_job_id` but received ''"):
            client.api.scheduled_jobs.with_raw_response.retrieve(
                scheduled_job_id="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HuggingFace) -> None:
        scheduled_job = client.api.scheduled_jobs.list(
            "namespace",
        )
        assert_matches_type(ScheduledJobListResponse, scheduled_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HuggingFace) -> None:
        response = client.api.scheduled_jobs.with_raw_response.list(
            "namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled_job = response.parse()
        assert_matches_type(ScheduledJobListResponse, scheduled_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HuggingFace) -> None:
        with client.api.scheduled_jobs.with_streaming_response.list(
            "namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled_job = response.parse()
            assert_matches_type(ScheduledJobListResponse, scheduled_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.scheduled_jobs.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HuggingFace) -> None:
        scheduled_job = client.api.scheduled_jobs.delete(
            scheduled_job_id="scheduledJobId",
            namespace="namespace",
        )
        assert scheduled_job is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HuggingFace) -> None:
        response = client.api.scheduled_jobs.with_raw_response.delete(
            scheduled_job_id="scheduledJobId",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled_job = response.parse()
        assert scheduled_job is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HuggingFace) -> None:
        with client.api.scheduled_jobs.with_streaming_response.delete(
            scheduled_job_id="scheduledJobId",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled_job = response.parse()
            assert scheduled_job is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.scheduled_jobs.with_raw_response.delete(
                scheduled_job_id="scheduledJobId",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scheduled_job_id` but received ''"):
            client.api.scheduled_jobs.with_raw_response.delete(
                scheduled_job_id="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_resume(self, client: HuggingFace) -> None:
        scheduled_job = client.api.scheduled_jobs.resume(
            scheduled_job_id="scheduledJobId",
            namespace="namespace",
        )
        assert scheduled_job is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_resume(self, client: HuggingFace) -> None:
        response = client.api.scheduled_jobs.with_raw_response.resume(
            scheduled_job_id="scheduledJobId",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled_job = response.parse()
        assert scheduled_job is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_resume(self, client: HuggingFace) -> None:
        with client.api.scheduled_jobs.with_streaming_response.resume(
            scheduled_job_id="scheduledJobId",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled_job = response.parse()
            assert scheduled_job is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_resume(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.scheduled_jobs.with_raw_response.resume(
                scheduled_job_id="scheduledJobId",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scheduled_job_id` but received ''"):
            client.api.scheduled_jobs.with_raw_response.resume(
                scheduled_job_id="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_suspend(self, client: HuggingFace) -> None:
        scheduled_job = client.api.scheduled_jobs.suspend(
            scheduled_job_id="scheduledJobId",
            namespace="namespace",
        )
        assert scheduled_job is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_suspend(self, client: HuggingFace) -> None:
        response = client.api.scheduled_jobs.with_raw_response.suspend(
            scheduled_job_id="scheduledJobId",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled_job = response.parse()
        assert scheduled_job is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_suspend(self, client: HuggingFace) -> None:
        with client.api.scheduled_jobs.with_streaming_response.suspend(
            scheduled_job_id="scheduledJobId",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled_job = response.parse()
            assert scheduled_job is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_suspend(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.scheduled_jobs.with_raw_response.suspend(
                scheduled_job_id="scheduledJobId",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scheduled_job_id` but received ''"):
            client.api.scheduled_jobs.with_raw_response.suspend(
                scheduled_job_id="",
                namespace="namespace",
            )


class TestAsyncScheduledJobs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHuggingFace) -> None:
        scheduled_job = await async_client.api.scheduled_jobs.create(
            namespace="namespace",
            job_spec={"flavor": "cpu-basic"},
            schedule='S?oC"** * * * *',
        )
        assert_matches_type(ScheduledJobCreateResponse, scheduled_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        scheduled_job = await async_client.api.scheduled_jobs.create(
            namespace="namespace",
            job_spec={
                "flavor": "cpu-basic",
                "arch": "amd64",
                "command": ["x"],
                "docker_image": "dockerImage",
                "environment": {"foo": "string"},
                "secrets": {"foo": "string"},
                "space_id": "spaceId",
                "timeout": 1,
            },
            schedule='S?oC"** * * * *',
            concurrency=True,
            suspend=True,
        )
        assert_matches_type(ScheduledJobCreateResponse, scheduled_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.scheduled_jobs.with_raw_response.create(
            namespace="namespace",
            job_spec={"flavor": "cpu-basic"},
            schedule='S?oC"** * * * *',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled_job = await response.parse()
        assert_matches_type(ScheduledJobCreateResponse, scheduled_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.scheduled_jobs.with_streaming_response.create(
            namespace="namespace",
            job_spec={"flavor": "cpu-basic"},
            schedule='S?oC"** * * * *',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled_job = await response.parse()
            assert_matches_type(ScheduledJobCreateResponse, scheduled_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.scheduled_jobs.with_raw_response.create(
                namespace="",
                job_spec={"flavor": "cpu-basic"},
                schedule='S?oC"** * * * *',
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncHuggingFace) -> None:
        scheduled_job = await async_client.api.scheduled_jobs.retrieve(
            scheduled_job_id="scheduledJobId",
            namespace="namespace",
        )
        assert_matches_type(ScheduledJobRetrieveResponse, scheduled_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.scheduled_jobs.with_raw_response.retrieve(
            scheduled_job_id="scheduledJobId",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled_job = await response.parse()
        assert_matches_type(ScheduledJobRetrieveResponse, scheduled_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.scheduled_jobs.with_streaming_response.retrieve(
            scheduled_job_id="scheduledJobId",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled_job = await response.parse()
            assert_matches_type(ScheduledJobRetrieveResponse, scheduled_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.scheduled_jobs.with_raw_response.retrieve(
                scheduled_job_id="scheduledJobId",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scheduled_job_id` but received ''"):
            await async_client.api.scheduled_jobs.with_raw_response.retrieve(
                scheduled_job_id="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHuggingFace) -> None:
        scheduled_job = await async_client.api.scheduled_jobs.list(
            "namespace",
        )
        assert_matches_type(ScheduledJobListResponse, scheduled_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.scheduled_jobs.with_raw_response.list(
            "namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled_job = await response.parse()
        assert_matches_type(ScheduledJobListResponse, scheduled_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.scheduled_jobs.with_streaming_response.list(
            "namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled_job = await response.parse()
            assert_matches_type(ScheduledJobListResponse, scheduled_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.scheduled_jobs.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHuggingFace) -> None:
        scheduled_job = await async_client.api.scheduled_jobs.delete(
            scheduled_job_id="scheduledJobId",
            namespace="namespace",
        )
        assert scheduled_job is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.scheduled_jobs.with_raw_response.delete(
            scheduled_job_id="scheduledJobId",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled_job = await response.parse()
        assert scheduled_job is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.scheduled_jobs.with_streaming_response.delete(
            scheduled_job_id="scheduledJobId",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled_job = await response.parse()
            assert scheduled_job is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.scheduled_jobs.with_raw_response.delete(
                scheduled_job_id="scheduledJobId",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scheduled_job_id` but received ''"):
            await async_client.api.scheduled_jobs.with_raw_response.delete(
                scheduled_job_id="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_resume(self, async_client: AsyncHuggingFace) -> None:
        scheduled_job = await async_client.api.scheduled_jobs.resume(
            scheduled_job_id="scheduledJobId",
            namespace="namespace",
        )
        assert scheduled_job is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_resume(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.scheduled_jobs.with_raw_response.resume(
            scheduled_job_id="scheduledJobId",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled_job = await response.parse()
        assert scheduled_job is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_resume(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.scheduled_jobs.with_streaming_response.resume(
            scheduled_job_id="scheduledJobId",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled_job = await response.parse()
            assert scheduled_job is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_resume(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.scheduled_jobs.with_raw_response.resume(
                scheduled_job_id="scheduledJobId",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scheduled_job_id` but received ''"):
            await async_client.api.scheduled_jobs.with_raw_response.resume(
                scheduled_job_id="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_suspend(self, async_client: AsyncHuggingFace) -> None:
        scheduled_job = await async_client.api.scheduled_jobs.suspend(
            scheduled_job_id="scheduledJobId",
            namespace="namespace",
        )
        assert scheduled_job is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_suspend(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.scheduled_jobs.with_raw_response.suspend(
            scheduled_job_id="scheduledJobId",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled_job = await response.parse()
        assert scheduled_job is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_suspend(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.scheduled_jobs.with_streaming_response.suspend(
            scheduled_job_id="scheduledJobId",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled_job = await response.parse()
            assert scheduled_job is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_suspend(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.scheduled_jobs.with_raw_response.suspend(
                scheduled_job_id="scheduledJobId",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scheduled_job_id` but received ''"):
            await async_client.api.scheduled_jobs.with_raw_response.suspend(
                scheduled_job_id="",
                namespace="namespace",
            )
