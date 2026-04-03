# Introduction to Coding - Notes

## Python Version Check (pythonTest.py)

- `sys` is a built-in module that gives access to system-specific information
- `sys.version` returns the Python version currently running on your machine
- This is useful to confirm which Python version your code is using, especially when multiple versions are installed

```python
import sys
print(sys.version)
```

---

## Classes and Objects (non_python_shop.py)

### What is a Class?
- A **class** is a blueprint/template for creating objects
- Think of it like a recipe — the recipe itself is the class, and the chai you make from it is the object

### What is an Object?
- An **object** is an instance of a class — a real thing created from the blueprint
- You can create multiple objects from one class, each with different values

### Key Concepts

- **`__init__` method** (Constructor): This is a special method that runs automatically when you create a new object. It sets up the initial values (properties) of the object.
  - `self` refers to the current object being created — it's how the object talks about itself
  - `self.sweetness = sweetness` stores the value inside the object so it can be used later

- **Methods**: Functions defined inside a class. They describe what the object can do.
  - `sip()` and `addSugar()` are methods — actions the chai object can perform

```python
class chai:
    def __init__(self, sweetness, milkLevel):  # constructor - runs on creation
        self.sweetness = sweetness              # store sweetness in the object
        self.milkLevel = milkLevel              # store milkLevel in the object

    def sip(self):                              # method - an action
        print("Sipping the chai...")

    def addSugar(self, amount):                 # method with a parameter
        print("Adding the sugar")

myChai = chai(sweetness=3, milkLevel=2)  # creating an object (instance)
myChai.addSugar(3)                        # calling a method on the object
```

### Why use classes?
- They keep related data and behavior together (organization)
- You can create many objects with different values from the same class (reusability)
- This is the foundation of **Object-Oriented Programming (OOP)**

---

## Virtual Environment (virtualEnvironment.py)

### What is a Virtual Environment?
- A virtual environment is an **isolated Python setup** inside a specific folder
- It has its own Python version and its own installed packages
- Changes you make inside a virtual environment do NOT affect other projects

### Why do we need it?
- Project A might need `flask 2.0` and Project B might need `flask 3.0`
- Without virtual environments, installing one version would break the other
- A virtual environment keeps each project's dependencies separate

### How to create one:
```bash
python3 -m venv .venv
```
- `python3 -m venv` → tells Python to run the `venv` module
- `.venv` → name of the folder where the virtual environment will be stored (`.venv` is a common convention)

### How to use:
1. **Activate**: `source .venv/bin/activate` (Mac/Linux) or `.venv\Scripts\activate` (Windows)
2. Now any `pip install` will only install packages inside this environment
3. **Deactivate**: just type `deactivate` when done
