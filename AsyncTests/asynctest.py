import asyncio
import time

async def e():
    print("Hello!")
    await asyncio.sleep(2)
    print("Goodbye!")

async def main():
    # for i in range(3):
    await asyncio.gather(*(e() for i in range(3)))

# main()
if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")