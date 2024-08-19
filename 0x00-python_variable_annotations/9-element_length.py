#!/usr/bin/env python3
"""Determine what type of function annotation."""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return value with appropriate types."""
    return [(i, len(i)) for i in lst]
