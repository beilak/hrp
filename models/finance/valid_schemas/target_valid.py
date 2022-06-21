from pydantic import BaseModel
from decimal import Decimal


class TrgIn(BaseModel):
    target_cnt_id: int
    user_login: str
    value: Decimal
    currency: str


class TrgOut(BaseModel):
    target_id: int
    target_cnt_id: int
    user_login: str
    value: Decimal
    currency: str
