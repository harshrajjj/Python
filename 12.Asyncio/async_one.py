import asyncio

async def brew_chai():
    print("Boiling water...")
    await asyncio.sleep(2)
    print("Steeping the tea...")
    await asyncio.sleep(3)
    print("Pouring into cup...")
    await asyncio.sleep(1)
    print("Adding sugar and milk...")
    await asyncio.sleep(1)
    print("Chai is ready!")


# asyncio.run(brew_chai())


async def brew(name):
    print(f"Boiling {name} water...")
    await asyncio.sleep(2)
    print(f"Pouring {name} into cup...")
    await asyncio.sleep(1)
    print(f"{name} is ready!")


# async def main():
#     await asyncio.gather(
#         brew("Chai"),
#         brew("Coffee")
#     )


# asyncio.run(main())


import aiohttp

async def fetch_data(session,url):
    async with session.get(url) as response:
        print(f"Fetching data from {url}...with status {response.status}")


async def main():
    urls = [
        "https://httpbin.org/delay/3",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/1"
    ]
    async with aiohttp.ClientSession() as session:
        task = [fetch_data(session, url) for url in urls]
        await asyncio.gather(*task)# asyncio.gather(*task) will wait for all the tasks to complete before proceeding  [*task] is used to unpack the list of tasks into individual arguments for asyncio.gather().


asyncio.run(main())   