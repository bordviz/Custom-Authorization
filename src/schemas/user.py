from datetime import datetime
from pydantic import BaseModel, EmailStr
from .config import TunedModel

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    username: str 
    email: EmailStr
    hashed_password: str

class UserRead(TunedModel):
    id: int
    first_name: str
    last_name: str
    username: str 
    email: EmailStr
    created_at: datetime