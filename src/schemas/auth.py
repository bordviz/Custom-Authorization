from pydantic import BaseModel, EmailStr, Field

class AuthRegister(BaseModel):
    first_name: str
    last_name: str
    username: str 
    email: EmailStr
    password: str = Field(min_length=8)

class AuthLogin(BaseModel):
    email: EmailStr
    password: str
