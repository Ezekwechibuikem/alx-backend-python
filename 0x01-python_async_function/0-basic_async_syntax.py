#!/usr/bin/env python3
"""
asynchronous coroutine
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    asynchronous coroutine that takes in none arguments
    and returns a float
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay