#!/usr/bin/env python3
"""
This module contains coroutines for generating and collecting random numbers.
"""

import asyncio
from typing import List
from 0-async_generator import async_generator  # Adjust the import as per the actual module name

async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers from async_generator
    using an asynchronous comprehension, then returns the list of
    random numbers.

    Returns:
        List[float]: A list of 10 random numbers.
    """
    return [number async for number in async_generator()]
