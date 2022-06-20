from pydantic import BaseModel, validator

from models.org.unit import UnitFactory
from models.org.user import UserFactory
from models.org.pydatic_schemas.user_model import UnitOut, UserOut
from typing import List


class UserUnitIn(BaseModel):
    login: str
    unit_id: str

    @validator("login")
    def is_user_exist(cls, value):
        if UserFactory.is_user_exist(value) is False:
            raise ValueError("User didn't created yet")
        return value

    @validator("unit_id")
    def is_unit_exist(cls, value):
        if UnitFactory.is_unit_exist(value) is False:
            raise ValueError("Unit didn't created yet")
        return value


class UserUnitOut(BaseModel):
    login: str
    units: List[UnitOut]


class UnitUserOut(BaseModel):
    unit_id: str
    users: List[UserOut]
