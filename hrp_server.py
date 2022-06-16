from fastapi import FastAPI, status, HTTPException
from models.user import UserCollection, UserIn, UserOut, User
from models.model_exceptions.ModelError import ModelError
from typing import List

hrp_api = FastAPI()


@hrp_api.get("/users/{login}", response_model=UserOut)
async def get_user(login: str):
    user: User = UserCollection.get_user(login)
    return UserOut(**user.__dict__)


@hrp_api.post("/users/", status_code=status.HTTP_201_CREATED, response_model=UserOut)
async def create_user(user: UserIn):
    if UserCollection.is_user_exist(user.login) is True:
        raise HTTPException(status_code=409, detail="User already exist")
    user_out = UserCollection.create(user)
    return UserOut(**user_out.__dict__)


@hrp_api.get("/users/", response_model=List[UserOut])
def read_users(skip: int = 0, limit: int = 100):
    users = UserCollection.get_users(offset=skip, limit=limit)
    users_out = []
    for user in users:
        users_out.append(UserOut(**user.__dict__))
    return users_out


@hrp_api.get("/units")
async def get_units():
    pass


@hrp_api.get("/units/{unit_id}")
async def get_unit(unit_id: str):
    pass

'''
@hrp_api.post("/units/", status_code=status.HTTP_201_CREATED)
async def create_unit(unit: Unit):
    pass
'''

@hrp_api.get("/units/{unit_id}/users")
async def get_users(unit_id: str):
    pass
