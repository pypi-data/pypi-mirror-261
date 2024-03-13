# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict

__all__ = ["ComplexQueryUnionQueryParams"]


class ComplexQueryUnionQueryParams(TypedDict, total=False):
    include: Union[str, List[str]]
