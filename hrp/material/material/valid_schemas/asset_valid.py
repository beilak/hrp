from pydantic import BaseModel
from decimal import Decimal


class AssetIn(BaseModel):
    name: str
    unit_id: str
    user_login: str
    count: float
    measure: str
    price: Decimal
    currency: str
    city: str | None
    address: str | None


class AssetOut(BaseModel):
    asset_id: int
    name: str
    unit_id: str
    user_login: str
    count: float
    measure: str
    price: Decimal
    currency: str
    city: str | None
    address: str | None
