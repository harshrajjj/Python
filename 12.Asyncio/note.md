# Asyncio, Daemon Threads, and Concurrency Pitfalls - Notes

---

# Part 1: Asyncio

## What is Asyncio?
- `asyncio` is Python's built-in library for writing **asynchronous** code
- It allows you to run multiple tasks **concurrently** within a **single thread**
- Instead of waiting idly for I/O (network, file, sleep), it switches to another task

### How is it different from threading?
| Threading | Asyncio |
|---|---|
| Multiple threads | Single thread |
| OS decides when to switch | **You** decide when to switch (with `await`) |
| Can be unpredictable | More predictable — switches only at `await` points |
| Good for blocking I/O | Best for non-blocking async I/O |

---

## async_one.py — `async`, `await`, `gather`, and `aiohttp`

### `async def` — Define an async function (coroutine):
- A function declared with `async def` is a **coroutine**
- It doesn't run when called — it returns a coroutine object (like generators)
- Must be run with `asyncio.run()` or `await`

### `await` — Pause and let other tasks run:
- `await` says "this will take time, go do something else and come back when it's done"
- Can only be used **inside** an `async def` function
- `await asyncio.sleep(2)` → pause for 2 seconds without blocking the whole program

```python
import asyncio

async def brew_chai():
    print("Boiling water...")
    await asyncio.sleep(2)       # pause — other tasks can run during this
    print("Steeping the tea...")
    await asyncio.sleep(3)
    print("Chai is ready!")

asyncio.run(brew_chai())         # entry point — starts the event loop
```

### `asyncio.run()` — Start the event loop:
- The **event loop** is the engine that runs async tasks
- `asyncio.run(main())` creates the loop, runs `main()`, and cleans up
- Only call this **once** in your program — usually at the top level

### `asyncio.gather()` — Run multiple tasks concurrently:
```python
async def brew(name):
    print(f"Boiling {name} water...")
    await asyncio.sleep(2)
    print(f"{name} is ready!")

async def main():
    await asyncio.gather(
        brew("Chai"),             # starts both at the same time
        brew("Coffee")
    )
    # Total: ~2 seconds (not 4) — they ran concurrently!

asyncio.run(main())
```

### How `gather()` works:
1. Starts **all** coroutines at the same time
2. When one hits `await`, switches to another
3. Returns when **all** are done
4. `*tasks` unpacks a list of tasks: `gather(*[task1, task2, task3])`

### `aiohttp` — Async HTTP requests:
- Regular `requests` library is **blocking** — it freezes the whole event loop
- `aiohttp` is the async version — it works with `await`

```python
import aiohttp

async def fetch_data(session, url):
    async with session.get(url) as response:
        print(f"Fetched {url} with status {response.status}")

async def main():
    urls = [
        "https://httpbin.org/delay/3",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/1"
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for url in urls]
        await asyncio.gather(*tasks)     # fetch all URLs at once

asyncio.run(main())
```

### `async with` — Async context manager:
- Like regular `with`, but for async resources
- `async with aiohttp.ClientSession() as session:` creates and properly closes the HTTP session
- `async with session.get(url) as response:` makes the request and cleans up

### `asyncio.sleep()` vs `time.sleep()`:
| `asyncio.sleep(2)` | `time.sleep(2)` |
|---|---|
| **Non-blocking** — other async tasks run | **Blocking** — everything stops |
| Use inside `async def` with `await` | Use in regular functions or threads |
| Releases control to event loop | Freezes the entire thread |

**Never use `time.sleep()` inside async code** — it defeats the entire purpose!

---

## thread_async.py — Mixing Asyncio with Threads (`run_in_executor`)

### The Problem:
- Some libraries are **blocking** (use `time.sleep()`, regular I/O)
- You can't `await` a blocking function — it would freeze the event loop

### The Solution — `run_in_executor()`:
- Runs a **blocking function** in a separate thread, wrapped as an awaitable
- The event loop stays free to run other async tasks

```python
from concurrent.futures import ThreadPoolExecutor

def check_stock(item):               # regular blocking function
    time.sleep(2)
    return f"{item} is in stock!"

async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, check_stock, "Laptop")
        print(result)

asyncio.run(main())
```

### How it works:
1. `asyncio.get_running_loop()` — gets the current event loop
2. `run_in_executor(pool, function, arg1, arg2)` — runs the blocking function in the thread pool
3. `await` — waits for the result without blocking the event loop
4. Other async tasks can run while `check_stock` is blocked in its thread

### When to use:
- When you need to call a **blocking library** (database drivers, file operations, `requests`) from async code
- Bridge between sync and async worlds

---

## process_async.py — Mixing Asyncio with Processes

### Same concept, but for CPU-bound work:
```python
from concurrent.futures import ProcessPoolExecutor

def encrypt_data(data):               # CPU-bound blocking function
    return ''.join(reversed(data))

async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, encrypt_data, "Sensitive Information")
        print(result)

if __name__ == "__main__":
    asyncio.run(main())
```

### Thread vs Process executor:
| `ThreadPoolExecutor` | `ProcessPoolExecutor` |
|---|---|
| For **I/O-bound** blocking code | For **CPU-bound** blocking code |
| Shares memory (same process) | Separate memory (different process) |
| Limited by GIL for CPU work | True parallelism for CPU work |
| No `if __name__` guard needed | **Requires** `if __name__` guard |

---

# Part 2: Daemon Threads

## deamon.py — Daemon Thread (Background Worker)

### What is a Daemon Thread?
- A daemon thread is a **background thread** that automatically dies when the main program exits
- Used for tasks that should run **as long as the program runs** and stop when it stops
- Think of it like background music — stops when you close the app

```python
import threading
import time

def monitor_tea_temperature():
    while True:                        # infinite loop!
        print("Monitoring temperature...")
        time.sleep(2)

t = threading.Thread(target=monitor_tea_temperature, daemon=True).start()
print("Main thread is doing other work...")
# Program exits → daemon thread is killed automatically
```

### Key point:
- `daemon=True` → thread dies when main program ends
- The `while True` loop would normally run forever, but the daemon thread is killed when `main` finishes

---

## nondeamon.py — Non-Daemon Thread (Keeps Program Alive)

```python
t = threading.Thread(target=monitor_tea_temperature).start()  # daemon=False (default)
print("Main thread is doing other work...")
# Program WON'T exit — non-daemon thread keeps it alive forever!
```

### Daemon vs Non-Daemon:
| Daemon (`daemon=True`) | Non-Daemon (default) |
|---|---|
| Dies when main thread exits | Keeps program alive until it finishes |
| For background tasks you don't care about | For important tasks that must complete |
| `while True` is safe — auto-killed | `while True` = program never exits! |

### Profiling tip (from the code):
```bash
py -m cProfile -s time nondeamon.py
```
- `cProfile` is Python's built-in profiler — shows how much time each function takes
- `-s time` sorts results by time spent
- Useful for finding performance bottlenecks

---

## bgWorker.py — Combining Daemon Threads with Asyncio

```python
import asyncio
import threading
import time

def background_task():
    while True:
        print(f"Background: {threading.current_thread().name}")
        time.sleep(2)

async def fetch_order():
    await asyncio.sleep(3)
    print("Order fetched")

threading.Thread(target=background_task, daemon=True).start()  # background worker
asyncio.run(fetch_order())                                       # async main task
```

### What happens:
1. Daemon thread starts — prints "Background..." every 2 seconds
2. Async event loop starts — `fetch_order()` waits 3 seconds
3. During the 3 seconds, the background thread prints its messages
4. After `fetch_order()` completes, `asyncio.run()` returns
5. Main program ends → daemon thread is killed

### Real-world pattern:
- Daemon thread for monitoring, logging, health checks
- Asyncio for the main application logic (handling requests, processing data)

---

# Part 3: Concurrency Pitfalls

## race_condition.py — Race Condition (Without Lock)

### What is a Race Condition?
- When two threads modify the same data **at the same time** and the result depends on **which one runs first**
- The outcome is unpredictable — different every run

```python
chai_stock = 0

def buy_chai():
    global chai_stock
    for _ in range(100000):
        chai_stock += 1          # NOT thread-safe!

thread = [threading.Thread(target=buy_chai) for _ in range(2)]
for t in thread: t.start()
for t in thread: t.join()

print(chai_stock)   # Expected: 200000, Actual: maybe 156743 — WRONG!
```

### Why it breaks:
- `chai_stock += 1` is actually 3 operations: **read** → **add 1** → **write back**
- Thread A reads `chai_stock = 100`
- Thread B reads `chai_stock = 100` (same value! A hasn't written back yet)
- Thread A writes `101`
- Thread B writes `101` (should be 102 — one increment was lost!)

### The fix — use a Lock:
```python
lock = threading.Lock()

def buy_chai():
    global chai_stock
    for _ in range(100000):
        with lock:               # only one thread at a time
            chai_stock += 1      # safe!
```

---

## deadLock.py — Deadlock (Threads Stuck Forever)

### What is a Deadlock?
- Two threads each **hold a lock** and **wait for the other's lock** — neither can proceed
- The program **freezes forever** — no crash, no error, just stuck

```python
lock_a = threading.Lock()
lock_b = threading.Lock()

def thread1():
    with lock_a:                         # holds lock A
        print("Thread 1: Acquired lock A")
        with lock_b:                     # wants lock B — but thread2 has it!
            print("Thread 1: Acquired lock B")

def thread2():
    with lock_b:                         # holds lock B
        print("Thread 2: Acquired lock B")
        with lock_a:                     # wants lock A — but thread1 has it!
            print("Thread 2: Acquired lock A")
```

### What happens:
```
Thread 1: acquires lock A ✓
Thread 2: acquires lock B ✓
Thread 1: wants lock B → BLOCKED (Thread 2 has it)
Thread 2: wants lock A → BLOCKED (Thread 1 has it)
→ DEADLOCK! Both threads wait forever.
```

### How to prevent deadlocks:
1. **Always acquire locks in the same order** — if everyone gets A first, then B, no deadlock
2. **Use timeout**: `lock.acquire(timeout=5)` — gives up after 5 seconds instead of waiting forever
3. **Avoid nested locks** when possible — simpler is safer
4. **Use `threading.RLock()`** (reentrant lock) — allows the same thread to acquire it multiple times

### Fixed version (same lock order):
```python
def thread1():
    with lock_a:
        with lock_b:       # A then B
            ...

def thread2():
    with lock_a:           # A then B (same order!)
        with lock_b:
            ...
```

### Profiling tools mentioned:
- `cProfile` — built-in profiler (function-level timing)
- `py-spy` — sampling profiler (no code changes needed)
- `line_profiler` — line-by-line timing
- `memory_profiler` — track memory usage
- `pyinstrument` — call stack profiler (easy to read output)
- `snakeviz` — visualize cProfile output in browser

---

## Summary: All Concurrency Tools

### When to use what:
```
I/O-bound + async library available?
  → asyncio (best performance, single thread)

I/O-bound + blocking library?
  → threading OR asyncio + run_in_executor

CPU-bound?
  → multiprocessing OR asyncio + ProcessPoolExecutor

Background task that should auto-stop?
  → daemon thread
```

### Concurrency pitfalls:

| Problem | What happens | Fix |
|---|---|---|
| Race condition | Shared data gets corrupted | Use `Lock` |
| Deadlock | Threads stuck forever | Same lock order, use timeouts |
| Blocking in async | Event loop freezes | Use `run_in_executor` |
| `time.sleep` in async | Blocks the event loop | Use `asyncio.sleep` |

### Key asyncio concepts:

| Concept | What it does |
|---|---|
| `async def` | Define a coroutine |
| `await` | Pause and let other tasks run |
| `asyncio.run()` | Start the event loop |
| `asyncio.gather()` | Run multiple coroutines concurrently |
| `asyncio.sleep()` | Non-blocking sleep |
| `run_in_executor()` | Run blocking code in thread/process pool |
| `aiohttp` | Async HTTP requests |
| `async with` | Async context manager |
