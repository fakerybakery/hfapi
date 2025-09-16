# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["DocSearchParams"]


class DocSearchParams(TypedDict, total=False):
    q: Required[str]

    limit: int

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
