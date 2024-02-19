#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function
task_wait_n. The code is nearly identical to wait_n except
task_wait_random is being called.
"""


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_wait_time: int) -> List[float]:
    """Execute wait_random n times"""
    tasks = []
    wait_times = []

    for i in range(n):
        task = task_wait_random(max_wait_time)
        tasks.append(task)

    for task in asyncio.as_completed((tasks)):
        wait_time = await task
        wait_times.append(wait_time)

    return wait_times
