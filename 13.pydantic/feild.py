from pydantic import BaseModel

from typing import List , Dict, Optional

class cart(BaseModel):
    id: int
    products: List[str]
    total_price: float
    user_id: Optional[int] = None