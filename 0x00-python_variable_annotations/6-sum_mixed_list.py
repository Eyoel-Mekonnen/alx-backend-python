#!/usr/bin/env python3
"""Annotated Function to return sum of list."""
from typing import List


def sum_mixed_list(mxd_list: List[int, float]) -> float:
    """Return Function that sum list."""
    sum = 0
    for i in range(0, len(mxd_list)):
        sum = sum + mxd_list[i]
    return sum
