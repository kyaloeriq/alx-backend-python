#!/usr/bin/env python3
"""
Module to measure the runtime of asynchronous coroutines
"""

import asyncio
import time
import importlib.util

# Dynamically import wait_n from 0-basic_async_syntax.py
spec = importlib.util.spec_from_file_location("basic_async_syntax", "./0-basic_async_syntax.py")
basic_async_syntax = importlib.util.module_from_spec(spec)
spec.loader.exec_module(basic_async_syntax)
wait_n = basic_async_syntax.wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay)
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start_time
    return total_time / n
