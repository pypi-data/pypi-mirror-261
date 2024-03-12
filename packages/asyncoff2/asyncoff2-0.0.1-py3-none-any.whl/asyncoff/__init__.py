import asyncio
from typing import Callable

def asyncoff(func: Callable):
    def inner(*args, **kwargs):
        async def create_task(*args, **kwargs):
            return await asyncio.create_task(func(*args, **kwargs))

        return asyncio.run(create_task(*args, **kwargs))

    return inner