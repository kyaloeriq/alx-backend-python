#!/usr/bin/env python3
"""
Module to measure the runtime of asynchronous coroutines
"""

import asyncio
import time
from typing import List
from 0-basic_async_syntax import wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    """
    start_time = time.perf_counter()
    await wait_n(n, max_delay)
    total_time = time.perf_counter() - start_time
    return total_time / n
