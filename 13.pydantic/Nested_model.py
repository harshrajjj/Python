from typing import List, Optional
from pydantic import BaseModel  

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    adresses: Address


address =Address(
    street="123 Main St",
    city="Anytown",
    state="CA",
    zip_code="12345"
)

user = User(
    id=1,
    name="John Doe",
    adresses=address
)

print(user)
print(user.adresses)


user_data = {
    "id": 2,
    "name": "Jane Doe",
    "adresses": {
        "street": "456 Elm St",
        "city": "Othertown",
        "state": "NY",
        "zip_code": "54321"
    }
}

user = User(**user_data)

print(user)
print(user.adresses)