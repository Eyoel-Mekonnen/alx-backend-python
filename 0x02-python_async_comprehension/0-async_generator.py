#!/usr/bin/env python3
"""Yield number on async loop."""
import asyncio
import random


async def async_generator():
    """Return Yeild random number."""
    for i in range(0, 10):
        await asyncio.sleep(1)
        random_number = random.uniform(0, 10)
        yield random_number
