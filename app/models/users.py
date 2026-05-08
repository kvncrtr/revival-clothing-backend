from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: str
    number: str
    online: bool

class User(BaseModel):
    username: str
    email: str
    number: str
    online: bool
    card_number: int
    created_at: datetime

class UserOut(BaseModel):
    username: str
    email: str
