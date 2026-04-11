import asyncio
import time 
import threading

def background_task():
    while True:
        print(f"Background task running in thread: {threading.current_thread().name}")
        time.sleep(2)

async def fetch_order():
    await asyncio.sleep(3)
    print("Order fetched")

threading.Thread(target=background_task, daemon=True).start()

asyncio.run(fetch_order())