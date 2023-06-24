# 1. Using `async` and `await` to define and run a simple asynchronous function.

import asyncio

async def greet():
    print("Hello")
    await asyncio.sleep(1)
    print("World!")

# greet()   ## RuntimeWarning: coroutine 'greet' was never awaited
asyncio.run(greet())


