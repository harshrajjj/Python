# Data Types - Notes

## Chapter 1: Variables, Memory, and Immutability

### What is a Variable?
- A variable is a **name that points to a value** stored in memory
- In Python, variables don't store the value directly — they store a **reference** (like an address) to where the value lives in memory

### What is `id()`?
- `id()` returns the **memory address** of an object
- Every object in Python has a unique id while it exists

### What is Immutability?
- **Immutable** means "cannot be changed after creation"
- **Integers, strings, tuples** are immutable in Python
- When you "change" an integer variable, Python doesn't modify the old value — it creates a **new object** in memory and points the variable to it

```python
sugarAmount = 2      # sugarAmount points to object 2 at some memory address
sugarAmount = 12     # sugarAmount now points to object 12 at a DIFFERENT address
                     # the object 2 still exists in memory, just nobody is pointing to it
```

- `id(2)` and `id(12)` will give different addresses — proving they are separate objects
- This is important because it means integers are safe — no one can accidentally change the value `2` to something else

---

## Chapter 2: Sets and Mutability

### What is Mutability?
- **Mutable** means "can be changed in place"
- **Sets, lists, dictionaries** are mutable in Python
- When you modify a mutable object, the object itself changes — no new object is created

```python
spiceMix = set()
print(id(spiceMix))    # some address, e.g., 140234567

spiceMix.add("ginger")
print(id(spiceMix))    # SAME address — the object was modified in place

spiceMix.add("cumin")
print(id(spiceMix))    # still the SAME address
```

### Key Difference:
| Immutable (int, str, tuple) | Mutable (list, set, dict) |
|---|---|
| Changing value = new object in memory | Changing value = same object modified |
| `id()` changes after reassignment | `id()` stays the same after modification |

---

## Chapter 3: Arithmetic Operators

Python supports all standard math operations:

| Operator | Name | Example | Result |
|---|---|---|---|
| `+` | Addition | `14 + 2` | `16` |
| `-` | Subtraction | `14 - 2` | `12` |
| `/` | Division | `7 / 3` | `2.333...` (always returns float) |
| `//` | Floor Division | `5 // 2` | `2` (rounds down to nearest integer) |
| `%` | Modulus | `5 % 2` | `1` (remainder after division) |
| `**` | Exponentiation | `10 ** 2` | `100` (10 raised to power 2) |

### Division vs Floor Division:
- `/` gives the **exact answer** as a float: `7 / 3 = 2.333...`
- `//` **rounds down** to the nearest whole number: `5 // 2 = 2`

### Modulus (`%`):
- Returns the **remainder** after division
- `5 % 2 = 1` because 5 divided by 2 is 2 with remainder 1
- Useful for checking if a number is even/odd: `n % 2 == 0` means even

### Large Numbers:
- Python allows underscores in numbers for readability: `1_000_000_000` is the same as `1000000000`

---

## Chapter 4: Booleans and Logical Operators

### What is a Boolean?
- A boolean has only two possible values: `True` or `False`
- Used for making decisions in code (conditions, if-statements)

### Booleans are secretly numbers:
- `True` equals `1` and `False` equals `0`
- You can do math with them — this is called **upcasting**

```python
stri_count = 5
is_boiling = True
total = stri_count + is_boiling  # 5 + 1 = 6 (True becomes 1)
```

### `bool()` Conversion — Truthy and Falsy:
- `bool(0)` → `False` (zero is falsy)
- `bool(1)` → `True` (any non-zero number is truthy)
- `bool("")` → `False` (empty string is falsy)
- `bool("hello")` → `True` (non-empty string is truthy)
- `bool([])` → `False` (empty list is falsy)
- `bool(None)` → `False`

### Logical Operators:

| Operator | Meaning | Example |
|---|---|---|
| `and` | Both must be True | `True and True` → `True` |
| `or` | At least one must be True | `True or False` → `True` |
| `not` | Flips the value | `not True` → `False` |

```python
water_hot = True
tea_added = True
tea_ready = water_hot and tea_added  # True — both conditions met
```

---

## Chapter 5: Floating Point Numbers

### What is a Float?
- A float is a number with a **decimal point**: `95.5`, `3.14`, `0.001`
- Stored in memory using the **IEEE 754** standard (binary representation)

### The Precision Problem:
- Computers store decimals in binary, so some decimal numbers **cannot be represented exactly**
- This leads to tiny rounding errors:

```python
idealTemp = 95.5
currentTemp = 95.49
print(idealTemp - currentTemp)  # Expected: 0.01, Actual: 0.009999999999990905
```

- This is NOT a Python bug — it happens in all programming languages
- `sys.float_info` shows the limits of float precision on your system

### How to fix precision issues:
- Use `Decimal` module for exact decimal arithmetic (important for money calculations)
- Use `Fraction` module for exact fraction representation
- Use `round()` function for display purposes

---

## Lists (List.py)

### What is a List?
- An **ordered, mutable** collection of items
- Can hold mixed types: `["water", 3, True, 5.5]`
- Defined with square brackets `[]`

### Important List Operations:

| Method | What it does | Example |
|---|---|---|
| `append(x)` | Add item to the end | `lst.append("sugar")` |
| `insert(i, x)` | Add item at position i | `lst.insert(2, "blacktea")` |
| `remove(x)` | Remove first occurrence of x | `lst.remove("water")` |
| `pop()` | Remove and return last item | `last = lst.pop()` |
| `extend(list2)` | Add all items from another list | `lst.extend(["a", "b"])` |
| `sort()` | Sort in place (alphabetically/numerically) | `lst.sort()` |
| `reverse()` | Reverse the list in place | `lst.reverse()` |
| `max(lst)` | Return largest item | `max([1,2,3])` → `3` |
| `min(lst)` | Return smallest item | `min([1,2,3])` → `1` |

### List Concatenation and Repetition:
```python
full = ["water", "milk"] + ["tea", "ginger"]  # combines two lists
strong = ["blacktea"] * 2                       # ["blacktea", "blacktea"]
```

### Bytearray:
- `bytearray` is a **mutable sequence of bytes** (numbers 0-255)
- Used for working with raw binary data
- `b"cumin"` creates an immutable bytes object, `bytearray(b"cumin")` makes it mutable

---

## Tuples (Tuples.py)

### What is a Tuple?
- An **ordered, immutable** collection of items
- Once created, you **cannot add, remove, or change** elements
- Defined with parentheses `()`

### Why use Tuples over Lists?
- **Safety**: data cannot be accidentally modified
- **Performance**: tuples are slightly faster than lists
- **Dictionary keys**: tuples can be used as dictionary keys, lists cannot

### Tuple Unpacking:
- You can assign each element of a tuple to a separate variable in one line:

```python
masala = ("cumin", "coriander", "cardamom")
spice1, spice2, spice3 = masala  # spice1="cumin", spice2="coriander", etc.
```

### Value Swapping:
- Python allows swapping two variables without a temporary variable:

```python
a, b = b, a  # swaps the values of a and b
```

- This works because Python evaluates the right side first (creates a tuple), then unpacks it

### Membership Testing:
```python
"cumin" in masala  # True — checks if "cumin" exists in the tuple
"ginger" in masala # False
```

---

## Dictionaries (Dictionary.py)

### What is a Dictionary?
- A collection of **key-value pairs** — like a real dictionary where each word (key) has a definition (value)
- **Unordered** (since Python 3.7, insertion order is maintained)
- **Mutable** — you can add, change, and delete entries
- **Keys must be unique** and immutable (strings, numbers, tuples)

### Creating a Dictionary:
```python
# Method 1: using dict()
chai_order = dict(type="ginger chai", size="medium", sugar_level=2)

# Method 2: using curly braces
chai_recipe = {}
chai_recipe["ginger"] = 1
chai_recipe["tea leaves"] = 2
```

### Important Dictionary Operations:

| Operation | What it does |
|---|---|
| `d["key"]` | Get value (raises KeyError if key missing) |
| `d.get("key", default)` | Get value (returns default if key missing — safer!) |
| `d["key"] = value` | Add or update a key-value pair |
| `del d["key"]` | Delete a key-value pair |
| `d.popitem()` | Remove and return the last inserted key-value pair |
| `d.update(other_dict)` | Merge another dictionary into this one |
| `"key" in d` | Check if key exists → `True`/`False` |
| `d.keys()` | Get all keys |
| `d.values()` | Get all values |
| `d.items()` | Get all key-value pairs as tuples |

### `get()` vs `[]`:
- `d["size"]` → returns value, but **crashes** if key doesn't exist
- `d.get("size", "unknown")` → returns value, or `"unknown"` if key doesn't exist (no crash)
- Always prefer `.get()` when you're not sure if the key exists

---

## Sets (sets.py)

### What is a Set?
- An **unordered collection of unique items** — no duplicates allowed
- Defined with curly braces `{}` (but empty set must be `set()`, not `{}` which creates a dict)
- **Mutable** — you can add/remove items
- Items must be **immutable** (strings, numbers, tuples — not lists)

### Set Operations (like math sets):

| Operation | Symbol | What it does |
|---|---|---|
| Union | `A \| B` | All items from both sets (combined) |
| Intersection | `A & B` | Only items that appear in BOTH sets |
| Difference | `A - B` | Items in A that are NOT in B |
| Symmetric Difference | `A ^ B` | Items in either set, but NOT in both |

```python
essential = {"salt", "pepper", "cumin", "cinnamon"}
optional = {"ginger", "cardamom", "cinnamon"}

essential | optional   # all unique spices from both
essential & optional   # {"cinnamon"} — only the common one
essential - optional   # {"salt", "pepper", "cumin"} — essential only
```

### Membership Testing:
```python
"cumin" in essential  # True
"ginger" in essential # False
```

---

## Strings (Strings.py)

### What is a String?
- A **sequence of characters** enclosed in quotes (`"hello"` or `'hello'`)
- **Immutable** — you cannot change individual characters, only create new strings

### f-strings (Formatted Strings):
- Prefix a string with `f` to embed variables directly:

```python
name = "Alice"
print(f"Hello, {name}!")  # "Hello, Alice!"
```

### Slicing:
- Extract parts of a string using `[start:end]` (end is NOT included):

```python
text = "Aromatic and bold"
text[0:10]    # "Aromatic a" — characters at index 0 through 9
text[::-1]    # "dlob dna citamorA" — reverses the entire string
```

- `[start:end:step]` — step of `-1` reverses the string

### Encoding/Decoding:
- **Encoding**: converting a string (human-readable) to bytes (computer-readable)
- **Decoding**: converting bytes back to a string
- `utf-8` is the most common encoding standard — supports all languages and emojis

```python
encoded = "Ginger Chai".encode("utf-8")   # b'Ginger Chai' (bytes)
decoded = encoded.decode("utf-8")          # "Ginger Chai" (string again)
```

---

## Advanced Data Types (Advanced_data_type.py)

### Arrow (Date/Time Library):
- `arrow` is a third-party library that makes working with dates and times easier than the built-in `datetime`
- Install with: `pip install arrow`

```python
import arrow

brewing_time = arrow.utcnow()              # current UTC time
brewing_time = brewing_time.shift(minutes=5)  # add 5 minutes
```

- `.utcnow()` → gets the current time in UTC
- `.shift()` → moves the time forward or backward by the specified amount

### Named Tuples (from `collections`):
- A **namedtuple** is like a regular tuple, but each position has a **name**
- It makes code more readable — access by name instead of index number

```python
from collections import namedtuple

ChaiProfile = namedtuple("ChaiProfile", ["name", "flavour", "strength"])
myChai = ChaiProfile(name="Masala Chai", flavour="Spicy", strength=8)

myChai.name       # "Masala Chai" — access by name (readable!)
myChai[0]         # "Masala Chai" — access by index (still works)
```

### Why use namedtuple over a regular tuple?
- `myChai.name` is much more readable than `myChai[0]`
- Still immutable like a regular tuple (safe from accidental changes)
- Lighter than a full class when you just need to store data

### Why use namedtuple over a dictionary?
- Immutable (dict is mutable)
- Uses less memory
- Supports tuple operations (unpacking, indexing)
