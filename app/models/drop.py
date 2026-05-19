from pydantic import BaseModel
from enum import Enum
from sqlalchemy import Column, Integer, String, Time, ForeignKey
from datetime import datetime
from app.database import Base

class StatusType(str, Enum):
    coming = "coming"
    available = "available"
    sold_out = "sold_out"
    archived = "archived"
    discontinued = "discontinued"
    vintage = "vintage"

# class DropModel():


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