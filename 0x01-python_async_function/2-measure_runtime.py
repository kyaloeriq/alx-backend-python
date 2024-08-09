#!/usr/bin/env python3
"""
Module to measure the runtime of asynchronous coroutines.
"""

import asyncio
import time
from 1-concurrent_coroutines import wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay).

    Args:
        n (int): Number of coroutines.
        max_delay (int): Maximum delay for coroutines.

    Returns:
        float: The average time per coroutine.
    """
    start_time: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time: float = time.perf_counter() - start_time
    return total_time / n
