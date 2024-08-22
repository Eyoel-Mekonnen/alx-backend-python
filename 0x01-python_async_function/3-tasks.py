#!/usr/bin/env python3
"""Create asyncio.Task."""
import asyncio

wait_random = __import__('1-concurrent_coroutines').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return a Scheduled asyncion.Task objects."""
    return asyncio.create_task(wait_random(max_delay))
