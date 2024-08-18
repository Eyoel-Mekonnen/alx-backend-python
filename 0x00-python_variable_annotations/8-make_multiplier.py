#!/usr/bin/env python3
"""Make Muliplier."""
from typing import Callable


def make_multiplier(mulitplier: float) -> Callable[[float], float]:
    """Return function that mulitplies float."""
    def multiplier_part(mulitplier: float) -> float:
        return mulitplier * mulitplier
    return multiplier_part
