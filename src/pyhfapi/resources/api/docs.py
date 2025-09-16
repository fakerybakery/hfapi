# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.api import doc_search_params
from ..._base_client import make_request_options
from ...types.api.doc_search_response import DocSearchResponse

__all__ = ["DocsResource", "AsyncDocsResource"]


class DocsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DocsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return DocsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DocsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return DocsResourceWithStreamingResponse(self)

    def search(
        self,
        *,
        q: str,
        limit: int | NotGiven = NOT_GIVEN,
        product: Literal[
            "hub",
            "transformers",
            "diffusers",
            "datasets",
            "gradio",
            "trackio",
            "smolagents",
            "huggingface_hub",
            "huggingface.js",
            "transformers.js",
            "inference-providers",
            "inference-endpoints",
            "peft",
            "accelerate",
            "optimum",
            "optimum-habana",
            "optimum-neuron",
            "optimum-intel",
            "optimum-executorch",
            "tokenizers",
            "llm-course",
            "mcp-course",
            "smol-course",
            "agents-course",
            "deep-rl-course",
            "computer-vision-course",
            "evaluate",
            "tasks",
            "dataset-viewer",
            "trl",
            "simulate",
            "sagemaker",
            "timm",
            "safetensors",
            "tgi",
            "setfit",
            "audio-course",
            "lerobot",
            "autotrain",
            "tei",
            "bitsandbytes",
            "cookbook",
            "sentence_transformers",
            "ml-games-course",
            "diffusion-course",
            "ml-for-3d-course",
            "chat-ui",
            "leaderboards",
            "lighteval",
            "argilla",
            "distilabel",
            "microsoft-azure",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocSearchResponse:
        """
        Search any Hugging Face documentation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/docs/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "limit": limit,
                        "product": product,
                    },
                    doc_search_params.DocSearchParams,
                ),
            ),
            cast_to=DocSearchResponse,
        )


class AsyncDocsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDocsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fakerybakery/hfapi#accessing-raw-response-data-eg-headers
        """
        return AsyncDocsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDocsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fakerybakery/hfapi#with_streaming_response
        """
        return AsyncDocsResourceWithStreamingResponse(self)

    async def search(
        self,
        *,
        q: str,
        limit: int | NotGiven = NOT_GIVEN,
        product: Literal[
            "hub",
            "transformers",
            "diffusers",
            "datasets",
            "gradio",
            "trackio",
            "smolagents",
            "huggingface_hub",
            "huggingface.js",
            "transformers.js",
            "inference-providers",
            "inference-endpoints",
            "peft",
            "accelerate",
            "optimum",
            "optimum-habana",
            "optimum-neuron",
            "optimum-intel",
            "optimum-executorch",
            "tokenizers",
            "llm-course",
            "mcp-course",
            "smol-course",
            "agents-course",
            "deep-rl-course",
            "computer-vision-course",
            "evaluate",
            "tasks",
            "dataset-viewer",
            "trl",
            "simulate",
            "sagemaker",
            "timm",
            "safetensors",
            "tgi",
            "setfit",
            "audio-course",
            "lerobot",
            "autotrain",
            "tei",
            "bitsandbytes",
            "cookbook",
            "sentence_transformers",
            "ml-games-course",
            "diffusion-course",
            "ml-for-3d-course",
            "chat-ui",
            "leaderboards",
            "lighteval",
            "argilla",
            "distilabel",
            "microsoft-azure",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocSearchResponse:
        """
        Search any Hugging Face documentation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/docs/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "limit": limit,
                        "product": product,
                    },
                    doc_search_params.DocSearchParams,
                ),
            ),
            cast_to=DocSearchResponse,
        )


class DocsResourceWithRawResponse:
    def __init__(self, docs: DocsResource) -> None:
        self._docs = docs

        self.search = to_raw_response_wrapper(
            docs.search,
        )


class AsyncDocsResourceWithRawResponse:
    def __init__(self, docs: AsyncDocsResource) -> None:
        self._docs = docs

        self.search = async_to_raw_response_wrapper(
            docs.search,
        )


class DocsResourceWithStreamingResponse:
    def __init__(self, docs: DocsResource) -> None:
        self._docs = docs

        self.search = to_streamed_response_wrapper(
            docs.search,
        )


class AsyncDocsResourceWithStreamingResponse:
    def __init__(self, docs: AsyncDocsResource) -> None:
        self._docs = docs

        self.search = async_to_streamed_response_wrapper(
            docs.search,
        )
