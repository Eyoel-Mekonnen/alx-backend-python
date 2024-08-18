#!/usr/bin/env python3
"""Annotated floats returns floats."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of floats."""
    sum = 0
    for nums in input_list:
        sum = sum + nums
    return sum
