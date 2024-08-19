#!/usr/bin/env python3
"""Augmenting Code with duck typed annotation."""
from typing import Sequence, Union, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Duck-typed Annotation."""
    if lst:
        return lst[0]
    else:
        return None
