import asyncio
from concurrent.futures import ProcessPoolExecutor

def encrypt_data(data):
    print(f"Encrypting data: {data}...")
    # Simulate a CPU-bound operation
    result = ''.join(reversed(data))  # Just a dummy encryption by reversing the string
    return f"Encrypted data: {result}"


async def main():
    asyncio_loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        result = await asyncio_loop.run_in_executor(pool, encrypt_data, "Sensitive Information")
        print(result)

if __name__ == "__main__":
    asyncio.run(main())

