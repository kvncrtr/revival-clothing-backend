from pydantic import BaseModel
from enum import Enum
from datetime import datetime

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy import (
    Column, 
    Integer, 
    String, 
    DateTime, 
    text, 
    Enum as SQLEnum
)

from app.database import Base

class StatusType(str, Enum):
    coming = "coming"
    available = "available"
    sold_out = "sold_out"
    archived = "archived"
    discontinued = "discontinued"
    vintage = "vintage"

# SQLAlchemy Models

class Drop(Base):
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
        server_default=func.now(),
        onupdate=func.now()
    )

    owner = Column(String, nullable=True)

    collection_type = Column(
        String,
        nullable=True,
        server_default=text("'streetwear'")
    )

    inventory_count = Column(Integer, nullable=False)

    # This means a drop can have many waitinglist signups
    waitlist_signups = relationship("WaitlistSignup", back_populates="drop")

# Pydantic Response/Request Schemas

class DropCreate(BaseModel):
    name: str
    status: StatusType = StatusType.coming
    price_cents: float
    inventory_count: int

class DropOut(BaseModel):
    id: int
    name: str
    status: StatusType
    price: float
    inventory_count: int
    created_at: datetime | None = None
    team: str | None = None
    collection_type: str | None = None

    model_config = {
        "from_attributes": True
    }

class DropCreateResponse(BaseModel):
    message: str
    drop: DropOut