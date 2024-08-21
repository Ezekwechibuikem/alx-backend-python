#!/usr/bin/env python3
"""
asynchronous coroutine
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    asynchronous coroutine that takes in 2 arguments
    and returns a float
    """
    job = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(job)]