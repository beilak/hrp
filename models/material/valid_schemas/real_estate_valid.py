from pydantic import BaseModel


class RealEstateIn(BaseModel):
    name: str
    unit_id: str
    user_login: str
    city: str | None
    address: str | None
    price: str | None
    currency: str | None


class RealEstateOut(BaseModel):
    real_estate_id: int
    name: str
    unit_id: str
    user_login: str
    city: str | None
    address: str | None
    price: str | None
    currency: str | None
