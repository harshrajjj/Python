from pydantic import BaseModel, field_validator


class person(BaseModel):
    first_name: str
    last_name: str

    @field_validator("first_name", "last_name")
    def name_must_be_capitalized(cls, value):
        if not value.istitle():
            raise ValueError("Name must be capitalized")
        return value
    

class user(BaseModel):
    email: str

    @field_validator("email")
    def validate_email(cls, value):
        if "@" not in value:
            raise ValueError("Invalid email address")
        return value


class product(BaseModel):
    price:str#$4.44
    @field_validator("price")
    def parse_price(cls, value):
        if value.startswith("$"):
            return float(value[1:])
        raise ValueError("Price must start with $")
    

