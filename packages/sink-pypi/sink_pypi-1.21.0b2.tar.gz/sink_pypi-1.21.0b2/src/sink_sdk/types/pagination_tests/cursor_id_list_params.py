# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["CursorIDListParams"]


class CursorIDListParams(TypedDict, total=False):
    limit: int

    next_id: Optional[str]
