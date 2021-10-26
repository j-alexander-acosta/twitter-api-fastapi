# Python
from uuid import UUID
from datetime import date
from typing import Optional

# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Fiel

# FastAPI
from fastapi import FastAPI

app = FastAPI()

# Models

class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8,
    )

class User(BaseModel):
        first_name: str = Field(
        ...,
        min_lenght=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_lenght=1,
        max_length=50
    )
    birth_date: str = Optional[date] = Field(default=None)

class tweet(BaseModel):
    pass

@app.get(path="/")
def home():
    return {"Twitter API": "Working!"}