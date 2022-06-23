from decimal import Decimal

from pydantic import BaseModel


class TrgCntIn(BaseModel):
    unit_id: str
    name: str
    description: str | None
    account_id: int
    value: Decimal
    currency: str
    init_value: Decimal
    init_currency: str


class TrgCntOut(BaseModel):
    target_cnt_id: int
    unit_id: str
    name: str
    description: str | None
    value: Decimal
    currency: str
    init_value: Decimal
    init_currency: str
