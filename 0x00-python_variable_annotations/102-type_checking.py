#!/usr/bin/env python3
"""Check Using Mypy."""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Piece of code."""
    zoomed_in: List = list(
        item for item in lst
        for i in range(factor)
    )
    return zoomed_in


array = (12, 72, 9)
zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
