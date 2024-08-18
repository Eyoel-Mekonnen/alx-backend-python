#!/usr/bin/env python3
"""Make Muliplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return function that mulitplies float."""
    def multiplier_part(value: float) -> float:
        return value * multiplier
    return multiplier_part
