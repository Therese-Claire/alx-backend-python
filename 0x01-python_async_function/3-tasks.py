#!/usr/bin/env python3
"""Function that creates an asynio task"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create an asyncio.Task that executes
    wait_random(max_delay)

    Args:
        max_delay (int): maximum delay value

    """
    loop = asyncio.get_event_loop()
    task = loop.create_task(wait_random(max_delay))
    return task
