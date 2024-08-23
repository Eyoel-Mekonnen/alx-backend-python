#!/usr/bin/env python3
"""Altering wait_n async Function."""
import asyncio
from typing import List

task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Return the delay time as float Lists."""
    lists = []
    for i in range(0, n):
        lists.append(asyncio.create_task(task_wait_random(max_delay)))
    results = []
    for yeilded_tasks in asyncio.as_completed(lists):
        retrieved = await yeilded_tasks
        results.append(retrieved)
    return results
