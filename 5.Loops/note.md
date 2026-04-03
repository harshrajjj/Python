# Loops in Python - Notes

## What are Loops?
- Loops let you **repeat a block of code** multiple times without writing it again and again
- Python has two main loops: `for` (when you know how many times) and `while` (when you don't)

---

## Story 1: `for` Loop with `range()` (Basic Counting)

### What is `range()`?
- `range()` generates a **sequence of numbers** — it doesn't create a list, it produces numbers one at a time (memory efficient)
- `range(start, stop)` → generates numbers from `start` up to but **NOT including** `stop`
- `range(1, 11)` → gives 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

```python
for token in range(1, 11):
    print(f"Token number #{token}")
```

### How the `for` loop works:
1. `range(1, 11)` produces the next number
2. That number is stored in `token`
3. The indented code runs using that `token` value
4. Go back to step 1 until the range is exhausted

### `range()` variations:
| Syntax | What it does | Example |
|---|---|---|
| `range(stop)` | 0 to stop-1 | `range(5)` → 0, 1, 2, 3, 4 |
| `range(start, stop)` | start to stop-1 | `range(1, 5)` → 1, 2, 3, 4 |
| `range(start, stop, step)` | start to stop-1 in steps | `range(0, 10, 2)` → 0, 2, 4, 6, 8 |

---

## Story 2: `for` Loop with `range()` (Batches)

- Same concept as Story 1 — using `range(1, 5)` to loop through batch numbers 1 to 4

```python
for batch in range(1, 5):
    print(f"Preparing chai for batch #{batch}")
```

- Remember: `range(1, 5)` gives 1, 2, 3, 4 — the **stop value (5) is excluded**

---

## Story 3: Looping Over a List (Iterating Collections)

### Direct iteration:
- You can loop directly over any **iterable** (list, tuple, string, set, dict)
- Each iteration, the next item from the list is stored in the variable

```python
orders = ["harsh", "sai", "sumanth"]

for name in orders:        # name takes each value: "harsh", then "sai", then "sumanth"
    print(f"Preparing chai for {name}")
```

### What is an Iterable?
- Anything you can loop over: lists, tuples, strings, sets, dictionaries, range objects
- `"hello"` is iterable — looping gives `"h"`, `"e"`, `"l"`, `"l"`, `"o"` one by one

---

## Story 4: `enumerate()` (Get Index + Value)

### The Problem:
- When looping over a list, sometimes you need the **position (index)** along with the value
- You could use `range(len(menu))` and `menu[i]`, but that's ugly

### The Solution — `enumerate()`:
- `enumerate(iterable, start=0)` gives you **(index, value)** pairs
- `start=1` makes the count begin from 1 instead of 0

```python
menu = ["chai", "coffee", "milk", "juice"]

for idx, item in enumerate(menu, start=1):
    print(f"Preparing {item} for customer #{idx}")
```

Output:
```
Preparing chai for customer #1
Preparing coffee for customer #2
Preparing milk for customer #3
Preparing juice for customer #4
```

### Tuple unpacking in the loop:
- `enumerate()` returns tuples like `(1, "chai")`, `(2, "coffee")`, etc.
- `for idx, item in ...` unpacks each tuple into two separate variables automatically

---

## Story 5: `zip()` (Loop Over Multiple Lists Together)

### The Problem:
- You have two related lists and want to pair them up: names with their bills

### The Solution — `zip()`:
- `zip(list1, list2)` pairs up elements at the **same position** from both lists
- Stops at the **shortest** list (if lengths differ, extra items are ignored)

```python
names = ["harsh", "sai", "sumanth"]
bills = [100, 150, 200]

for name, bill in zip(names, bills):
    print(f"{name}'s bill is {bill}")
```

### How `zip()` pairs them:
```
("harsh", 100)  →  first iteration
("sai", 150)    →  second iteration
("sumanth", 200) → third iteration
```

### Zipping more than 2 lists:
```python
for a, b, c in zip(list1, list2, list3):  # works with any number of lists
```

---

## Story 6: `while` Loop (Loop Until a Condition is False)

### What is a `while` loop?
- Keeps running **as long as** the condition is `True`
- Stops the moment the condition becomes `False`
- Use when you **don't know in advance** how many times you need to loop

```python
temperature = 40

while temperature < 100:                       # keep going while temp is below 100
    print(f"Temperature is {temperature}°C, heating...")
    temperature += 15                           # increase temp each time

print("Water is boiling now!")
```

### Execution trace:
```
temperature = 40  → 40 < 100? YES → print, temp becomes 55
temperature = 55  → 55 < 100? YES → print, temp becomes 70
temperature = 70  → 70 < 100? YES → print, temp becomes 85
temperature = 85  → 85 < 100? YES → print, temp becomes 100
temperature = 100 → 100 < 100? NO → loop stops
```

### Infinite loop danger:
- If the condition **never** becomes `False`, the loop runs forever
- Always make sure something inside the loop **changes the condition**
- `Ctrl + C` to force-stop an infinite loop in the terminal

### `for` vs `while`:
| `for` loop | `while` loop |
|---|---|
| Know how many times to loop | Don't know how many times |
| Loop over a collection or range | Loop until a condition changes |
| Can't accidentally run forever | Can run forever if condition never becomes False |

---

## Story 7: `break` and `continue` (Loop Control)

### `continue` — Skip This Iteration:
- Skips the **rest of the current iteration** and jumps to the next one
- The loop keeps running, just this one round is skipped

### `break` — Stop the Entire Loop:
- **Exits the loop immediately** — no more iterations happen
- Code after the loop still runs

```python
flavours = ["ginger", "out of stock", "lemon", "discontinued", "Chocolate", "strawberry"]

for flavour in flavours:
    if flavour == "out of stock":
        continue                    # skip this one, go to next flavour
    if flavour == "discontinued":
        break                       # stop the entire loop RIGHT NOW
    print(f"{flavour} is available")
```

Output:
```
ginger is available          ← printed normally
                             ← "out of stock" skipped by continue
lemon is available           ← printed normally
                             ← "discontinued" hit break, loop stops
                             ← "Chocolate" and "strawberry" never reached
```

### Tuple unpacking in loops:
- A list of tuples can be unpacked directly in the `for` statement:

```python
staff = [("amit", 16), ("susan", 22), ("bob", 19), ("alice", 17)]

for name, age in staff:     # each tuple (name, age) is unpacked
    if age >= 18:
        print(f"{name} is an adult")
    else:
        print(f"{name} is a minor")
```

---

## Story 8: Walrus Operator `:=` (Assign and Use in One Step)

### What is the Walrus Operator?
- Written as `:=` — looks like a walrus on its side (eyes and tusks)
- It **assigns a value to a variable AND returns that value** at the same time
- Introduced in **Python 3.8**

### Without walrus (two steps):
```python
value = 15
remainder = value % 5       # Step 1: calculate
if remainder:                # Step 2: check
    print(f"Remainder is {remainder}")
```

### With walrus (one step):
```python
value = 15
if (remainder := value % 5):    # calculate AND check in one line
    print(f"Remainder is {remainder}")
```

### Walrus with `input()` — check and use:
```python
available_sizes = ["small", "medium", "large"]

if (requested := input("What size?")) in available_sizes:
    print(f"{requested} is available")       # requested is already assigned!
else:
    print(f"{requested} is not available")
```

### Walrus with `while` — input validation loop:
```python
flavours = ["ginger", "masala", "lemon", "mint"]

while (flavour := input("What flavour?")) not in flavours:
    print(f"{flavour} is not available, try again")

print(f"{flavour} is available")
```

- Without walrus, you'd need to call `input()` before the loop AND inside the loop (duplicate code)
- Walrus does the assignment inside the condition itself — cleaner!

### When to use walrus:
- When you need to **assign and check** a value in the same expression
- Input validation loops
- Avoiding repeated function calls
- **Don't** overuse it — readability is more important than saving one line

---

## Story 9: Practical Example (Loops + Dictionaries + Logic)

### The Scenario:
- A list of users, each with an order total and a coupon code
- A dictionary mapping coupon codes to their discount values (percentage, fixed amount)
- Loop through users and calculate their discount

```python
users = [
    {"id": 1, "total": 100, "coupon": "p10"},
    {"id": 2, "total": 200, "coupon": "p10"},
    {"id": 3, "total": 300, "coupon": "f10"},
    {"id": 4, "total": 400, "coupon": "f50"},
    {"id": 5, "total": 500, "coupon": "p20"},
]

discount = {
    "p10": (0.1, 0),    # 10% off, no fixed discount
    "p20": (0.2, 0),    # 20% off, no fixed discount
    "f10": (0, 10),     # no percentage, flat 10 rupees off
    "f50": (0, 50),     # no percentage, flat 50 rupees off
}
```

### Key concepts used:

**1. List of dictionaries** — common pattern to represent records/rows of data

**2. Dictionary `.get()` with default:**
```python
percent, fixed = discount.get(user["coupon"], (0, 0))
```
- Looks up the coupon code in the discount dictionary
- If coupon doesn't exist, returns `(0, 0)` as default — no crash
- Tuple unpacking assigns both values at once

**3. Calculation:**
```python
discount_amount = user["total"] * percent + fixed
```
- For `"p10"` with total 100: `100 * 0.1 + 0 = 10` rupees discount
- For `"f50"` with total 400: `400 * 0 + 50 = 50` rupees discount

### This combines everything:
- `for` loop to iterate over users
- Dictionary lookup with `.get()`
- Tuple unpacking
- f-string formatting
- Arithmetic operations

---

## Summary: All Loop Tools

| Tool | Purpose | Example |
|---|---|---|
| `for` + `range()` | Loop a known number of times | `for i in range(10):` |
| `for` + list | Loop over each item | `for x in items:` |
| `enumerate()` | Get index + value | `for i, x in enumerate(items):` |
| `zip()` | Loop over multiple lists together | `for a, b in zip(l1, l2):` |
| `while` | Loop until condition is False | `while temp < 100:` |
| `break` | Exit loop immediately | `if done: break` |
| `continue` | Skip to next iteration | `if skip: continue` |
| `:=` walrus | Assign + check in one expression | `while (x := input()) != "q":` |
