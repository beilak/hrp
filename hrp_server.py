from fastapi import FastAPI, status
from valid_type import *

hrp_api = FastAPI()


@hrp_api.get("/units")
async def get_units():
    pass


@hrp_api.get("/units/{unit_id}")
async def get_unit(unit_id: str):
    pass


@hrp_api.post("/units/", status_code=status.HTTP_201_CREATED)
async def create_unit(unit: Unit):
    pass


@hrp_api.get("/units/{unit_id}/users")
async def get_users(unit_id: str):
    pass


@hrp_api.get("/units/{unit_id}/users/{user_id}")
async def get_user(unit_id: str, user_id: str):
    pass


@hrp_api.post("/units/{unit_id}/users/", status_code=status.HTTP_201_CREATED)
async def create_user(unit_id: str, user: User):
    pass
