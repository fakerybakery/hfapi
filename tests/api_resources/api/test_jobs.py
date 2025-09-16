# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hfpy import HuggingFace, AsyncHuggingFace
from tests.utils import assert_matches_type
from hfpy.types.api import JobListResponse, JobStartResponse, JobCancelResponse, JobRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJobs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: HuggingFace) -> None:
        job = client.api.jobs.retrieve(
            job_id="jobId",
            namespace="namespace",
        )
        assert_matches_type(JobRetrieveResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: HuggingFace) -> None:
        response = client.api.jobs.with_raw_response.retrieve(
            job_id="jobId",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobRetrieveResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: HuggingFace) -> None:
        with client.api.jobs.with_streaming_response.retrieve(
            job_id="jobId",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobRetrieveResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.jobs.with_raw_response.retrieve(
                job_id="jobId",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.api.jobs.with_raw_response.retrieve(
                job_id="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HuggingFace) -> None:
        job = client.api.jobs.list(
            "namespace",
        )
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HuggingFace) -> None:
        response = client.api.jobs.with_raw_response.list(
            "namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HuggingFace) -> None:
        with client.api.jobs.with_streaming_response.list(
            "namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobListResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.jobs.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_cancel(self, client: HuggingFace) -> None:
        job = client.api.jobs.cancel(
            job_id="jobId",
            namespace="namespace",
        )
        assert_matches_type(JobCancelResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: HuggingFace) -> None:
        response = client.api.jobs.with_raw_response.cancel(
            job_id="jobId",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobCancelResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: HuggingFace) -> None:
        with client.api.jobs.with_streaming_response.cancel(
            job_id="jobId",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobCancelResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.jobs.with_raw_response.cancel(
                job_id="jobId",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.api.jobs.with_raw_response.cancel(
                job_id="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_start(self, client: HuggingFace) -> None:
        job = client.api.jobs.start(
            namespace="namespace",
            environment={"foo": "string"},
            flavor="cpu-basic",
        )
        assert_matches_type(JobStartResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_start_with_all_params(self, client: HuggingFace) -> None:
        job = client.api.jobs.start(
            namespace="namespace",
            environment={"foo": "string"},
            flavor="cpu-basic",
            arch="amd64",
            arguments=["string"],
            command=["x"],
            docker_image="dockerImage",
            secrets={"foo": "string"},
            space_id="spaceId",
            timeout_seconds=1,
        )
        assert_matches_type(JobStartResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_start(self, client: HuggingFace) -> None:
        response = client.api.jobs.with_raw_response.start(
            namespace="namespace",
            environment={"foo": "string"},
            flavor="cpu-basic",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobStartResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_start(self, client: HuggingFace) -> None:
        with client.api.jobs.with_streaming_response.start(
            namespace="namespace",
            environment={"foo": "string"},
            flavor="cpu-basic",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobStartResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_start(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.jobs.with_raw_response.start(
                namespace="",
                environment={"foo": "string"},
                flavor="cpu-basic",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stream_events(self, client: HuggingFace) -> None:
        job = client.api.jobs.stream_events(
            job_id="jobId",
            namespace="namespace",
        )
        assert job is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_stream_events(self, client: HuggingFace) -> None:
        response = client.api.jobs.with_raw_response.stream_events(
            job_id="jobId",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert job is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_stream_events(self, client: HuggingFace) -> None:
        with client.api.jobs.with_streaming_response.stream_events(
            job_id="jobId",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert job is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_stream_events(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.jobs.with_raw_response.stream_events(
                job_id="jobId",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.api.jobs.with_raw_response.stream_events(
                job_id="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stream_logs(self, client: HuggingFace) -> None:
        job = client.api.jobs.stream_logs(
            job_id="jobId",
            namespace="namespace",
        )
        assert job is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_stream_logs(self, client: HuggingFace) -> None:
        response = client.api.jobs.with_raw_response.stream_logs(
            job_id="jobId",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert job is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_stream_logs(self, client: HuggingFace) -> None:
        with client.api.jobs.with_streaming_response.stream_logs(
            job_id="jobId",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert job is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_stream_logs(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.jobs.with_raw_response.stream_logs(
                job_id="jobId",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.api.jobs.with_raw_response.stream_logs(
                job_id="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stream_metrics(self, client: HuggingFace) -> None:
        job = client.api.jobs.stream_metrics(
            job_id="jobId",
            namespace="namespace",
        )
        assert job is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_stream_metrics(self, client: HuggingFace) -> None:
        response = client.api.jobs.with_raw_response.stream_metrics(
            job_id="jobId",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert job is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_stream_metrics(self, client: HuggingFace) -> None:
        with client.api.jobs.with_streaming_response.stream_metrics(
            job_id="jobId",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert job is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_stream_metrics(self, client: HuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.api.jobs.with_raw_response.stream_metrics(
                job_id="jobId",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.api.jobs.with_raw_response.stream_metrics(
                job_id="",
                namespace="namespace",
            )


class TestAsyncJobs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncHuggingFace) -> None:
        job = await async_client.api.jobs.retrieve(
            job_id="jobId",
            namespace="namespace",
        )
        assert_matches_type(JobRetrieveResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.jobs.with_raw_response.retrieve(
            job_id="jobId",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobRetrieveResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.jobs.with_streaming_response.retrieve(
            job_id="jobId",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobRetrieveResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.jobs.with_raw_response.retrieve(
                job_id="jobId",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.api.jobs.with_raw_response.retrieve(
                job_id="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHuggingFace) -> None:
        job = await async_client.api.jobs.list(
            "namespace",
        )
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.jobs.with_raw_response.list(
            "namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.jobs.with_streaming_response.list(
            "namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobListResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.jobs.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncHuggingFace) -> None:
        job = await async_client.api.jobs.cancel(
            job_id="jobId",
            namespace="namespace",
        )
        assert_matches_type(JobCancelResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.jobs.with_raw_response.cancel(
            job_id="jobId",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobCancelResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.jobs.with_streaming_response.cancel(
            job_id="jobId",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobCancelResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.jobs.with_raw_response.cancel(
                job_id="jobId",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.api.jobs.with_raw_response.cancel(
                job_id="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_start(self, async_client: AsyncHuggingFace) -> None:
        job = await async_client.api.jobs.start(
            namespace="namespace",
            environment={"foo": "string"},
            flavor="cpu-basic",
        )
        assert_matches_type(JobStartResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_start_with_all_params(self, async_client: AsyncHuggingFace) -> None:
        job = await async_client.api.jobs.start(
            namespace="namespace",
            environment={"foo": "string"},
            flavor="cpu-basic",
            arch="amd64",
            arguments=["string"],
            command=["x"],
            docker_image="dockerImage",
            secrets={"foo": "string"},
            space_id="spaceId",
            timeout_seconds=1,
        )
        assert_matches_type(JobStartResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_start(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.jobs.with_raw_response.start(
            namespace="namespace",
            environment={"foo": "string"},
            flavor="cpu-basic",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobStartResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.jobs.with_streaming_response.start(
            namespace="namespace",
            environment={"foo": "string"},
            flavor="cpu-basic",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobStartResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_start(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.jobs.with_raw_response.start(
                namespace="",
                environment={"foo": "string"},
                flavor="cpu-basic",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stream_events(self, async_client: AsyncHuggingFace) -> None:
        job = await async_client.api.jobs.stream_events(
            job_id="jobId",
            namespace="namespace",
        )
        assert job is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_stream_events(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.jobs.with_raw_response.stream_events(
            job_id="jobId",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert job is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_stream_events(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.jobs.with_streaming_response.stream_events(
            job_id="jobId",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert job is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_stream_events(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.jobs.with_raw_response.stream_events(
                job_id="jobId",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.api.jobs.with_raw_response.stream_events(
                job_id="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stream_logs(self, async_client: AsyncHuggingFace) -> None:
        job = await async_client.api.jobs.stream_logs(
            job_id="jobId",
            namespace="namespace",
        )
        assert job is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_stream_logs(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.jobs.with_raw_response.stream_logs(
            job_id="jobId",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert job is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_stream_logs(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.jobs.with_streaming_response.stream_logs(
            job_id="jobId",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert job is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_stream_logs(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.jobs.with_raw_response.stream_logs(
                job_id="jobId",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.api.jobs.with_raw_response.stream_logs(
                job_id="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stream_metrics(self, async_client: AsyncHuggingFace) -> None:
        job = await async_client.api.jobs.stream_metrics(
            job_id="jobId",
            namespace="namespace",
        )
        assert job is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_stream_metrics(self, async_client: AsyncHuggingFace) -> None:
        response = await async_client.api.jobs.with_raw_response.stream_metrics(
            job_id="jobId",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert job is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_stream_metrics(self, async_client: AsyncHuggingFace) -> None:
        async with async_client.api.jobs.with_streaming_response.stream_metrics(
            job_id="jobId",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert job is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_stream_metrics(self, async_client: AsyncHuggingFace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.api.jobs.with_raw_response.stream_metrics(
                job_id="jobId",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.api.jobs.with_raw_response.stream_metrics(
                job_id="",
                namespace="namespace",
            )
