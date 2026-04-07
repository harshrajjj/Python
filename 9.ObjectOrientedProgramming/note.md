# Object Oriented Programming (OOP) in Python - Notes

---

## What is OOP?
- A way of organizing code around **objects** — things that bundle **data** (attributes) and **behavior** (methods) together
- Instead of writing loose functions and variables, you group related things into classes
- Real world analogy: a "Car" class has data (color, speed) and behavior (drive, brake)

---

## class.py — Creating a Class and Object

### What is a Class?
- A **blueprint/template** for creating objects
- Defines what attributes and methods the objects will have
- By itself, a class does nothing — you need to create objects from it

### What is an Object?
- An **instance** of a class — a real thing created from the blueprint
- Each object is independent — changing one doesn't affect others

```python
class chai:
    pass            # empty class — valid but does nothing

print(type(chai))   # <class 'type'> — chai itself is a type
ginger = chai()     # create an object (instance) of the class
print(type(ginger)) # <class '__main__.chai'> — ginger is a chai object
print(ginger)       # <__main__.chai object at 0x...> — memory address
```

### Key points:
- `class ClassName:` defines a class (convention: PascalCase for class names)
- `ClassName()` creates a new object — the parentheses call the constructor
- `type()` tells you what class an object belongs to
- `pass` is a placeholder when the class body is empty

---

## initObject.py — `__init__` and `__str__`

### `__init__` — The Constructor:
- A special method that runs **automatically** when you create an object
- Used to set up the object's initial data (attributes)
- `self` is the object being created — you attach data to it with `self.attribute = value`

```python
class chaiOrder:
    def __init__(self, flavor):
        self.flavor = flavor       # store flavor inside the object

    def summary(self):
        print(f"Your order is {self.flavor} chai.")

order1 = chaiOrder("ginger")      # __init__ runs, self.flavor = "ginger"
order1.summary()                   # "Your order is ginger chai."
```

### `__str__` — Human-readable string representation:
- Defines what `print(object)` shows
- Without it, printing an object shows an ugly memory address

```python
class chaiOrder:
    def __str__(self):
        return f"This is a {self.flavor} chai"

order = chaiOrder("matcha")
print(order)   # "This is a matcha chai" (instead of <object at 0x...>)
```

### Double underscore methods (`__dunder__`):
- Methods wrapped in `__double_underscores__` are called **dunder methods** or **magic methods**
- Python calls them automatically in specific situations:
  - `__init__` → when creating an object
  - `__str__` → when printing or converting to string
  - `__len__` → when calling `len(object)`
  - `__eq__` → when comparing with `==`

---

## selfArgs.py — Understanding `self`

### What is `self`?
- `self` refers to the **current object** — the specific instance calling the method
- It's how the object accesses its own data and methods
- It's always the **first parameter** in any method, but you don't pass it when calling

```python
class chaiCup:
    size = 150                     # class attribute (shared by all cups)

    def describe(self):            # self = the specific cup calling this
        print(f"This is a {self.size} ml cup.")

my_cup = chaiCup()
my_cup.describe()                  # Python automatically passes my_cup as self
```

### Behind the scenes:
```python
my_cup.describe()
# Python translates this to:
chaiCup.describe(my_cup)           # my_cup is passed as self
```

- `self` is not a keyword — it's a convention. You could name it anything, but **always use `self`**

---

## namespace.py — Class Attributes vs Instance Attributes

### Class attribute:
- Defined directly inside the class (outside any method)
- **Shared** by all objects of that class
- Accessed via `ClassName.attribute` or `object.attribute`

### Instance attribute:
- Created on a specific object using `object.attribute = value`
- **Belongs only** to that one object

```python
class chai:
    origin = "india"           # class attribute — shared by all

masala = chai()
print(masala.origin)           # "india" — reads from class (no instance attr yet)

masala.flavour = "spicy"       # instance attribute — only masala has this
print(masala.flavour)          # "spicy"
# print(chai.flavour)          # ERROR — class doesn't have this attribute
```

### Dynamic attributes:
- You can add attributes to a class **after** defining it:
```python
chai.isHot = True              # adds attribute to the class itself
print(masala.isHot)            # True — all instances can access class attributes
```

### How Python looks up attributes:
1. First checks the **instance** for the attribute
2. If not found, checks the **class**
3. If not found there, checks **parent classes**
4. If still not found → `AttributeError`

---

## attributeShadowing.py — Instance Overriding Class Attributes

### What is Attribute Shadowing?
- When an instance has an attribute with the **same name** as a class attribute
- The instance attribute **shadows** (hides) the class attribute for that specific object
- Other objects and the class itself are unaffected

```python
class chai:
    temp = "hot"               # class attribute

cutting_chai = chai()
print(cutting_chai.temp)       # "hot" — reads from class (no instance attr)

cutting_chai.temp = "cold"     # creates an INSTANCE attribute that shadows the class one
print(cutting_chai.temp)       # "cold" — reads from instance
print(chai.temp)               # "hot" — class attribute is unchanged!

del cutting_chai.temp          # deletes the instance attribute
print(cutting_chai.temp)       # "hot" — falls back to class attribute again
```

### The mental model:
- Think of it like wearing sunglasses over your regular glasses
- `cutting_chai.temp = "cold"` puts on sunglasses (instance attr hides class attr)
- `del cutting_chai.temp` takes off sunglasses (class attr is visible again)
- The regular glasses (class attr) were never changed

---

## classMethods.py — `@classmethod` (Alternative Constructors)

### What is a Class Method?
- A method that belongs to the **class**, not to a specific object
- Receives `cls` (the class itself) as the first argument, instead of `self`
- Decorated with `@classmethod`

### Why use class methods?
- **Alternative constructors** — different ways to create an object from different data formats

```python
class chaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_data):          # create from a dictionary
        return cls(order_data['tea_type'], order_data['sweetness'], order_data['size'])

    @classmethod
    def from_string(cls, order_data):        # create from a string like "black-high-small"
        tea_type, sweetness, size = order_data.split('-')
        return cls(tea_type, sweetness, size)
```

### Usage:
```python
# Normal way:
order = chaiOrder('green', 'medium', 'large')

# From a dictionary:
order1 = chaiOrder.from_dict({'tea_type': 'green', 'sweetness': 'medium', 'size': 'large'})

# From a string:
order2 = chaiOrder.from_string('black-high-small')
```

### `cls` vs `self`:
| `self` | `cls` |
|---|---|
| Refers to a specific **object** | Refers to the **class** itself |
| Used in regular methods | Used in `@classmethod` |
| `self.attribute` accesses instance data | `cls(...)` creates a new object |

### `__dict__`:
- Every object has a `__dict__` attribute — a dictionary of all its instance attributes
- `print(order1.__dict__)` → `{'tea_type': 'green', 'sweetness': 'medium', 'size': 'large'}`

---

## StaticMethods.py — `@staticmethod` (Utility Functions)

### What is a Static Method?
- A method that belongs to the class but **doesn't access** `self` or `cls`
- It's basically a regular function that lives inside a class for **organizational** purposes
- Decorated with `@staticmethod`

```python
class chaiUtils:
    @staticmethod
    def clean_ingredients(ingredients):
        return [ingredient.strip() for ingredient in ingredients]

raw = "water , milk , ginger , honey"
cleaned = chaiUtils.clean_ingredients(raw)   # ["water", "milk", "ginger", "honey"]
```

### When to use which:

| Type | Decorator | First arg | Access to | Use for |
|---|---|---|---|---|
| Regular method | (none) | `self` | Instance + class | Most methods — work with object data |
| Class method | `@classmethod` | `cls` | Class only | Alternative constructors, factory methods |
| Static method | `@staticmethod` | (none) | Nothing | Utility/helper functions related to the class |

---

## PropertyDecorator.py — `@property` (Getter/Setter)

### The Problem:
- Sometimes you want to **control** how an attribute is accessed or set
- Example: age should never be negative, temperature should auto-convert units

### `@property` — Make a method behave like an attribute:
```python
class tealeaf:
    def __init__(self, age):
        self._age = age            # convention: _prefix means "internal, don't touch directly"

    @property
    def age(self):                 # GETTER — runs when you READ leaf.age
        return self._age + 2

    @age.setter
    def age(self, value):          # SETTER — runs when you WRITE leaf.age = value
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
```

### Usage — looks like a normal attribute:
```python
leaf = tealeaf(5)
print(leaf.age)       # 7 — calls the getter (5 + 2)

leaf.age = 10         # calls the setter (validates, then sets _age = 10)
print(leaf.age)       # 12 — calls the getter (10 + 2)

leaf.age = -3         # ValueError: Age cannot be negative
```

### Key points:
- `@property` makes `leaf.age` call the **getter method** automatically — no parentheses needed
- `@age.setter` makes `leaf.age = value` call the **setter method** automatically
- The actual data is stored in `self._age` (with underscore — private by convention)
- Without a setter, the property is **read-only** — trying to set it raises `AttributeError`

### Why use `@property` instead of direct access?
- **Validation**: prevent invalid values (negative age, wrong type)
- **Computed values**: return calculated results that look like simple attributes
- **Backward compatibility**: change internal logic without breaking external code

---

## baseClass.py — Inheritance and `super()`

### What is Inheritance?
- A class can **inherit** attributes and methods from another class
- The child class gets everything from the parent, and can add or override things
- `class Child(Parent):` — the child inherits from the parent

```python
class chai:
    def __init__(self, type_, strength):
        self.type_ = type_
        self.strength = strength

class gingerChai(chai):
    def __init__(self, type_, strength, ginger_amount):
        super().__init__(type_, strength)     # call parent's __init__
        self.ginger_amount = ginger_amount    # add new attribute
```

### What is `super()`?
- `super()` gives you access to the **parent class's methods**
- `super().__init__(...)` calls the parent's constructor — sets up inherited attributes
- Without `super()`, the parent's `__init__` doesn't run, and inherited attributes won't be set

### Three ways to call parent's `__init__` (evolution):

```python
# 1. Copy-paste (BAD — duplicates code):
self.type_ = type_
self.strength = strength

# 2. Direct parent call (works but brittle):
chai.__init__(self, type_, strength)

# 3. super() (BEST — clean and supports multiple inheritance):
super().__init__(type_, strength)
```

---

## InheritanceComposition.py — Inheritance vs Composition

### Inheritance ("is-a" relationship):
```python
class baseChai:
    def __init__(self, flavor):
        self.flavor = flavor
    def describe(self):
        print(f"This is a {self.flavor} chai.")

class chaiOrder(baseChai):              # chaiOrder IS A baseChai
    def __init__(self, flavor):
        super().__init__(flavor)
    def order_summary(self):
        print(f"Your order: {self.flavor} chai.")
```

### Composition ("has-a" relationship):
```python
class chaiShop:
    chai_cls = baseChai                 # shop HAS A chai class

    def __init__(self):
        self.chai = self.chai_cls("masala")  # creates a chai object inside

    def serve(self):
        self.chai.describe()

class fancyChaiShop(chaiShop):
    chai_cls = chaiOrder                # override which chai class to use

shop = fancyChaiShop()
shop.serve()                            # uses chaiOrder instead of baseChai
```

### Inheritance vs Composition:
| Inheritance ("is-a") | Composition ("has-a") |
|---|---|
| `class Dog(Animal)` — Dog IS an Animal | `class Car` has an `Engine` object inside |
| Child gets all parent's methods | Object uses another object's methods |
| Tight coupling — child depends on parent | Loose coupling — easier to swap parts |
| Use for "same type" relationships | Use for "contains" relationships |

### When to use which:
- **Inheritance**: when the child truly is a specialized version of the parent
- **Composition**: when an object uses/contains another object (generally preferred — more flexible)

---

## Mro.py — Method Resolution Order (MRO)

### What is MRO?
- When a class inherits from **multiple parents**, Python needs to decide which parent's method to use
- **MRO** is the order in which Python searches for methods/attributes
- Uses the **C3 linearization** algorithm

```python
class A:
    label = 'A : base class'

class B(A):
    label = 'B : derived class'

class C(A):
    label = 'C : derived class'

class D(B, C):                   # inherits from BOTH B and C
    pass

cup = D()
print(cup.label)                 # "B : derived class"
print(D.__mro__)                 # (D, B, C, A, object)
```

### How MRO works for `D(B, C)`:
```
D → B → C → A → object
```

1. Look in `D` — no `label` found
2. Look in `B` — found! `"B : derived class"` — stop here
3. (Would check C, then A, then object if not found)

### Reading MRO:
- `D.__mro__` returns the full search order as a tuple
- Left-to-right in the inheritance list matters: `class D(B, C)` checks B before C

### The Diamond Problem:
```
        A
       / \
      B   C
       \ /
        D
```
- Both B and C inherit from A, and D inherits from both
- Without MRO, `A`'s methods could be called multiple times
- Python's MRO ensures each class appears **only once** in the resolution order

---

## Summary: All OOP Concepts

| Concept | What it does |
|---|---|
| `class` | Define a blueprint for objects |
| `object = Class()` | Create an instance from a class |
| `__init__` | Constructor — set up initial data when object is created |
| `self` | Reference to the current object inside methods |
| `__str__` | Define what `print(object)` shows |
| Class attribute | Shared by all objects of the class |
| Instance attribute | Belongs to one specific object |
| Attribute shadowing | Instance attr hides class attr with same name |
| `@classmethod` | Alternative constructors (receives `cls`) |
| `@staticmethod` | Utility function inside a class (no `self` or `cls`) |
| `@property` | Make a method act like an attribute (getter/setter) |
| Inheritance | Child class gets parent's attributes and methods |
| `super()` | Call parent class's methods |
| Composition | Object contains/uses other objects |
| MRO | Order Python searches for methods in multiple inheritance |
