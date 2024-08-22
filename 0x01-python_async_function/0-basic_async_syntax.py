#!/usr/bin/env python3
"""Gives backed delayed amount in floating number."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Returend how much delay there was in async."""
    delayed_part = random.uniform(0, max_delay)
    await asyncio.sleep(delayed_part)
    return delayed_part
