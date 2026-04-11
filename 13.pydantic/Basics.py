from pydantic import BaseModel


class user(BaseModel):
    name: str
    age: int
    email: str

input_data = {
    "name": "John Doe",
    "age": 30,
    "email": "email.com"
}

user_instance = user(**input_data)
print(user_instance)