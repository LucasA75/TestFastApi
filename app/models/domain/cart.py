from pydantic import BaseModel
from datetime import date, datetime

class Cart(BaseModel):
    items: Item
    id: ID
    TotalValue: int
    Date: datetime
    owner: User
    