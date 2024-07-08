#!/usr/bin/env python3
"""Modification of wait_n"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """coroutine that imports wait_random and spawn
    wait_random n times with the specified max_delay

    Args:
        n (int): first integer
        max_delay: second integer

    Returns: List of delay values
    """
    tasks = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    return await asyncio.gather(*tasks)
