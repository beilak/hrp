from decimal import Decimal

from pydantic import BaseModel


class ProfitIn(BaseModel):
    profit_cnt_id: int
    user_login: str
    value: Decimal
    currency: str


class ProfitOut(BaseModel):
    profit_id: int
    profit_cnt_id: int
    user_login: str
    value: Decimal
    currency: str
