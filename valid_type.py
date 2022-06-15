from pydantic import BaseModel


class Unit(BaseModel):
    unit_id: str
    name: str


class User(BaseModel):
    user_id: str
    unit_id: str
    first_name: str
    last_name: str
