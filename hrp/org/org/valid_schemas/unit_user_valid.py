from typing import List

from pydantic import BaseModel, validator

from hrp.org.org.unit import UnitFactory
from models.org.user import UserFactory
from hrp.org.org.valid_schemas.unit_valid import UnitOut
from models.org.valid_schemas.user_valid import UserOut


class UserUnitIn(BaseModel):
    login: str
    unit_id: str

    @classmethod
    @validator("login")
    def is_user_exist(cls, value):
        if UserFactory.is_user_exist(value) is False:
            raise ValueError("User didn't created yet")
        return value

    @classmethod
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
