import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

# Your example blocking function
def queryBar():
    time.sleep(3)
    print('bar')

# Run queryBar 10 times using asyncio
executor = ThreadPoolExecutor(10)



async def in_thread(func):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(executor, func)

async def call_queryBar_multiple_times():
    # results = await asyncio.gather(*(in_thread(queryBar) for _ in range(10)))
    results = await asyncio.gather(*(in_thread(lambda: queryBar()) for _ in range(10)))

    # Parentheses cannot be used when calling querrybar because it will attempt to make corutines using the result from the function instead of the function itself, which blocks the execution. 

    print(results)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(call_queryBar_multiple_times())
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()