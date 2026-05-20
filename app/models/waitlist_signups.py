from pydantic import BaseModel, EmailStr

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    UniqueConstraint,
    ForeignKey
)

from app.database.db import Base

# SQLAlchemy Models

class WaitlistSignup(Base):
    __tablename__ = "waitlist_signups"
    __table_args__ = (
        UniqueConstraint("drop_id", "email", name="uq_waitlist_drop_email"),
    )

    id = Column(Integer, primary_key=True)

    drop_id = Column(
        Integer, 
        ForeignKey("drops.id"), 
        nullable=False
    )
    
    first_name = Column(String, nullable=False)

    last_name = Column(String, nullable=False)

    email = Column(String, nullable=False)

    size = Column(String, nullable=False)

    created_at = Column(
        DateTime(timezone=True), 
        server_default=func.now(),
        nullable=True
    )
    
    # This means a signups can have many drops
    drop = relationship("Drop", back_populates="waitlist_signups")

# Pydantic Res/Req Schemas

class WaitlistCreate(BaseModel):
    drop_id: int
    first_name: str 
    last_name: str 
    email: EmailStr
    size: str

class WaitlistOut(BaseModel):
    message: str
    drop_id: int
    size: str

class WaitlistDemandOut(BaseModel):
    drop_id: int
    total_signups: int
    size_demand: dict[str, int]