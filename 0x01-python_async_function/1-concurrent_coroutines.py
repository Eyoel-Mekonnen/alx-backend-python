#!/usr/bin/env python3
"""Execute Multiple Coroutines at the same time with async."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List:
    """Return delay float value list."""
    lists = []
    for i in range(0, n):
        lists.append(asyncio.create_task(wait_random(max_delay)))
    results = []
    for yeilded_tasks in asyncio.as_completed(lists):
        retrieved = await yeilded_tasks
        results.append(retrieved)
    return results
