# Conditionals in Python - Notes

## What are Conditionals?
- Conditionals let your program **make decisions** — run different code based on whether a condition is `True` or `False`
- They are the "if this, then that" of programming
- Without conditionals, your code would always do the exact same thing every time

---

## Mini Story 1: `if` / `else` (Basic Conditional)

### How it works:
- `if` checks a condition — if it's `True`, the indented code below runs
- `else` runs when the `if` condition is `False` — it's the fallback

```python
kettle_boiled = True

if kettle_boiled:           # Is this True?
    print("Time to make tea!")   # YES → this runs
else:
    print("Please wait.")        # NO → this would run instead
```

### Key points:
- The condition after `if` must evaluate to `True` or `False`
- `if kettle_boiled:` is shorthand for `if kettle_boiled == True:`
- **Indentation matters** — Python uses indentation (4 spaces) to know which code belongs inside the `if` or `else` block
- The colon `:` at the end of `if` and `else` is required

---

## Mini Story 2: `or` Operator and `input()` (Multiple Conditions)

### `input()` function:
- `input("message")` pauses the program and waits for the user to type something
- It always returns a **string**, even if the user types a number
- `.lower()` converts the input to lowercase so "Cookies", "COOKIES", "cookies" all match

### `or` operator:
- Checks if **at least one** condition is `True`

```python
snack = input("enter your prefer snack: ").lower()

if snack == "cookies" or snack == "samosa":   # True if EITHER matches
    print(f"great choice! {snack} are delicious.")
else:
    print(f"Sorry, we don't have {snack} in our menu.")
```

### Common mistake:
```python
# WRONG — this doesn't work as expected:
if snack == "cookies" or "samosa":    # "samosa" is always truthy!

# CORRECT — compare each value separately:
if snack == "cookies" or snack == "samosa":
```

---

## Mini Story 3: `elif` (Multiple Branches)

### What is `elif`?
- Short for **"else if"** — checks another condition if the previous one was `False`
- You can have as many `elif` blocks as you need
- Python checks them **top to bottom** and runs the FIRST one that is `True`, then skips the rest

```python
cup_size = input("Enter your cup size: ").lower()

if cup_size == "small":          # Check 1
    print("250ml")
elif cup_size == "medium":       # Check 2 (only if Check 1 was False)
    print("500ml")
elif cup_size == "large":        # Check 3 (only if Check 1 & 2 were False)
    print("1000ml")
else:                            # Fallback (if ALL checks were False)
    print("Invalid cup size.")
```

### Flow:
```
if → False? → elif → False? → elif → False? → else
     True? → run this block, skip everything below
```

### `if` vs `elif` vs `else`:
| Keyword | When it runs |
|---|---|
| `if` | Always checked first |
| `elif` | Only checked if all previous `if`/`elif` were False |
| `else` | Runs if nothing above was True (no condition needed) |

---

## Mini Story 4: Nested Conditionals (if inside if)

### What is Nesting?
- Putting an `if` statement **inside** another `if` statement
- Used when a second decision **depends on** the first decision

```python
device_status = input("Is the device on or off? ").lower()
temperature = int(input("Enter temperature: "))

if device_status == "on":              # Outer condition
    if temperature < 20:               # Inner condition (only checked if device is on)
        print("Temperature is low.")
    elif 20 <= temperature <= 30:      # Chained comparison!
        print("Temperature is moderate.")
    else:
        print("Temperature is high.")
else:                                  # Outer else
    print("Device is off.")
```

### `int()` conversion:
- `input()` always returns a string, so `"25"` is text, not a number
- `int(input(...))` converts it to an integer so you can do math comparisons

### Chained comparison:
- `20 <= temperature <= 30` is Python shorthand for `temperature >= 20 and temperature <= 30`
- This is a special Python feature — most other languages don't support this

### When to nest vs use `and`:
```python
# Nested approach:
if device_status == "on":
    if temperature < 20:
        print("Low temp")

# Same thing with 'and':
if device_status == "on" and temperature < 20:
    print("Low temp")
```
- Use nesting when the inner conditions are complex or have their own `elif`/`else`
- Use `and` when it's a simple combined check

---

## Mini Story 5: Ternary Operator (One-Line Conditional)

### What is a Ternary Operator?
- A way to write a simple `if-else` in **one line**
- Useful for assigning a value based on a condition

### Syntax:
```python
value_if_true if condition else value_if_false
```

### Example:
```python
order_amount = int(input("Enter total amount: "))

delivery_fee = 0 if order_amount >= 50 else 5
```

This is equivalent to:
```python
if order_amount >= 50:
    delivery_fee = 0
else:
    delivery_fee = 5
```

### When to use:
- Simple assignments with two possible values — keeps code concise
- **Don't** use it for complex logic — it becomes hard to read
- Rule of thumb: if it doesn't fit comfortably in one line, use regular `if-else`

---

## Mini Story 6: `match-case` (Structural Pattern Matching)

### What is `match-case`?
- Introduced in **Python 3.10**
- Similar to `switch-case` in other languages (C, Java, JavaScript)
- Cleaner way to check a value against **multiple specific options**

```python
seat_type = input("Enter seat type: ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper seat.")
    case "ac":
        print("AC seat.")
    case "general":
        print("General seat.")
    case "luxury":
        print("Luxury seat.")
    case _:                        # underscore = wildcard (matches anything)
        print("Invalid seat type.")
```

### Key points:
- `match` takes a value and compares it against each `case`
- `case _:` is the **wildcard/default** — runs if no other case matches (like `else`)
- Each `case` is checked top to bottom, first match wins
- No `break` needed (unlike C/Java) — Python only runs the matched case

### `match-case` vs `if-elif-else`:
| `match-case` | `if-elif-else` |
|---|---|
| Best for matching a value against **specific options** | Best for **range checks** and **complex conditions** |
| Cleaner when you have many exact matches | More flexible (supports `and`, `or`, `<`, `>`) |
| Requires Python 3.10+ | Works in all Python versions |

### When to use which:
- Checking exact values (menu options, commands, types) → `match-case`
- Checking ranges, multiple conditions, or complex logic → `if-elif-else`

---

## Summary: All Conditional Tools

| Tool | Use Case | Example |
|---|---|---|
| `if` / `else` | Simple yes/no decision | Is the kettle boiled? |
| `if` / `elif` / `else` | Multiple options to check | Small, medium, or large? |
| `or`, `and` | Combine multiple conditions | Cookies or samosa? |
| Nested `if` | Decision depends on a previous decision | Device on → then check temperature |
| Ternary | One-line assignment based on condition | Free delivery if order >= 50 |
| `match-case` | Match a value against many exact options | Sleeper, AC, general, luxury? |
