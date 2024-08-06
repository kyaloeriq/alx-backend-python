#!/usr/bin/env python3
"""
This module contains an asynchronous generator that yields random numbers.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that yields a random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)