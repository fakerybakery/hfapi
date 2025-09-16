from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `hugging_face.resources` module.

    This is used so that we can lazily import `hugging_face.resources` only when
    needed *and* so that users can just import `hugging_face` and reference `hugging_face.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("hugging_face.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
