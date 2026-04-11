from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    description: str = None



product_onr = Product(id=1, name="Laptop", price=999.99, description="A high-performance laptop")

product_two = Product(id=2, name="Smartphone", price=499.99)

print(product_onr)
print(product_two)