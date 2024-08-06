#!/usr/bin/env python3
"""
Module contains coroutines for generating and collecting random numbers
"""

import asyncio
import time
from typing import List
from 1-async_comprehension import async_comprehension

async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime of executing async_comprehension
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_time = time.perf_counter() - start_time
    return total_time
