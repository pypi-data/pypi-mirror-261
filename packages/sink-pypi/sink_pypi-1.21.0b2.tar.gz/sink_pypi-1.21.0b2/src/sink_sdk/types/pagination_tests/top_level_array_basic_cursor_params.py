# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["TopLevelArrayBasicCursorParams"]


class TopLevelArrayBasicCursorParams(TypedDict, total=False):
    cursor: Optional[str]

    limit: int
