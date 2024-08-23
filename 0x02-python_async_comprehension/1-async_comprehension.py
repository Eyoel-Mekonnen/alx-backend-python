#!/usr/bin/env python3
"""Async Comprehension."""
from typing import Generator
import asyncio


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """Return 10 random number using __aiter__()."""
    results = [i async for i in async_generator()]
    return results
