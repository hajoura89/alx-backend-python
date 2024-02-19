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


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Execute wait_random n times"""
    wait_times = await asyncio.gather(
     *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
