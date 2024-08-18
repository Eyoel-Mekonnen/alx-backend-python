#!/usr/bin/env python3
"""Function that take str and int | float and return tuple."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return newTuple."""
    v = float(v**2)
    newTuple = (k, v)
    return newTuple
