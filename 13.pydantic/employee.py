from typing import Optional
from pydantic import BaseModel,Field

class Employee(BaseModel):
    id:int
    name: str =Field(
        ...,#required field
        min_length=2,
        max_length=50,
        description="The name of the employee"
        examples="harsh"
    )
    age: Optional[int] = Field(
        None,
        ge=18,
        le=65,
        description="The age of the employee"
    )
    email: Optional[str] = Field(
        None,
        regex=r'^[a-zA-Z0-9_.+-]+@[a-zA-ZA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
        description="The email of the employee"
    )