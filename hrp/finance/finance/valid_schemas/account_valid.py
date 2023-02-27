from pydantic import BaseModel


class AccIn(BaseModel):
    acc_number: str | None
    unit_id: str
    user_login: str
    acc_type: str
    description: str
    bank: str


class AccOut(BaseModel):
    acc_id: int
    acc_number: str | None
    unit_id: str
    user_login: str
    acc_type: str
    description: str
    bank: str
