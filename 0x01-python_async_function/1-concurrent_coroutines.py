#!/usr/bin/env python3
"""
Import wait_random from the previous python file that you’ve
written and write an async routine called wait_n that takes in 2
int arguments (in this order): n and max_wait_time. You will spawn
wait_random n times with the specified max_wait_time.

wait_n should return the list of all the wait_times (float values).
The list of the wait_times should be in ascending order without using
sort() because of concurrency.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_wait_time: int) -> List[float]:
    """Execute wait_random n times"""
    tasks = []
    wait_times = []

    for i in range(n):
        task = wait_random(max_wait_time)
        tasks.append(task)

    for task in asyncio.as_completed((tasks)):
        wait_time = await task
        wait_times.append(wait_time)

    return wait_times
