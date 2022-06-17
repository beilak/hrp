from pydantic import BaseModel, EmailStr
from typing import List

class UnitIn(BaseModel):
    unit_id: str
    description: str
    admin: str
    join_pass: str | None


class UnitOut(BaseModel):
    unit_id: str
    description: str
    admin: str


class UserIn(BaseModel):
    login: str
    first_name: str
    last_name: str
    password: str
    email: EmailStr | None


class UserOut(BaseModel):
    login: str
    first_name: str
    last_name: str
    email: EmailStr | None

