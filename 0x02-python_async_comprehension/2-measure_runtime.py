#!/usr/bin/env python3
"""Measure Runtime."""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Return the measured Time."""
    start = time.time()
    await asyncio.gather(*[async_comprehension() for i in range(0, 4)])
    end = time.time()
    return end - start
