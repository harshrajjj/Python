from pydantic import BaseModel, computed_field,Field

class product(BaseModel):
    price :float
    tax : float

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price + self.tax
    

class Booking(BaseModel):
    user_id: int
    product_id: int
    room_id: int
    night:int = Field(..., gt=0, description="Number of nights for the booking")
    rate_per_night: float = Field(..., gt=0, description="Rate per night for the booking")
    @computed_field
    @property
    def total_price(self) -> float:
        return self.night * self.rate_per_night




booking = Booking(user_id=1, product_id=101, room_id=202, night=3, rate_per_night=150.0)

print(booking)
print(booking.total_price)