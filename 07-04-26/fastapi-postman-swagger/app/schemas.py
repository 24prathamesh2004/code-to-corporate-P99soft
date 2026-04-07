from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    email: EmailStr
    age: int

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: str | None = None
    age: int | None = None

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True