# Functions in Python - Notes

## What is a Function?
- A function is a **reusable block of code** that performs a specific task
- You define it once with `def`, then call it as many times as you need
- Functions help you avoid repeating code and keep things organized

### Basic syntax:
```python
def function_name(parameters):
    # code here
    return value  # optional
```

---

## Story 1: Defining and Calling Functions (Basics)

### How to define a function:
- Use `def` keyword, followed by the function name, parentheses, and a colon
- The code inside the function must be **indented**

```python
def print_order(name, chai_type):
    print(f"{name} ordered a {chai_type} chai.")

print_order("aman", "masala")  # calling the function
```

### Functions calling other functions:
- A function can call other functions inside it — this is how you **break big tasks into small steps**

```python
def generate_report():
    fetch_sales()           # Step 1
    filter_valid_sales()    # Step 2
    summerize_sales()       # Step 3
    print("Report done!")

generate_report()  # one call does all 3 steps
```

### Why this is powerful:
- Each function has **one job** (Single Responsibility)
- Easy to test, debug, and modify individual steps
- The main function reads like a to-do list

---

## Story 2: Return Values and Using Results

### `return` statement:
- `return` sends a value **back** to where the function was called
- Without `return`, a function returns `None` by default
- The function **stops executing** as soon as it hits `return`

```python
def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup    # sends the result back

mybill = calculate_bill(3, 5)      # mybill = 15
```

### Using return values in loops:
```python
def add_vat(price, vat_rate):
    return price * (100 + vat_rate) / 100

orders = [100, 150, 200]
for order in orders:
    total = add_vat(order, 20)     # use the returned value
    print(f"Original: {order}, With VAT: {total}")
```

### Functions as building blocks:
- One function's return value can be passed as input to another function
- This is how you build complex logic from simple pieces

---

## Story 3: Scope — Local vs Global Variables

### What is Scope?
- **Scope** determines where a variable can be accessed
- A variable created **inside** a function is **local** — it only exists inside that function
- A variable created **outside** all functions is **global** — it can be read everywhere

### Local scope:
```python
def serve_chai():
    chai_type = "masala chai"    # local — only exists inside this function
    print(chai_type)             # works fine

chai_type = "ginger chai"       # global — different variable, same name!
serve_chai()                    # prints "masala chai"
print(chai_type)                # prints "ginger chai" — global was NOT changed
```

### Key rule: Local variables **shadow** global ones
- If a function has a variable with the same name as a global, the **local one wins** inside that function
- The global variable is **untouched** — Python creates a completely separate local variable

### Nested function scope:
```python
def chai_counter():
    chai_order = "lemon"          # outer function's local variable
    def print_order():
        chai_order = "masala"     # inner function's OWN local variable
        print("inner:", chai_order)   # "masala"
    print_order()
    print("outer:", chai_order)       # still "lemon" — inner didn't change it
```

- Each function has its **own scope** — inner functions can't modify outer variables by default

---

## Story 4: `nonlocal` and `global` Keywords

### The Problem:
- By default, inner functions **can't modify** outer function variables
- By default, functions **can't modify** global variables
- `nonlocal` and `global` keywords override this

### `nonlocal` — Modify the outer function's variable:
```python
def update_order():
    chai_type = "Elaichi"
    def kitchen():
        nonlocal chai_type       # "I want to modify the OUTER function's chai_type"
        chai_type = "kesar"      # this NOW changes the outer variable
    kitchen()
    print(chai_type)             # "kesar" — it was modified!
```

### `global` — Modify the global variable from inside a function:
```python
chai = "plain"                   # global variable

def front_desk():
    def kitchen():
        global chai              # "I want to modify the GLOBAL chai"
        chai = "Irani"           # this NOW changes the global variable
    kitchen()

front_desk()
print(chai)                      # "Irani" — global was modified
```

### When to use:
| Keyword | What it does | When to use |
|---|---|---|
| `nonlocal` | Modify enclosing function's variable | Nested functions that need to update outer state |
| `global` | Modify module-level variable | **Rarely** — generally avoid, makes code harder to debug |

---

## Story 5: Parameters Deep Dive — `*args`, `**kwargs`, and Mutability

### Passing immutable vs mutable objects:
- **Immutable (strings, ints, tuples)**: Function gets a copy of the reference — can't change the original
- **Mutable (lists, dicts, sets)**: Function gets the SAME object — changes affect the original!

```python
chai = [1, 2, 3]
def edit_chai(cup):
    cup[1] = 42          # modifies the ORIGINAL list!

edit_chai(chai)
print(chai)              # [1, 42, 3] — the original list was changed
```

### Positional vs Keyword arguments:
```python
def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

# Positional — order matters:
make_chai("green tea", "full cream", "less sugar")

# Keyword — order doesn't matter:
make_chai(milk="full cream", sugar="less sugar", tea="green tea")
```

### `*args` — Accept any number of positional arguments:
- Collects extra positional arguments into a **tuple**

### `**kwargs` — Accept any number of keyword arguments:
- Collects extra keyword arguments into a **dictionary**

```python
def special_chai(*args, **kwargs):
    print("args:", args)       # ("green tea", "full cream", "less sugar")
    print("kwargs:", kwargs)   # {"flavor": "elaichi", "size": "large"}

special_chai("green tea", "full cream", "less sugar", flavor="elaichi", size="large")
```

### Mutable default argument trap:
```python
# DANGEROUS — the default list is shared across ALL calls:
def chai_order(order=[]):
    order.append("masala")
    print(order)

chai_order()  # ["masala"]
chai_order()  # ["masala", "masala"] — BUG! List persists between calls

# SAFE — use None as default:
def chai_order(order=None):
    if order is None:
        order = []       # fresh list every time
    print(order)
```

- **Why this happens**: Default values are created **once** when the function is defined, not each time it's called
- **Rule**: Never use mutable objects (list, dict, set) as default arguments — use `None` instead

---

## Story 6: Return Patterns

### Returning a value:
```python
def make_chai():
    return "masala chai"

result = make_chai()   # result = "masala chai"
```

### `pass` — Empty function placeholder:
```python
def ideal_chai():
    pass              # does nothing — placeholder for future code

print(ideal_chai())   # None — no return means None
```

- Use `pass` when you want to define a function but haven't written the code yet
- Without `pass`, an empty function would cause a syntax error

### Early return (conditional return):
```python
def chai_status(cups):
    if cups > 3:
        return "too much chai"     # function STOPS here if True
    elif cups == 3:
        return "just right"
    else:
        return "not enough chai"
```

- Once a `return` is hit, the function **immediately exits** — no code below it runs

### Returning multiple values:
```python
def chai_report():
    return 100, 20, 10             # returns a tuple: (100, 20, 10)

sold, remaining, _ = chai_report()  # unpack into variables
```

- Python actually returns a **tuple** — you can unpack it into separate variables
- `_` is a convention for "I don't care about this value" (throwaway variable)

---

## Story 7: Pure vs Impure Functions, Recursion, and Lambda

### Pure Function:
- **Always** returns the same output for the same input
- Has **no side effects** — doesn't modify anything outside itself
- Easier to test, debug, and reason about

```python
def pure_chai(cups):
    return cups * 5       # same input → same output, always
```

### Impure Function:
- Modifies something **outside** itself (global variable, file, database)
- Same input might give different results depending on external state

```python
total_chai = 0

def impure_chai(cups):
    global total_chai
    total_chai += cups * 5   # modifies global state — side effect!
```

- **Prefer pure functions** whenever possible — they're predictable and safe

### Recursion — Function calling itself:
```python
def pore_chai(n):
    if n == 0:
        return "All cups are served"   # base case — STOPS the recursion
    else:
        return pore_chai(n - 1)        # recursive case — calls itself with smaller n
```

- **Base case**: The condition that stops the recursion (without it → infinite loop → crash)
- **Recursive case**: The function calls itself with a simpler/smaller problem
- Each call waits for the inner call to finish before completing

### Execution trace for `pore_chai(3)`:
```
pore_chai(3) → calls pore_chai(2)
  pore_chai(2) → calls pore_chai(1)
    pore_chai(1) → calls pore_chai(0)
      pore_chai(0) → returns "All cups are served"
    returns "All cups are served"
  returns "All cups are served"
returns "All cups are served"
```

### Lambda — Anonymous (one-line) function:
```python
# Regular function:
def is_masala(chai):
    return chai == "masala"

# Same thing as lambda:
is_masala = lambda chai: chai == "masala"
```

- `lambda parameters: expression` — no `def`, no `return`, no name needed
- Can only contain a **single expression** (no multiple lines, no if-else blocks)

### `filter()` with Lambda:
```python
chai_types = ["masala", "ginger", "lemon", "masala", "ginger", "lemon"]

strong_chai = list(filter(lambda chai: chai == "masala", chai_types))
# Result: ["masala", "masala"]
```

- `filter(function, iterable)` keeps only items where the function returns `True`
- `list()` converts the filter result back to a list

### Common higher-order functions:
| Function | What it does | Example |
|---|---|---|
| `filter(fn, list)` | Keep items where fn returns True | Filter only "masala" |
| `map(fn, list)` | Apply fn to every item | Double all prices |
| `sorted(list, key=fn)` | Sort using fn as the sorting key | Sort by price |

---

## Story 8: Docstrings and Function Metadata

### What is a Docstring?
- A string written as the **first line** inside a function, enclosed in triple quotes `"""`
- It describes what the function does
- Not a comment — it's stored as part of the function object and can be accessed programmatically

```python
def chai_flavor(flavour="masala"):
    """return the flavor of chai"""
    chai = "ginger"
    return flavour
```

### Accessing function metadata:
```python
print(chai_flavor.__doc__)    # "return the flavor of chai"
print(chai_flavor.__name__)   # "chai_flavor"
```

- `__doc__` → the docstring (the description you wrote)
- `__name__` → the function's name as a string

### Why docstrings matter:
- `help(chai_flavor)` uses the docstring to show documentation
- IDEs show docstrings as tooltips when you hover over a function
- Tools like Sphinx can auto-generate documentation from docstrings

### Docstring vs Comment:
| Docstring (`"""..."""`) | Comment (`# ...`) |
|---|---|
| First line inside a function | Anywhere in code |
| Stored in `__doc__` attribute | Ignored by Python completely |
| Accessible at runtime | Not accessible at runtime |
| Describes **what** the function does | Explains **why** something is done |

---

## Story 9: Importing Functions

### Types of imports:
```python
# Import entire module:
import math
math.sqrt(16)              # must use module.function

# Import specific function:
from math import sqrt
sqrt(16)                   # use directly, no prefix

# Import with alias:
import numpy as np
np.array([1, 2, 3])       # shorter name

# Import everything (NOT recommended):
from math import *         # pollutes namespace, hard to track where things come from
```

### Why importing matters:
- Python has a huge **standard library** (built-in modules) — no need to reinvent the wheel
- Third-party packages (installed via `pip`) are also imported this way
- Your own `.py` files are modules too — you can import functions from one file into another

---

## Summary: All Function Concepts

| Concept | What it does |
|---|---|
| `def` | Define a function |
| `return` | Send a value back to the caller |
| `pass` | Placeholder for empty function |
| Scope (local/global) | Controls where variables are accessible |
| `nonlocal` | Modify outer function's variable |
| `global` | Modify global variable from inside function |
| `*args` | Accept any number of positional arguments |
| `**kwargs` | Accept any number of keyword arguments |
| Default `None` for mutables | Avoid the mutable default argument trap |
| Pure function | No side effects, same input → same output |
| Recursion | Function calls itself with a base case |
| `lambda` | One-line anonymous function |
| `filter()` / `map()` | Higher-order functions with lambdas |
| Docstring (`"""..."""`) | Document what a function does |
| `__doc__` / `__name__` | Access function metadata |
| `import` / `from...import` | Reuse code from other modules |
