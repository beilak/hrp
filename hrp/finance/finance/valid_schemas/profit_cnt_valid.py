from pydantic import BaseModel


class ProfitCntIn(BaseModel):
    unit_id: str
    name: str
    description: str | None
    account_id: int
    currency: str


class ProfitCntOut(BaseModel):
    profit_cnt_id: int
    unit_id: str
    name: str
    description: str | None
    account_id: int
    currency: str
