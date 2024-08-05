#!/usr/bin/env python3
"""
Module to measure the runtime of asynchronous coroutines
"""

import asyncio
import time
import importlib.util
import sys

def import_module_from_file(module_name: str, file_path: str):
    """
    Dynamically import a module from a file path.
    """
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

# Dynamically import wait_n from 1-concurrent_coroutines
module = import_module_from_file("concurrent_coroutines", "./1-concurrent_coroutines")
wait_n = getattr(module, "wait_n")

def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay)
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start_time
    return total_time / n
