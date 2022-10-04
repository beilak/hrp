from decimal import Decimal

from pydantic import BaseModel


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
