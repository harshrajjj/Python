# Pydantic in Python - Notes

---

## What is Pydantic?
- A **data validation** library for Python — makes sure your data is the right type and format
- You define a **model** (a class) with type hints, and Pydantic automatically validates incoming data
- If the data is wrong, it throws a clear error instead of silently breaking later
- Install with: `pip install pydantic`

### Why use Pydantic?
- **No manual validation** — no more writing `if isinstance(x, int)` everywhere
- **Auto type conversion** — pass `"30"` for an `int` field, Pydantic converts it automatically
- **Clear error messages** — tells you exactly which field failed and why
- Used heavily in **FastAPI**, **LangChain**, and modern Python APIs

---

## Basics.py — First Pydantic Model

### Creating a model:
```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str
```

- Inherit from `BaseModel` — this makes it a Pydantic model
- Each field has a **name** and a **type hint** — Pydantic uses these to validate

### Using the model:
```python
input_data = {"name": "John Doe", "age": 30, "email": "email.com"}

user = User(**input_data)     # ** unpacks the dict as keyword arguments
print(user)                   # name='John Doe' age=30 email='email.com'
```

### What happens behind the scenes:
1. Pydantic checks: is `name` a string? is `age` an int? is `email` a string?
2. If types don't match, it tries to **convert** them (e.g., `"30"` → `30`)
3. If conversion fails, it raises a `ValidationError`

### Pydantic model vs regular class:
| Regular class | Pydantic BaseModel |
|---|---|
| No automatic validation | Validates types on creation |
| Need manual `__init__` | Auto-generates `__init__` from fields |
| `print()` shows memory address | `print()` shows all field values |
| No type coercion | Auto-converts compatible types |

---

## prodect_model.py — Default Values and Optional Fields

```python
class Product(BaseModel):
    id: int
    name: str
    price: float
    description: str = None      # optional — defaults to None

product_one = Product(id=1, name="Laptop", price=999.99, description="A high-performance laptop")
product_two = Product(id=2, name="Smartphone", price=499.99)  # description is optional
```

### Key points:
- Fields **without** a default are **required** — must be provided
- Fields **with** a default (`= None`, `= "default"`) are **optional**
- `= None` means the field can be skipped entirely

---

## feild.py — `Field()` for Advanced Constraints

### What is `Field()`?
- Gives you **extra control** over each field — constraints, descriptions, examples
- Import from `pydantic`: `from pydantic import Field`

```python
from typing import Optional, List, Dict
from pydantic import BaseModel, Field

class cart(BaseModel):
    id: int
    products: List[str]
    total_price: float
    user_id: Optional[int] = None
```

### `typing` module types:
| Type | What it means | Example |
|---|---|---|
| `str`, `int`, `float` | Basic types | `name: str` |
| `Optional[int]` | Can be `int` or `None` | `age: Optional[int] = None` |
| `List[str]` | List of strings | `products: List[str]` |
| `Dict[str, int]` | Dict with str keys, int values | `prices: Dict[str, int]` |
| `Union[str, int]` | Can be either str or int | `value: Union[str, int]` |

---

## employee.py — `Field()` with Validation Constraints

```python
from pydantic import BaseModel, Field
from typing import Optional

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,                          # ... means REQUIRED (no default)
        min_length=2,                 # at least 2 characters
        max_length=50,                # at most 50 characters
        description="The name of the employee"
    )
    age: Optional[int] = Field(
        None,                         # default is None (optional)
        ge=18,                        # greater than or equal to 18
        le=65,                        # less than or equal to 65
    )
    email: Optional[str] = Field(
        None,
        pattern=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',  # regex pattern
    )
```

### `Field()` constraints:

| Constraint | What it does | For |
|---|---|---|
| `...` (Ellipsis) | Field is **required** | All types |
| `None` | Field is **optional**, defaults to None | All types |
| `min_length` / `max_length` | Min/max string length | `str` |
| `ge` (greater or equal) | Minimum value | `int`, `float` |
| `le` (less or equal) | Maximum value | `int`, `float` |
| `gt` / `lt` | Strictly greater/less than | `int`, `float` |
| `pattern` | Must match regex pattern | `str` |
| `description` | Documentation for the field | All types |

---

## field_validation.py — `@field_validator` (Custom Validation)

### What is `@field_validator`?
- A decorator that lets you write **custom validation logic** for a specific field
- Runs after Pydantic's built-in type checking

```python
from pydantic import BaseModel, field_validator

class User(BaseModel):
    username: str

    @field_validator('username')
    def validate_username(cls, value):
        if len(value) < 5:
            raise ValueError('Username must be at least 5 characters long')
        return value         # MUST return the value (or a modified version)
```

### How it works:
1. Pydantic checks: is `username` a string? (built-in check)
2. Then runs `validate_username` with the value
3. If it raises `ValueError` → validation fails
4. If it returns a value → that becomes the field's value

### Validating multiple fields with one validator:
```python
class Person(BaseModel):
    first_name: str
    last_name: str

    @field_validator("first_name", "last_name")     # applies to BOTH fields
    def name_must_be_capitalized(cls, value):
        if not value.istitle():
            raise ValueError("Name must be capitalized")
        return value
```

### Transforming data in a validator:
```python
class Product(BaseModel):
    price: str    # "$4.44"

    @field_validator("price")
    def parse_price(cls, value):
        if value.startswith("$"):
            return float(value[1:])        # "$4.44" → 4.44 (transforms the value!)
        raise ValueError("Price must start with $")
```

- Validators can **transform** data — return a different value than what was passed in
- This is useful for parsing, normalizing, or cleaning input

---

## field_validation.py — `@model_validator` (Cross-Field Validation)

### What is `@model_validator`?
- Validates **relationships between multiple fields** — not just one field in isolation
- Runs after all individual field validators

```python
from pydantic import BaseModel, model_validator

class Signup(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')     # runs AFTER all fields are validated
    def check_passwords_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError('Passwords do not match')
        return values
```

### `mode='after'` vs `mode='before'`:
| `mode='after'` | `mode='before'` |
|---|---|
| Runs after all fields are validated | Runs before field validation |
| Receives the model instance | Receives raw input data (dict) |
| Fields are already typed and validated | Fields might be wrong type |
| Most common — use this by default | Use for preprocessing raw data |

---

## Nested_model.py — Nested Models (Model Inside Model)

### What is Nesting?
- A Pydantic model can have a **field that is another model**
- This represents complex, structured data — like a user with an address

```python
class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    addresses: Address             # a whole Address model as a field!
```

### Creating nested models:

**Method 1 — Pass an Address object:**
```python
address = Address(street="123 Main St", city="Anytown", state="CA", zip_code="12345")
user = User(id=1, name="John Doe", addresses=address)
```

**Method 2 — Pass a dictionary (Pydantic auto-converts):**
```python
user_data = {
    "id": 2,
    "name": "Jane Doe",
    "addresses": {                 # Pydantic converts this dict to an Address object!
        "street": "456 Elm St",
        "city": "Othertown",
        "state": "NY",
        "zip_code": "54321"
    }
}
user = User(**user_data)
```

### Accessing nested data:
```python
print(user.addresses.city)         # "Othertown" — dot notation through nested models
```

---

## Advanced_Nested_Model.py — Complex Nesting and Union Types

### Multiple levels of nesting:
```python
class Address(BaseModel):
    street: str
    city: str

class Company(BaseModel):
    name: str
    address: Optional[Address] = None     # optional nested model

class Employee(BaseModel):
    name: str
    age: int
    company: Optional[Company] = None     # optional nested model
```

- Models can be nested as deeply as needed
- Use `Optional` for nested models that might not always be present

### `Union` — Mixed types in a list:
```python
from typing import Union, List

class TextContent(BaseModel):
    type: str = "text"
    content: str

class ImageContent(BaseModel):
    type: str = "image"
    url: str

class Article(BaseModel):
    title: str
    contents: List[Union[TextContent, ImageContent]]    # list can contain either type!
```

- `Union[TextContent, ImageContent]` means each item can be **either** a text or image
- Pydantic figures out which model to use based on the data
- Common pattern for APIs with mixed content types (like a blog with text and images)

### Deeply nested real-world example:
```python
class Country(BaseModel):
    name: str
    population: int
    languages: List[str]

class State(BaseModel):
    name: str
    population: int
    capital: str

class City(BaseModel):
    name: str
    population: int
    country: Country               # nested
    state: State                   # nested

class Address(BaseModel):
    street: str
    city: City                     # nested (which itself has nested models!)
    zip_code: str
```

- Each level validates its own fields — errors bubble up clearly
- Pydantic tells you exactly where the validation failed (e.g., `addresses.city.country.name`)

---

## recursive_nested.py — Recursive Models (Self-Referencing)

### What is a Recursive Model?
- A model that **contains itself** as a field — like a comment with replies that are also comments

```python
from typing import List, Optional

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None    # a Comment can contain Comments!

Comment.model_rebuild()     # required — resolves the forward reference
```

### Why `'Comment'` in quotes?
- When Python reads `List['Comment']`, the `Comment` class isn't fully defined yet
- The quotes make it a **forward reference** — a string that gets resolved later
- `Comment.model_rebuild()` tells Pydantic to resolve these references after the class is complete

### Using recursive models:
```python
class Post(BaseModel):
    id: int
    title: str
    comments: List[Comment]

post = Post(
    id=1,
    title="My First Post",
    content="Hello!",
    comments=[
        Comment(id=1, content="Great post!"),
        Comment(
            id=2,
            content="Thanks!",
            replies=[
                Comment(id=3, content="I agree!"),     # nested replies
                Comment(id=4, content="Me too!")
            ]
        )
    ]
)

print(post.comments[1].replies[0].content)   # "I agree!"
```

### Use cases:
- Comment threads (replies to replies)
- File systems (folders containing folders)
- Org charts (manager → employees → their employees)
- Tree data structures

---

## computed_property.py — `@computed_field` (Auto-Calculated Fields)

### What is a Computed Field?
- A field whose value is **automatically calculated** from other fields
- Not stored — recalculated every time you access it
- Uses `@computed_field` + `@property`

```python
from pydantic import BaseModel, computed_field, Field

class Product(BaseModel):
    price: float
    tax: float

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price + self.tax
```

### Practical example:
```python
class Booking(BaseModel):
    user_id: int
    product_id: int
    room_id: int
    night: int = Field(..., gt=0)
    rate_per_night: float = Field(..., gt=0)

    @computed_field
    @property
    def total_price(self) -> float:
        return self.night * self.rate_per_night

booking = Booking(user_id=1, product_id=101, room_id=202, night=3, rate_per_night=150.0)
print(booking.total_price)   # 450.0 — automatically calculated!
print(booking)               # total_price is included in the output
```

### Key points:
- **No need to pass `total_price`** when creating the model — it's calculated
- **Included in serialization** — shows up in `model_dump()`, JSON output, and `print()`
- **Always up to date** — if the source fields change, the computed field reflects it
- Must have a **return type hint** (`-> float`)
- Uses both `@computed_field` AND `@property` decorators together

### `@computed_field` vs regular `@property`:
| `@property` alone | `@computed_field` + `@property` |
|---|---|
| Works but NOT included in serialization | Included in `model_dump()`, JSON, `print()` |
| Hidden from API responses | Visible in API responses |
| Just a Python property | A proper Pydantic field |

---

## advance_validator.py — More Validator Patterns

### Validate email format:
```python
class User(BaseModel):
    email: str

    @field_validator("email")
    def validate_email(cls, value):
        if "@" not in value:
            raise ValueError("Invalid email address")
        return value
```

### Validate capitalization:
```python
class Person(BaseModel):
    first_name: str
    last_name: str

    @field_validator("first_name", "last_name")
    def name_must_be_capitalized(cls, value):
        if not value.istitle():          # "John" → True, "john" → False
            raise ValueError("Name must be capitalized")
        return value
```

### Transform and validate (parse price string):
```python
class Product(BaseModel):
    price: str    # accepts "$4.44"

    @field_validator("price")
    def parse_price(cls, value):
        if value.startswith("$"):
            return float(value[1:])      # "$4.44" → 4.44
        raise ValueError("Price must start with $")
```

- The field type is `str`, but the validator **returns a `float`**
- The stored value will be the float — validators can change the type!

---

## Summary: All Pydantic Concepts

| Concept | What it does |
|---|---|
| `BaseModel` | Base class for all Pydantic models |
| Type hints (`str`, `int`) | Define and validate field types |
| `Optional[type]` | Field can be the type or `None` |
| `List[type]`, `Dict[k, v]` | Typed collections |
| `Union[A, B]` | Field can be type A or type B |
| `Field(...)` | Required field with constraints |
| `Field(None)` | Optional field with constraints |
| `min_length` / `max_length` | String length limits |
| `ge` / `le` / `gt` / `lt` | Number range limits |
| `pattern` | Regex validation for strings |
| `@field_validator` | Custom validation for one field |
| `@model_validator` | Cross-field validation |
| Nested models | Model as a field of another model |
| `'ModelName'` + `model_rebuild()` | Recursive/self-referencing models |
| `@computed_field` + `@property` | Auto-calculated fields |
| `**data` | Unpack dict into model constructor |
| `model_dump()` | Convert model to dictionary |
