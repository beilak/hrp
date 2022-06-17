from fastapi import FastAPI, status, HTTPException
from models.org.user import UserCollection
from models.org.db_schemas.user import User
from models.org.unit import UnitCollection
from models.org.db_schemas.unit import Unit
from models.org.pydatic_schemas.schemas import UserIn, UserOut, UnitIn, UnitOut
from models.org.pydatic_schemas.UnitUser import UserUnitIn, UserUnitOut, UnitUserOut
from sqlalchemy.exc import NoResultFound

from models.model_exceptions.ModelError import ModelError
from typing import List

hrp_api = FastAPI()


@hrp_api.get("/users/", response_model=List[UserOut])
def get_users(skip: int = 0, limit: int = 100):
    users = UserCollection.get_users(offset=skip, limit=limit)
    users_out = []
    for user in users:
        users_out.append(UserOut(**user.__dict__))
    return users_out


@hrp_api.get("/users/{login}", response_model=UserOut)
async def get_user(login: str):
    user: User = UserCollection.get_user(login)
    return UserOut(**user.__dict__)


@hrp_api.post("/users/", status_code=status.HTTP_201_CREATED, response_model=UserOut)
async def create_user(user: UserIn):
    if UserCollection.is_user_exist(user.login) is True:
        raise HTTPException(status_code=409, detail="User already exist")
    created_user = UserCollection.create(user)
    return UserOut(**created_user.__dict__)


@hrp_api.put("/users/{login}", status_code=status.HTTP_200_OK, response_model=UserOut)
async def create_user(user: UserIn):
    # ToDo Update User date
    pass


@hrp_api.put("/users/{login}/join_to_unit", status_code=status.HTTP_200_OK, response_model=UserUnitOut)
async def user_join_to_unit(join: UserUnitIn):
    unit = UnitCollection.get_unit(join.unit_id)
    try:
        user = UserCollection.join_to_unit(join.login, unit)
        units = [UnitOut(**i.__dict__) for i in user.units]
    except ModelError as Error:
        raise HTTPException(status_code=409, detail=str(Error))

    return UserUnitOut(login=user.login, units=units)


@hrp_api.get("/units/", response_model=List[UnitOut])
async def get_units(skip: int = 0, limit: int = 100):
    units = UnitCollection.get_units(offset=skip, limit=limit)
    unit_out = []
    for unit in units:
        unit_out.append(UnitOut(**unit.__dict__))
    return unit_out


@hrp_api.get("/units/{unit_id}", response_model=UnitOut)
async def get_unit(unit_id: str):
    try:
        unit: Unit = UnitCollection.get_unit(unit_id)
    except NoResultFound as error:
        raise HTTPException(status_code=404, detail=str(error))
    return UnitOut(**unit.__dict__)


@hrp_api.post("/units/", status_code=status.HTTP_201_CREATED, response_model=UnitOut)
async def create_unit(unit: UnitIn):
    if UnitCollection.is_unit_exist(unit.unit_id) is True:
        raise HTTPException(status_code=409, detail="Unit already exist")
    created_unit = UnitCollection.create(unit)
    return UnitOut(**created_unit.__dict__)


@hrp_api.get("/units/{unit_id}/users", response_model=UnitUserOut)
async def get_unit_users(unit_id: str):
    try:
        unit: Unit = UnitCollection.get_unit(unit_id)
        users = [UserOut(**i.__dict__) for i in unit.users]
    except NoResultFound as error:
        raise HTTPException(status_code=404, detail=str(error))
    return UnitUserOut(unit_id=unit_id, users=users)

