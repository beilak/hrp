from pydantic import BaseModel


class UnitIn(BaseModel):
    unit_id: str
    description: str
    admin: str
    join_pass: str | None


class UnitOut(BaseModel):
    unit_id: str
    description: str
    admin: str
