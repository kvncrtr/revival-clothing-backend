from pydantic import BaseModel
from enum import Enum
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum as SQLEnum, text
from sqlalchemy.sql import func
from datetime import datetime
from app.database import Base

class StatusType(str, Enum):
    coming = "coming"
    available = "available"
    sold_out = "sold_out"
    archived = "archived"
    discontinued = "discontinued"
    vintage = "vintage"

class DropModel(Base):
    __tablename__ = "drops"

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)

    price_cents = Column(
        Integer,
        nullable=True,
        server_default=text("0")
    )

    status = Column(
        SQLEnum(StatusType, name="status_type"),
        nullable=True,
        server_default=text("'coming'")
    )

    team = Column(String, nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        nullable=True,
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        nullable=True,
        server_default=func.now()
    )

    owner = Column(String, nullable=True)

    collection_type = Column(
        String,
        nullable=True,
        server_default=text("'streetware'")
    )

    inventory_count = Column(
        Integer,
        nullable=False
    )

'''
ALTER TABLE drops
DROP COLUMN units_count;
'''



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