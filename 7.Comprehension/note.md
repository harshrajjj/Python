# Comprehensions in Python - Notes

## What is a Comprehension?
- A comprehension is a **short, one-line way to create a new collection** (list, dict, set) from an existing one
- It replaces the need for writing a full `for` loop + `append` pattern
- Comprehensions are more **readable** and often **faster** than regular loops

### The basic idea:
```
[what_to_keep  for item in collection  if condition]
 ^^^^^^^^^^^^  ^^^^^^^^^^^^^^^^^^^^^^^  ^^^^^^^^^^^^
 output        loop                     filter (optional)
```

---

## List Comprehension (List.py)

### Without comprehension (the old way):
```python
menu = ["Masala chai", "Ginger chai", "Lemon tea", "ice tea"]

iced_tea = []
for tea in menu:
    if "ice" in tea:
        iced_tea.append(tea)
```

### With comprehension (the clean way):
```python
iced_tea = [tea for tea in menu if "ice" in tea]
# Result: ["ice tea"]
```

### How to read it:
> "Give me `tea` **for each** `tea` **in** `menu` **if** `"ice"` is **in** `tea`"

### Breaking it down:
| Part | Meaning |
|---|---|
| `tea` (first) | What to put in the new list (the output) |
| `for tea in menu` | Loop through each item in menu |
| `if "ice" in tea` | Only include items that contain "ice" |

### Filtering by length:
```python
len_tea = [tea for tea in menu if len(tea) > 10]
```
- `len(tea)` returns the number of characters in the string
- Only keeps teas with names longer than 10 characters

### More examples:
```python
# Double every number:
doubles = [x * 2 for x in range(5)]        # [0, 2, 4, 6, 8]

# Convert to uppercase:
upper = [tea.upper() for tea in menu]       # ["MASALA CHAI", "GINGER CHAI", ...]

# With else (use ternary, move if BEFORE for):
labels = ["hot" if "ice" not in tea else "cold" for tea in menu]
```

### Important syntax rule:
- **Filter only** (if): goes **after** the for → `[x for x in list if condition]`
- **Transform with if-else**: goes **before** the for → `[x if condition else y for x in list]`

---

## Dictionary Comprehension (dictionary.py)

### What is it?
- Same idea as list comprehension but creates a **dictionary** instead
- Uses curly braces `{}` with a `key: value` pattern

### Syntax:
```python
{key: value for item in collection}
```

### Example — Convert prices from INR to USD:
```python
tea_prices_inr = {
    "masala chai": 20,
    "ginger chai": 15,
    "lemon tea": 10,
}

tea_prices_usd = {tea: price / 80 for tea, price in tea_prices_inr.items()}
```

### How to read it:
> "Create a dict where the key is `tea` and the value is `price / 80`, **for each** `tea, price` **in** the original dict's items"

### Breaking it down:
| Part | Meaning |
|---|---|
| `tea: price / 80` | The key-value pair in the new dict |
| `for tea, price in ...` | Loop through each key-value pair |
| `.items()` | Returns (key, value) tuples from the dict |

### More examples:
```python
# Swap keys and values:
flipped = {v: k for k, v in original.items()}

# Filter expensive items:
cheap = {tea: price for tea, price in prices.items() if price < 20}

# Create dict from two lists:
names = ["chai", "coffee"]
costs = [10, 15]
menu = {name: cost for name, cost in zip(names, costs)}
```

---

## Set Comprehension (set.py)

### What is it?
- Creates a **set** — automatically removes duplicates
- Uses curly braces `{}` like dict, but without the `:` key-value pattern

### Syntax:
```python
{expression for item in collection}
```

### Example — Remove duplicates from a list:
```python
favourite_chai = ["masala chai", "masala chai", "ginger chai", "lemon tea", "lemon tea"]

unique_chai = {tea for tea in favourite_chai}
# Result: {"masala chai", "ginger chai", "lemon tea"} — duplicates gone!
```

- This is essentially the same as `set(favourite_chai)` but with comprehension syntax
- Useful when you want to **filter or transform** while removing duplicates

### Nested comprehension — Flatten and deduplicate:
```python
recipe = {
    "masala chai": ["tea leaves", "milk", "sugar", "spices"],
    "ginger chai": ["ginger", "water"],
    "lemon tea": ["lemon juice", "water"],
}

unique_ingredients = {spice for ingredients in recipe.values() for spice in ingredients}
```

### How to read nested comprehension:
> "Give me each `spice`, **for each** `ingredients` list **in** recipe values, **for each** `spice` **in** that `ingredients` list"

### Reading order — nested comprehension is read left to right like nested loops:
```python
# The comprehension:
{spice for ingredients in recipe.values() for spice in ingredients}

# Is equivalent to:
result = set()
for ingredients in recipe.values():       # outer loop (first for)
    for spice in ingredients:             # inner loop (second for)
        result.add(spice)
```

- The **first `for`** is the outer loop
- The **second `for`** is the inner loop
- This flattens all ingredient lists into one set of unique ingredients

---

## Generator Expressions (generators.py)

### What is a Generator?
- A generator is like a **lazy list** — it produces values **one at a time** instead of storing everything in memory at once
- Uses parentheses `()` instead of square brackets `[]`
- Once a value is produced and consumed, it's **gone** — you can't go back

### Why use generators?
- **Memory efficient** — doesn't store all values at once
- If you have 1 million items, a list stores all 1 million in memory; a generator stores only 1 at a time
- Perfect when you only need to **iterate once** or pass into a function like `sum()`

### Syntax:
```python
# List comprehension — creates entire list in memory:
squares_list = [x**2 for x in range(10)]     # [0, 1, 4, 9, 16, ...]

# Generator expression — creates values on demand:
squares_gen = (x**2 for x in range(10))       # <generator object>
```

### Using generators:
```python
squares = (x**2 for x in range(10))

print(squares)           # <generator object> — NOT the values
print(list(squares))     # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] — converted to list
```

### With `sum()`:
```python
total = sum(x for x in range(11))   # 55 — no extra brackets needed inside sum()
```
- When passing a generator to a function, you can **drop the outer parentheses**
- `sum(x for x in range(11))` is cleaner than `sum((x for x in range(11)))`

### Generator vs List Comprehension:

| List Comprehension `[]` | Generator Expression `()` |
|---|---|
| Creates the full list in memory | Creates values one at a time |
| Can access items by index `[0]` | Cannot index — only iterate forward |
| Can iterate multiple times | **Exhausted after one pass** — can't reuse |
| Uses more memory | Uses almost no memory |
| Faster for small data | Better for large data |

### When to use which:
- **Need to access items multiple times or by index?** → List comprehension
- **Just iterating once or passing to `sum()`/`max()`/`min()`?** → Generator
- **Working with huge data (millions of items)?** → Generator (saves memory)

### Important — generators are exhausted after one use:
```python
squares = (x**2 for x in range(5))

print(list(squares))   # [0, 1, 4, 9, 16] — works!
print(list(squares))   # [] — empty! Generator is exhausted
```

---

## Summary: All Comprehension Types

| Type | Syntax | Result |
|---|---|---|
| List | `[x for x in items]` | `[1, 2, 3]` |
| Dict | `{k: v for k, v in items}` | `{"a": 1, "b": 2}` |
| Set | `{x for x in items}` | `{1, 2, 3}` (unique) |
| Generator | `(x for x in items)` | Generator object (lazy) |

### Pattern to remember:
```
[expression for item in iterable if condition]   → List
{key: val  for item in iterable if condition}    → Dict
{expression for item in iterable if condition}   → Set
(expression for item in iterable if condition)   → Generator
```

The only difference is the **brackets** — everything inside works the same way!
