#!/usr/bin/env python3
"""Make Muliplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return function that mulitplies float."""
    def multiplier_part(multiplier: float) -> float:
        return multiplier * multiplier
    return multiplier_part
