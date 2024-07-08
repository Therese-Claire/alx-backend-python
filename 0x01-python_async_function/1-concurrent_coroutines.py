#!/usr/bin/env python3
"""Task 1's module"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """coroutine that imports wait_random and spawn
    wait_random n times with the specified max_delay

    Args:
        n (int): first integer
        max_delay: second integer

    Returns: List of delay values
    """
    delays = []
    tasks = []

    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    for task in tasks:
        delay = await task
        delays.append(delay)

    return sorted(delays)
