from pydantic import BaseModel, ValidationError
from typing import List, Optional,Union


class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str



class Company(BaseModel):
    name: str
    address:Optional[Address] = None



class Employee(BaseModel):
    name: str
    age: int
    company: Optional[Company] = None


#mixed data type

class TextContent(BaseModel):
    type: str ="text"
    content: str

class ImageContent(BaseModel):
    type: str = "image"
    url: str

class Article(BaseModel):
    title: str
    contents: List[Union[TextContent, ImageContent]]


class country(BaseModel):
    name: str
    population: int
    languages: List[str]

class state(BaseModel):
    name: str
    population: int
    capital: str

class city(BaseModel):
    name: str
    population: int
    country: country
    state: state

class Address(BaseModel):
    street: str
    city: city
    state: state
    zip_code: str

class Orgin(BaseModel):
    name: str
    address: Address
    branches: List[Address] = None

