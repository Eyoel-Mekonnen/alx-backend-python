#!/usr/bin/env python3
"""Module returns total execution Time."""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Return the time it took."""
    starttime = time.time()
    asyncio.run(wait_n(n, max_delay))
    endtime = time.time()
    time_per_task = (endtime - starttime) / n
    return time_per_task
