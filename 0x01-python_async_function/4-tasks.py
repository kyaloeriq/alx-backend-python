#!/usr/bin/env python3
"""
Module to run multiple asyncio.Tasks concurrently using task_wait_random.
"""

import asyncio
from typing import List
from 1-concurrent_coroutines import task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with the specified max_delay.

    Args:
        n (int): Number of tasks to spawn.
        max_delay (int): Maximum delay for each task.

    Returns:
        List[float]: List of delays in the order they were completed.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
