#!/usr/bin/env python3
"""Coroutin that generates random numbers
"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Coroutine that generates random numbers between 0 and 10, one number
    at a time.

    Yields:
        Generator[float, None, None]:  A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
