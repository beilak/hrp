from fastapi import FastAPI, status, HTTPException
from models.org.user import UserFactory
from models.org.db_schemas.db_user import User
from models.org.unit import UnitFactory
from models.org.db_schemas.db_unit import Unit
from models.org.pydatic_schemas.user_model import UserIn, UserOut, UnitIn, UnitOut
from models.org.pydatic_schemas.UnitUser import UserUnitIn, UserUnitOut, UnitUserOut
from models.finance.account import AccountService
from models.finance.valid_schemas.acc_valid import AccIn, AccOut

from sqlalchemy.exc import NoResultFound

from models.model_exceptions.ModelError import ModelError
from typing import List

hrp_api = FastAPI()


@hrp_api.get("/users/", status_code=status.HTTP_200_OK, response_model=List[UserOut])
def get_users(skip: int = 0, limit: int = 100):
    users = UserFactory.get_users(offset=skip, limit=limit)
    users_out = []
    for user in users:
        users_out.append(UserOut(**user.__dict__))
    return users_out


@hrp_api.get("/users/{login}", status_code=status.HTTP_200_OK, response_model=UserOut)
async def get_user(login: str):
    user: User = UserFactory.get_user(login)
    return UserOut(**user.__dict__)


@hrp_api.post("/users/", status_code=status.HTTP_201_CREATED, response_model=UserOut)
async def create_user(user: UserIn):
    if UserFactory.is_user_exist(user.login) is True:
        raise HTTPException(status_code=409, detail="User already exist")
    created_user = UserFactory.create(user)
    return UserOut(**created_user.__dict__)


@hrp_api.put("/users/{login}", status_code=status.HTTP_200_OK, response_model=UserOut)
async def update_user(user: UserIn):
    # ToDo Update User date
    pass


@hrp_api.post("/units/", status_code=status.HTTP_201_CREATED, response_model=UnitOut)
async def create_unit(unit: UnitIn):
    if UnitFactory.is_unit_exist(unit.unit_id) is True:
        raise HTTPException(status_code=409, detail="Unit already exist")
    try:
        created_unit = UnitFactory.create(unit)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
    return UnitOut(**created_unit.__dict__)


@hrp_api.get("/units/", status_code=status.HTTP_200_OK, response_model=List[UnitOut])
async def get_units(skip: int = 0, limit: int = 100):
    units = UnitFactory.get_units(offset=skip, limit=limit)
    unit_out = []
    for unit in units:
        unit_out.append(UnitOut(**unit.__dict__))
    return unit_out


@hrp_api.get("/units/{unit_id}", response_model=UnitOut)
async def get_unit(unit_id: str):
    try:
        unit: Unit = UnitFactory.get_unit(unit_id)
    except NoResultFound as error:
        raise HTTPException(status_code=404, detail=str(error))
    return UnitOut(**unit.__dict__)


@hrp_api.put("/users/{login}/join_to_unit", status_code=status.HTTP_200_OK,
             response_model=UserUnitOut)
async def user_join_to_unit(join: UserUnitIn):
    unit = UnitFactory.get_unit(join.unit_id)
    try:
        user = UserFactory.join_to_unit(join.login, unit)
        units = [UnitOut(**i.__dict__) for i in user.units]
    except ModelError as Error:
        raise HTTPException(status_code=409, detail=str(Error))
    return UserUnitOut(login=user.login, units=units)


@hrp_api.get("/units/{unit_id}/users", status_code=status.HTTP_200_OK,
             response_model=UnitUserOut)
async def get_unit_users(unit_id: str):
    try:
        unit: Unit = UnitFactory.get_unit(unit_id)
        users = [UserOut(**i.__dict__) for i in unit.users]
    except NoResultFound as error:
        raise HTTPException(status_code=404, detail=str(error))
    return UnitUserOut(unit_id=unit_id, users=users)


""" Account endpoint """


@hrp_api.post("/units/{unit_id}/account", status_code=status.HTTP_201_CREATED, response_model=AccOut)
async def create_account(acc: AccIn):
    try:
        return AccountService.create(acc)
    except Exception as error:
        raise HTTPException(status_code=409, detail=str(error))


@hrp_api.get("/units/{unit_id}/account", status_code=status.HTTP_200_OK, response_model=List[AccOut])
async def get_accounts(skip: int = 0, limit: int = 100):
    try:
        return AccountService.query(offset=skip, limit=limit)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@hrp_api.get("/units/{unit_id}/account/{account_id}", status_code=status.HTTP_200_OK, response_model=AccOut)
async def get_account(account_id: str):
    try:
        return AccountService.read(account_id)
    except NoResultFound as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

""" """


