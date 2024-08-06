#!/usr/bin/env python3
"""
This module contains coroutines for generating and collecting random numbers.
"""

from typing import List
from 0-async_generator import async_generator

async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers from async_generator
    """
    return [number async for number in async_generator()]
