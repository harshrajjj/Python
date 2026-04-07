# Files and Exception Handling in Python - Notes

---

# Part 1: Exception Handling

## What is an Exception?
- An exception is an **error that happens while your code is running** (not a syntax error)
- If unhandled, it **crashes your program** and shows a traceback
- Exception handling lets you **catch errors gracefully** and keep the program running

---

## basic.py — What Happens Without Handling

### Unhandled exception:
```python
order = ["masala dosa", "plain dosa", "onion dosa", "paper dosa"]
print(order[9])   # IndexError: list index out of range — CRASH!
```

- The list has 4 items (index 0-3), but we tried to access index 9
- Python raises `IndexError` and the program **stops immediately**
- Everything after this line **never runs**

### Common exception types:

| Exception | When it happens |
|---|---|
| `IndexError` | Accessing a list index that doesn't exist |
| `KeyError` | Accessing a dictionary key that doesn't exist |
| `TypeError` | Wrong type (e.g., `"hello" * "world"`) |
| `ValueError` | Right type, wrong value (e.g., `int("abc")`) |
| `FileNotFoundError` | Trying to open a file that doesn't exist |
| `ZeroDivisionError` | Dividing by zero |
| `AttributeError` | Accessing an attribute/method that doesn't exist |

---

## tryExcept.py — `try` / `except` (Catching Errors)

### How it works:
- `try` block: put the code that **might fail** here
- `except` block: runs **only if** an error occurs in the try block
- If no error occurs, the except block is **skipped entirely**

```python
chai = {"masala": 10, "plain": 5, "onion": 15}

try:
    print(chai["ginger"])          # KeyError! "ginger" doesn't exist
except KeyError:
    print("Sorry, we don't have that flavor.")
```

### Without try/except:
```python
print(chai["ginger"])   # CRASH — KeyError, program stops
```

### With try/except:
```python
try:
    print(chai["ginger"])          # error happens here
except KeyError:                   # caught! program continues
    print("Sorry, we don't have that flavor.")

# Code here still runs — program didn't crash
```

### Using inside a function:
```python
def serve_chai(flavor):
    try:
        print(f"Your {flavor} chai costs {chai[flavor]} rupees.")
    except KeyError:
        print("Sorry, we don't have that flavor.")

serve_chai("ginger")   # "Sorry, we don't have that flavor."
serve_chai("masala")   # "Your masala chai costs 10 rupees."
```

---

## multipleException.py — Catching Multiple Exception Types

### The Problem:
- Different operations can raise **different types** of errors
- You might want to handle each one differently

### Catching multiple exceptions separately:
```python
def process_order(item, quantity):
    try:
        price = {"masala": 20}[item]    # could raise KeyError
        total = price * quantity         # could raise TypeError
        print(f"Total: {total} rupees.")
    except KeyError:
        print("Sorry, we don't have that item.")
    except TypeError:
        print("Quantity must be a number.")

process_order("ginger", 2)      # KeyError → "Sorry, we don't have that item."
process_order("masala", "two")   # TypeError → "Quantity must be a number."
```

### Why `"masala" * "two"` fails:
- `price * quantity` → `20 * "two"` → you can't multiply an int by a string that isn't a number
- Python raises `TypeError`

### Order matters:
- Python checks `except` blocks **top to bottom** — the first matching one runs
- Put **specific** exceptions first, **general** ones last
- `except Exception` catches almost everything — use it as a fallback, not the first option

```python
try:
    ...
except KeyError:        # specific — checked first
    ...
except TypeError:       # specific — checked second
    ...
except Exception:       # general — catches anything else (last resort)
    ...
```

---

## complete_order.py — `raise` (Throwing Your Own Exceptions)

### What is `raise`?
- `raise` lets you **manually trigger** an exception
- Useful when your code detects something wrong that Python wouldn't catch on its own

```python
def brew_chai(flavor):
    if flavor not in ["masala", "plain", "onion", "paper"]:
        raise ValueError("Sorry, we don't have that flavor.")
    else:
        print(f"Here is your {flavor} chai.")

try:
    brew_chai("ginger")          # raises ValueError
except ValueError as e:
    print(e)                     # "Sorry, we don't have that flavor."
```

### `as e` — Accessing the error message:
- `except ValueError as e:` captures the exception object in variable `e`
- `print(e)` shows the message you passed when raising
- Useful for logging or showing the user what went wrong

### When to use `raise`:
- Input validation — rejecting invalid data before it causes deeper problems
- Business rules — "you can't order more than 10 cups"
- When the error isn't something Python would detect automatically

---

## customException.py — Creating Custom Exceptions

### Why custom exceptions?
- Built-in exceptions (`ValueError`, `KeyError`) are generic
- Custom exceptions give your errors **meaningful names** specific to your program
- Makes error handling more readable and organized

### How to create one:
```python
class InvalidChaiError(Exception):
    pass                          # no extra logic needed — just inherit from Exception
```

### Using it:
```python
def bill(flavour, cups):
    menu = {"masala": 20, "plain": 10, "onion": 15, "paper": 25}
    try:
        if flavour not in menu:
            raise InvalidChaiError("Sorry, we don't have that flavor.")
        else:
            total = menu[flavour] * cups
            print(f"Total for {cups} {flavour} chai: {total} rupees.")
    except Exception as e:
        print(e)

bill("ginger", 2)   # "Sorry, we don't have that flavor."
bill("masala", 2)    # "Total for 2 masala chai: 40 rupees."
```

### How it works:
1. `class InvalidChaiError(Exception): pass` — creates a new exception type
2. `raise InvalidChaiError("message")` — throws it with a custom message
3. `except Exception as e` — catches it (since `InvalidChaiError` inherits from `Exception`)

---

## custom_except2.py — Another Custom Exception Example

```python
class outOfIngredient(Exception):
    pass

def make_chai(milk, sugar):
    if milk == 0 or sugar == 0:
        raise outOfIngredient("Sorry, we are out of ingredients.")
    else:
        print("Here is your chai.")

make_chai(1, 2)    # "Here is your chai."
make_chai(0, 2)    # outOfIngredient: Sorry, we are out of ingredients. — CRASH!
```

### Notice:
- This code **doesn't catch** the exception — it just raises it
- Without a `try/except`, the program will crash when `make_chai(0, 2)` is called
- To handle it gracefully, wrap the call in `try/except`:

```python
try:
    make_chai(0, 2)
except outOfIngredient as e:
    print(e)
```

---

# Part 2: File Handling

## fileHandling.py — Reading and Writing Files

### The Old Way (manual close):
```python
file = open("orders.txt", "w")
try:
    order = ["masala dosa", "plain dosa", "onion dosa"]
    for item in order:
        file.write(item + "\n")
except Exception as e:
    print(e)
finally:
    file.close()        # MUST close the file, even if an error occurs
```

### `finally` block:
- Runs **no matter what** — whether the try succeeds or fails
- Used for cleanup: closing files, releasing resources, disconnecting from databases
- Even if an exception is raised, `finally` still runs

### The Modern Way — `with` statement (recommended):
```python
with open("orders.txt", "w") as file:
    order = ["masala dosa", "plain dosa", "onion dosa", "paper dosa"]
    for item in order:
        file.write(item + "\n")
# file is automatically closed when the with block ends
```

### Why `with` is better:
- **Automatically closes** the file when the block ends — even if an error occurs
- No need for `try/finally/file.close()` — cleaner and safer
- Uses Python's **context manager** protocol (`__enter__` and `__exit__` methods)

### File modes:

| Mode | What it does |
|---|---|
| `"r"` | **Read** — default, file must exist |
| `"w"` | **Write** — creates file or **overwrites** existing content |
| `"a"` | **Append** — adds to end of file, doesn't delete existing content |
| `"x"` | **Create** — creates file, fails if it already exists |
| `"r+"` | **Read + Write** — file must exist |
| `"b"` | **Binary mode** — add to other modes (e.g., `"rb"`, `"wb"`) |

### Common file operations:
```python
# Write to a file:
with open("file.txt", "w") as f:
    f.write("Hello\n")

# Read entire file:
with open("file.txt", "r") as f:
    content = f.read()

# Read line by line:
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())       # .strip() removes the trailing \n

# Append to a file:
with open("file.txt", "a") as f:
    f.write("New line\n")
```

---

## Summary: try/except Full Structure

```python
try:
    # code that might fail
except SpecificError as e:
    # handle specific error
except AnotherError as e:
    # handle another specific error
except Exception as e:
    # catch-all for any other error
else:
    # runs ONLY if no exception occurred (optional)
finally:
    # runs NO MATTER WHAT — cleanup code (optional)
```

| Block | When it runs |
|---|---|
| `try` | Always runs first |
| `except` | Only if an error matches |
| `else` | Only if NO error occurred |
| `finally` | Always — error or not |

### Best practices:
- **Be specific** — catch `KeyError`, not `Exception`, when you know the error type
- **Don't catch everything silently** — `except: pass` hides bugs
- **Use `with`** for files — never manually `open()`/`close()`
- **Raise early, catch late** — validate inputs as soon as possible, handle errors at the right level
- **Custom exceptions** — use them when built-in ones don't describe the problem well enough
