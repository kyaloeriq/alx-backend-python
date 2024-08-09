#!/usr/bin/env python3
"""
Module to create an asyncio.Task from wait_random.
"""

import asyncio
from 0-basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task that runs wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
