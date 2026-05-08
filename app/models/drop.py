from pydantic import BaseModel
from datetime import datetime

class DropIn(BaseModel):
    name: str
    status: str
    price: float
    number_of_units: int


class Drop(DropIn):
    id: int
    created_at: datetime
    team: str

class DropOut(BaseModel):
    id: int
    name: str
    status: str
    price: float
    number_of_units: int

class DropCreateResponse(BaseModel):
    message: str
    drop: DropOut