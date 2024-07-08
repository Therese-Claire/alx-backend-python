#!/usr/bin/env python3
"""Task 0's module"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """asynchronous coroutine that takes an interger and waits
    for a random delay between 0 and max_delay.

    Args:
        max_delay (int): int argument.

    Returns:
        float : Random delay value.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
