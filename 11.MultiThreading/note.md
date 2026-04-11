# MultiThreading and MultiProcessing in Python - Notes

---

# Part 1: Threading

## What is a Thread?
- A thread is a **separate flow of execution** within your program
- By default, Python runs code **line by line** (single thread)
- With multiple threads, you can do multiple things **at the same time** (concurrently)
- Think of it like a restaurant: one waiter (single thread) vs multiple waiters (multi-thread)

---

## ThreadOne.py — Basic Threading

### Without threading (sequential):
```python
boil_milk()      # takes 2 seconds
toast_bread()    # takes 3 seconds
# Total: 5 seconds — one after the other
```

### With threading (concurrent):
```python
import threading
import time

def prepare_chai(type, wait_time):
    print(f"Preparing {type} chai...")
    time.sleep(wait_time)
    print(f"{type} chai is ready.")

t1 = threading.Thread(target=prepare_chai, args=("Masala", 2))
t2 = threading.Thread(target=prepare_chai, args=("Ginger", 3))

t1.start()   # starts thread 1 — runs in the background
t2.start()   # starts thread 2 — runs in the background

t1.join()    # wait for thread 1 to finish
t2.join()    # wait for thread 2 to finish
# Total: ~3 seconds — both ran at the same time!
```

### Key methods:

| Method | What it does |
|---|---|
| `threading.Thread(target=fn, args=(...))` | Create a new thread |
| `t.start()` | Begin executing the thread |
| `t.join()` | Wait for the thread to finish before moving on |

### Why `join()` matters:
- Without `join()`, the main program might end **before** the threads finish
- `join()` says "wait here until this thread is done"
- Without it, `print("All done")` could run before the threads complete

### Passing arguments:
- `args=("Masala", 2)` — pass positional arguments as a **tuple**
- Single argument needs a trailing comma: `args=("Masala",)` — otherwise Python thinks it's just parentheses, not a tuple

---

## threading_example.py — Multiple Threads Running Together

```python
def take_orders():
    for i in range(5):
        print("Taking order", i)
        time.sleep(1)

def prepare_food():
    for i in range(5):
        print("Preparing food", i)
        time.sleep(2)

t1 = threading.Thread(target=take_orders)
t2 = threading.Thread(target=prepare_food)

t1.start()
t2.start()
t1.join()
t2.join()
```

### What the output looks like:
```
Taking order 0
Preparing food 0
Taking order 1          ← takes orders faster (1s sleep)
Taking order 2
Preparing food 1        ← prepares food slower (2s sleep)
Taking order 3
Taking order 4
Preparing food 2
...
```

- Both functions run **simultaneously** — their outputs are interleaved
- Orders are taken every 1 second while food is prepared every 2 seconds
- The output order may vary between runs — this is normal with threads

---

## RhreadDownload.py — Practical Example (Downloading Files)

### Why threading is perfect for downloads:
- Downloading files involves **waiting for network responses** (I/O-bound)
- While waiting for one download, the CPU is idle
- Threads let you start multiple downloads at once — use that idle time

```python
import requests

def download_file(url):
    print(f"Starting download from {url}...")
    response = requests.get(url)
    print(f"Finished. Content length: {len(response.content)} bytes.")

urls = ["https://httpbin.org/jpeg", "https://httpbin.org/png", "https://httpbin.org/svg"]

threads = []
for url in urls:
    t = threading.Thread(target=download_file, args=(url,))
    threads.append(t)
    t.start()              # start all downloads at once

for t in threads:
    t.join()               # wait for all to finish
```

### Pattern: Start all, then join all
1. Create and start all threads in one loop
2. Join all threads in a **separate** loop
3. This ensures all threads are running before you wait for any of them

### Without threading: download A → wait → download B → wait → download C → wait (slow)
### With threading: download A + B + C simultaneously → wait for all (fast!)

---

## ThreadLock.py — Thread Lock (Preventing Race Conditions)

### The Problem — Race Condition:
- When multiple threads modify the **same variable**, they can interfere with each other
- `counter += 1` is actually 3 steps: read → add 1 → write back
- If two threads read the same value before either writes, one increment is **lost**

```python
counter = 0

def increment():
    global counter
    for _ in range(100000):
        counter += 1        # NOT safe! Multiple threads can corrupt this

# Expected: 500000 (5 threads × 100000)
# Actual: might be 387423 or some random lower number — BUG!
```

### The Solution — Lock:
- A `Lock` ensures only **one thread at a time** can access the protected code
- Other threads must wait until the lock is released

```python
counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:           # acquire lock — only one thread enters at a time
            counter += 1     # safe! No other thread can touch this simultaneously
                             # lock is released when 'with' block ends
```

### How `with lock` works:
1. Thread A enters `with lock` — acquires the lock
2. Thread B tries to enter — **blocked**, waits
3. Thread A finishes `counter += 1` — lock is released
4. Thread B now enters — acquires the lock
5. Result: `counter` is always exactly `500000`

### Lock = like a bathroom lock — only one person at a time!

---

## GIL.py — Global Interpreter Lock (GIL)

### What is the GIL?
- The **Global Interpreter Lock** is a mutex in CPython that allows only **one thread to execute Python bytecode at a time**
- Even with multiple threads, only one actually runs Python code at any moment
- The GIL switches between threads rapidly, giving the **illusion** of parallelism

### Why does the GIL exist?
- CPython's memory management (reference counting) is **not thread-safe**
- The GIL prevents race conditions in Python's internal data structures
- It's a trade-off: simpler implementation but limited thread parallelism

### What this means for you:

| Task Type | Threading helps? | Why |
|---|---|---|
| **I/O-bound** (network, file, sleep) | YES | Thread releases GIL while waiting for I/O |
| **CPU-bound** (math, loops, counting) | NO | GIL prevents true parallel execution |

### The demo — threading is slow for CPU work:
```python
# Threading — runs 4 CPU-heavy tasks
# But GIL means they run ONE AT A TIME
# Total time: ~same as running them sequentially

# Multiprocessing — runs 4 CPU-heavy tasks
# Each process has its OWN Python interpreter and OWN GIL
# Total time: ~4x faster (true parallelism)
```

### Key takeaway:
- **I/O-bound tasks** (downloads, file reads, API calls) → use **threading**
- **CPU-bound tasks** (calculations, data processing) → use **multiprocessing**

---

# Part 2: Multiprocessing

## What is Multiprocessing?
- Instead of threads (which share the same process and GIL), multiprocessing creates **separate processes**
- Each process has its **own Python interpreter** and **own memory space**
- Processes run **truly in parallel** on different CPU cores — no GIL limitation

---

## Process_1.py vs process_2.py — Threading vs Multiprocessing Comparison

### Threading (Process_1.py) — limited by GIL:
```python
import threading

def cpu_heavy():
    count = 0
    for i in range(10**7):
        count += 1

t1 = [threading.Thread(target=cpu_heavy) for _ in range(4)]
[t.start() for t in t1]
[t.join() for t in t1]
# Slow — GIL means threads take turns
```

### Multiprocessing (process_2.py) — true parallelism:
```python
from multiprocessing import Process

def cpu_heavy():
    count = 0
    for i in range(10**7):
        count += 1

if __name__ == "__main__":
    p1 = [Process(target=cpu_heavy) for _ in range(4)]
    [t.start() for t in p1]
    [t.join() for t in p1]
    # Fast — each process runs on its own CPU core
```

### `if __name__ == "__main__":` — Why is this required?
- On Windows, multiprocessing **imports the module** in each new process
- Without this guard, the process creation code would run again inside each new process → infinite loop of spawning processes
- **Always** wrap multiprocessing code in `if __name__ == "__main__":`

---

## multiprocessing_.py — Multiple Processes

```python
from multiprocessing import Process

def brew_coffee(name):
    print(f"Brewing coffee for {name}")
    time.sleep(2)
    print(f"Coffee ready for {name}")

if __name__ == "__main__":
    chai_maker = [
        Process(target=brew_coffee, args=(f"Customer {i}",)) for i in range(5)
    ]

    for maker in chai_maker:
        maker.start()          # start all 5 processes

    for maker in chai_maker:
        maker.join()           # wait for all to finish
```

- Creates 5 separate processes — all brew coffee in parallel
- Each process runs independently with its own memory

---

## Process_value.py — Sharing Data Between Processes (`Value`)

### The Problem:
- Each process has its **own memory** — they can't share regular variables
- `global counter` doesn't work across processes like it does with threads

### The Solution — `Value`:
- `multiprocessing.Value` creates a **shared memory** variable that all processes can access

```python
from multiprocessing import Process, Value

def increment(counter):
    for _ in range(100000):
        with counter.get_lock():      # lock to prevent race conditions
            counter.value += 1

if __name__ == "__main__":
    counter = Value("i", 0)           # "i" = integer type, initial value 0
    processes = [Process(target=increment, args=(counter,)) for _ in range(4)]
    [p.start() for p in processes]
    [p.join() for p in processes]
    print(f"Final counter: {counter.value}")   # 400000 — correct!
```

### `Value("i", 0)` explained:
- First argument is the **type code**: `"i"` = integer, `"d"` = double (float)
- Second argument is the **initial value**
- `counter.value` accesses the actual number
- `counter.get_lock()` returns a built-in lock for safe access

### Why `Value` instead of a regular variable?
- Regular variables are **copied** into each process — changes in one don't affect others
- `Value` uses **shared memory** — all processes see the same data
- Still need a lock (`get_lock()`) to prevent race conditions, just like with threads

---

## process_queue.py — Communication Between Processes (`Queue`)

### The Problem:
- Processes can't share regular variables
- `Value` works for simple numbers, but what about sending messages or complex data?

### The Solution — `Queue`:
- A **queue** is a pipe between processes — one process puts data in, another takes it out
- FIFO: First In, First Out

```python
from multiprocessing import Process, Queue

def prepare_chai(queue):
    queue.put("masala chai is ready")     # put data INTO the queue

if __name__ == "__main__":
    q = Queue()
    p = Process(target=prepare_chai, args=(q,))
    p.start()
    p.join()
    print(q.get())     # "masala chai is ready" — get data FROM the queue
```

### Queue methods:
| Method | What it does |
|---|---|
| `q.put(data)` | Add data to the queue |
| `q.get()` | Remove and return data from the queue (waits if empty) |
| `q.empty()` | Check if queue is empty |

### Use cases:
- Process A generates data, Process B processes it (producer-consumer pattern)
- Collecting results from multiple worker processes
- Sending tasks to worker processes

---

## Summary: Threading vs Multiprocessing

| Feature | Threading | Multiprocessing |
|---|---|---|
| Module | `threading` | `multiprocessing` |
| Unit | Thread | Process |
| Memory | **Shared** (same process) | **Separate** (own memory) |
| GIL | Limited by GIL | **No GIL** — true parallelism |
| Best for | **I/O-bound** (network, files, sleep) | **CPU-bound** (calculations, loops) |
| Communication | Shared variables + Lock | `Value`, `Queue`, `Pipe` |
| Overhead | Lightweight (fast to create) | Heavier (slower to create) |
| `if __name__` guard | Not required | **Required** on Windows |

### Decision guide:
```
Is the task I/O-bound (waiting for network/files/user)?
  → YES → use threading
  → NO → Is it CPU-bound (heavy calculations)?
    → YES → use multiprocessing
    → NO → probably don't need either
```

### Thread safety tools:

| Tool | Module | What it does |
|---|---|---|
| `Lock` | `threading` | One thread at a time |
| `Value` | `multiprocessing` | Shared integer/float between processes |
| `Queue` | `multiprocessing` | Send data between processes (FIFO) |
| `get_lock()` | `multiprocessing.Value` | Lock for shared Value |
