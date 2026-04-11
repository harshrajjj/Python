import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def check_stock(item):
    print(f"Checking stock for {item}...")
    time.sleep(2)  # Simulate a blocking I/O operation
    return f"{item} is in stock!"


async def main():
    asyncio_loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await asyncio_loop.run_in_executor(pool, check_stock, "Laptop")
        print(result)


asyncio.run(main())