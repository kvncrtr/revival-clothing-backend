from pydantic import BaseModel

class Drop(BaseModel):
    id: int
    name: str
    status: str
    price: float