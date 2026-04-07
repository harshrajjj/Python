# Generators and Decorators in Python - Notes

---

# Part 1: Generators

## What is a Generator?
- A generator is a special kind of function that **produces values one at a time** using `yield` instead of `return`
- It **pauses** after each `yield` and **resumes** from where it left off when you ask for the next value
- Think of it like a bookmark — it remembers where it stopped

### Key difference from regular functions:
- `return` → gives one result and the function is **done forever**
- `yield` → gives one result, **pauses**, and can give more results later

---

## generators.py — Basic Generator with `yield`

### How `yield` works:
```python
def serve_chai():
    yield "Boil water"       # pause here, give this value
    yield "Add tea leaves"   # when asked again, resume and give this
    yield "Add milk"         # when asked again, give this

stall = serve_chai()         # creates a generator object (nothing runs yet!)
```

### Important: Calling a generator function does NOT run it!
- `serve_chai()` does **not** execute the code — it creates a **generator object**
- The code only runs when you **iterate** over it or call `next()`

### Two ways to get values:

**1. Using a `for` loop (recommended):**
```python
for cup in stall:
    print(cup)
# "Boil water"
# "Add tea leaves"
# "Add milk"
```

**2. Using `next()` manually:**
```python
chai = get_chai_gen()

print(next(chai))   # "cup 1" — runs until first yield, pauses
print(next(chai))   # "cup 2" — resumes, runs until second yield, pauses
print(next(chai))   # "cup 3" — resumes, runs until third yield, pauses
print(next(chai))   # StopIteration ERROR — no more yields!
```

### `StopIteration` error:
- When there are no more `yield` statements, calling `next()` raises `StopIteration`
- `for` loops handle this automatically — they stop when `StopIteration` is raised
- With `next()` you need to be careful or handle the error yourself

### Generator vs Regular function returning a list:
```python
# Regular function — creates entire list in memory at once:
def get_chai_list():
    return ["Boil water", "Add tea leaves", "Add milk"]

# Generator — produces one item at a time:
def get_chai_gen():
    yield "cup 1"
    yield "cup 2"
    yield "cup 3"
```

| Regular Function (return list) | Generator (yield) |
|---|---|
| All values stored in memory at once | One value at a time |
| Returns a list | Returns a generator object |
| Can access by index `[0]` | Can only go forward with `next()` |
| Good for small data | Essential for large/infinite data |

---

## infiniteGenerators.py — Infinite Generator

### The Problem:
- You can't create an infinite list — your memory would run out
- But you CAN create an infinite generator — it only produces one value at a time

```python
def infinite_chai():
    count = 1
    while True:              # infinite loop!
        yield "cup " + str(count)
        count += 1

refill = infinite_chai()

for _ in range(5):           # only take 5 values from the infinite generator
    print(next(refill))
# "cup 1", "cup 2", "cup 3", "cup 4", "cup 5"
```

### Why this doesn't crash:
- `while True` would normally be an infinite loop
- But `yield` **pauses** the function after each value
- The generator only runs when you ask for the next value with `next()`
- You control how many values to take — the generator just sits there waiting

### Use cases for infinite generators:
- Reading a stream of data (logs, sensors, live feeds)
- Generating unique IDs
- Producing values until a condition is met externally

---

## sendgenerators.py — Sending Values INTO a Generator

### What is `.send()`?
- Normally generators only **output** values (with `yield`)
- `.send()` lets you **input** values back into the generator
- The sent value becomes the result of the `yield` expression

```python
def chai_customer():
    print("Welcome to the chai shop")
    order = yield                    # pause and WAIT for a value to be sent
    while True:
        print(f"Here is your {order}")
        order = yield               # pause again and wait for next value

stall = chai_customer()

next(stall)                          # "prime" the generator — runs until first yield
stall.send("chai")                   # sends "chai" → order becomes "chai"
stall.send("chai with ginger")       # sends "chai with ginger" → order becomes that
```

### Step by step:
1. `next(stall)` — runs the generator until the first `yield`, prints "Welcome...", then pauses
2. `stall.send("chai")` — resumes the generator, `order` receives `"chai"`, prints "Here is your chai", hits `yield` again, pauses
3. `stall.send("chai with ginger")` — same process, `order` receives the new value

### Why `next()` first?
- You MUST call `next()` once before using `.send()` — this is called **priming** the generator
- The generator needs to advance to the first `yield` before it can receive values
- Alternatively, `stall.send(None)` works the same as `next(stall)` for priming

---

## closeGenerator.py — `yield from` and `.close()`

### `yield from` — Delegate to another generator:
```python
def local_chai():
    yield "masala chai"
    yield "ginger chai"

def important_chai():
    yield "matcha"
    yield "oolong"

def full_chai():
    yield from local_chai()        # yields all items from local_chai
    yield from important_chai()    # then yields all items from important_chai

for chai in full_chai():
    print(chai)
# "masala chai", "ginger chai", "matcha", "oolong"
```

### Why `yield from`?
- Without it, you'd need a loop: `for item in local_chai(): yield item`
- `yield from` does the same thing in one clean line
- It **delegates** the yielding to another generator

### `.close()` — Shut down a generator:
```python
def chai_stall():
    try:
        while True:
            order = yield "waiting for order"
    except GeneratorExit:          # triggered by .close()
        print("Stall is closed")

stall = chai_stall()
print(next(stall))   # "waiting for order"
stall.close()        # "Stall is closed" — generator is shut down
```

### How `.close()` works:
- Calling `.close()` raises a `GeneratorExit` exception **inside** the generator
- You can catch it with `try/except` to run cleanup code (close files, save state, etc.)
- After `.close()`, the generator is **done** — calling `next()` raises `StopIteration`

---

# Part 2: Decorators

## What is a Decorator?
- A decorator is a function that **wraps another function** to add extra behavior
- It takes a function as input, adds something before/after it, and returns a new enhanced function
- Uses the `@decorator_name` syntax — placed above the function definition

### The mental model:
Think of it like wrapping a gift — the gift (original function) is the same, but the wrapping (decorator) adds something extra around it.

---

## decorations.py — Basic Decorator

### How a decorator works step by step:

```python
from functools import wraps

def my_decorator(func):         # Step 1: Takes a function as input
    @wraps(func)
    def wrapper():              # Step 2: Creates a new function that wraps the original
        print("Before the function")
        func()                  # Step 3: Calls the original function
        print("After the function")
    return wrapper              # Step 4: Returns the wrapper function

@my_decorator                   # Step 5: Apply the decorator
def greet():
    print("Hello!")

greet()
```

Output:
```
Before the function
Hello!
After the function
```

### What `@my_decorator` actually does:
```python
@my_decorator
def greet():
    print("Hello!")

# Is EXACTLY the same as:
def greet():
    print("Hello!")
greet = my_decorator(greet)     # replace greet with the wrapped version
```

- `@` is just **syntactic sugar** — a shortcut for reassigning the function

### What is `@wraps(func)`?
- Without `@wraps`, the wrapped function loses its original name and docstring
- `greet.__name__` would return `"wrapper"` instead of `"greet"`
- `@wraps(func)` preserves the original function's metadata (name, docstring, etc.)

```python
print(greet.__name__)   # "greet" (thanks to @wraps)
                        # Without @wraps, this would print "wrapper"
```

- **Always use `@wraps`** when writing decorators — import it from `functools`

---

## loggingDecorator.py — Decorator with Arguments (`*args`, `**kwargs`)

### The problem:
- The basic decorator's wrapper takes no arguments
- But what if the original function takes arguments?

### The solution — use `*args` and `**kwargs`:
```python
from functools import wraps

def logging_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):                         # accept ANY arguments
        print(f"Calling '{func.__name__}' with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)                    # pass them to the original
        print(f"'{func.__name__}' returned: {result}")
        return result                                     # return the original result
    return wrapper

@logging_decorator
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
```

Output:
```
Calling 'add_numbers' with args: (3, 5), kwargs: {}
'add_numbers' returned: 8
```

### Why `*args, **kwargs`?
- Makes the decorator **universal** — it can wrap ANY function regardless of its parameters
- `*args` captures positional arguments as a tuple
- `**kwargs` captures keyword arguments as a dictionary
- `func(*args, **kwargs)` passes them all through to the original function

### Important — return the result:
- If the original function returns something, the wrapper must `return result` too
- Otherwise the decorated function would always return `None`

---

## authDecorator.py — Practical Decorator (Access Control)

### Real-world use case — checking permissions:
```python
from functools import wraps

def auth_decorator(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role == 'admin':
            print("Access granted.")         # admin gets special treatment
        else:
            return func(user_role)           # non-admin runs the original function
    return wrapper

@auth_decorator
def access_resource(user_role):
    print(f"Access denied for user role: {user_role}")

access_resource('admin')   # "Access granted."
access_resource('user')    # "Access denied for user role: user"
```

### How it works:
1. When `access_resource('admin')` is called, it actually calls `wrapper('admin')`
2. Wrapper checks: is the role `"admin"`? YES → print "Access granted", skip the original function
3. When `access_resource('user')` is called, wrapper checks: is it admin? NO → run the original function

### Common real-world decorator use cases:
| Decorator | Purpose |
|---|---|
| `@login_required` | Check if user is logged in before accessing a page |
| `@cache` / `@lru_cache` | Cache function results to avoid recalculating |
| `@timer` | Measure how long a function takes to run |
| `@retry` | Retry a function if it fails (with limit) |
| `@validate` | Check input before running the function |

---

## Summary

### Generators:

| Concept | What it does |
|---|---|
| `yield` | Produce a value and pause the function |
| `next()` | Resume the generator and get the next value |
| `StopIteration` | Error when generator has no more values |
| Infinite generator | `while True` + `yield` — produces values forever |
| `.send(value)` | Send a value INTO the generator |
| `yield from` | Delegate to another generator |
| `.close()` | Shut down a generator, triggers `GeneratorExit` |

### Decorators:

| Concept | What it does |
|---|---|
| `@decorator` | Wrap a function with extra behavior |
| `wrapper(*args, **kwargs)` | Make decorator work with any function |
| `@wraps(func)` | Preserve original function's name and docstring |
| `return result` | Pass through the original function's return value |
