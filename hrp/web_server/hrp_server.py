from fastapi import FastAPI, status, HTTPException
from models.org import (UserFactory, User, UnitFactory, Unit, UserIn, UserOut,
                        UnitIn, UnitOut, UserUnitIn, UserUnitOut, UnitUserOut)

from sqlalchemy.exc import NoResultFound
from models.model_exceptions.ModelError import ModelError
from typing import List

# Finance
from models import AccountService, AccIn, AccOut
from models import TargetCntService, TargetService, TrgCntIn, TrgCntOut, TrgIn, TrgOut
from models import ProfitCntService, ProfitService, ProfitCntIn, ProfitCntOut, ProfitIn, ProfitOut

# Material
from models import RealEstateService, RealEstateIn, RealEstateOut
from models import AssetService, AssetIn, AssetOut

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


@hrp_api.get("/units/{unit_id}/users",
             status_code=status.HTTP_200_OK,
             response_model=UnitUserOut)
async def get_unit_users(unit_id: str):
    try:
        unit: Unit = UnitFactory.get_unit(unit_id)
        users = [UserOut(**i.__dict__) for i in unit.users]
    except NoResultFound as error:
        raise HTTPException(status_code=404, detail=str(error))
    return UnitUserOut(unit_id=unit_id, users=users)


""" Account endpoint """


@hrp_api.post("/units/{unit_id}/account",
              status_code=status.HTTP_201_CREATED,
              response_model=AccOut)
async def create_account(acc: AccIn):
    try:
        service = AccountService.build_service()
        return service.create(acc)
    except Exception as error:
        raise HTTPException(status_code=409, detail=str(error))


@hrp_api.get("/units/{unit_id}/account", status_code=status.HTTP_200_OK, response_model=List[AccOut])
async def get_accounts(skip: int = 0, limit: int = 100):
    try:
        service = AccountService.build_service()
        return service.query(offset=skip, limit=limit)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@hrp_api.get("/units/{unit_id}/account/{account_id}", status_code=status.HTTP_200_OK, response_model=AccOut)
async def get_account(account_id: str):
    try:
        service = AccountService.build_service()
        return service.read(account_id)
    except NoResultFound as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


""" """

""" Target Center endpoint """


@hrp_api.post("/units/{unit_id}/target_cnt",
              status_code=status.HTTP_201_CREATED, response_model=TrgCntOut)
async def create_target_cnt(trg_cnt: TrgCntIn):
    try:
        service = TargetCntService.build_service()
        return service.create(trg_cnt)
    except Exception as error:
        raise HTTPException(status_code=409, detail=str(error))


@hrp_api.get("/units/{unit_id}/target_cnt",
             status_code=status.HTTP_200_OK, response_model=List[TrgCntOut])
async def get_targets_cnt(skip: int = 0, limit: int = 100):
    try:
        service = TargetCntService.build_service()
        return service.query(offset=skip, limit=limit)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@hrp_api.get("/units/{unit_id}/target_cnt/{target_cnt_id}",
             status_code=status.HTTP_200_OK, response_model=TrgCntOut)
async def get_target_cnt(target_cnt_id: str):
    try:
        service = TargetCntService.build_service()
        return service.read(target_cnt_id)
    except NoResultFound as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


""" """

""" Target endpoint """


@hrp_api.post("/units/{unit_id}/target", status_code=status.HTTP_201_CREATED,
              response_model=TrgOut)
async def create_target(trg: TrgIn):
    try:
        service = TargetService.build_service()
        return service.create(trg)
    except Exception as error:
        raise HTTPException(status_code=409, detail=str(error))


@hrp_api.get("/units/{unit_id}/target", status_code=status.HTTP_200_OK,
             response_model=List[TrgOut])
async def get_targets(skip: int = 0, limit: int = 100):
    try:
        service = TargetService.build_service()
        return service.query(offset=skip, limit=limit)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@hrp_api.get("/units/{unit_id}/target/{target_id}",
             status_code=status.HTTP_200_OK, response_model=TrgOut)
async def get_target(target_id: str):
    try:
        service = TargetService.build_service()
        return service.read(target_id)
    except NoResultFound as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


""" """


""" Profit Center endpoint """


@hrp_api.post("/units/{unit_id}/profit_cnt",
              status_code=status.HTTP_201_CREATED,
              response_model=ProfitCntOut)
async def create_profit_cnt(profit_cnt: ProfitCntIn):
    try:
        service = ProfitCntService.build_service()
        return service.create(profit_cnt)
    except Exception as error:
        raise HTTPException(status_code=409, detail=str(error))


@hrp_api.get("/units/{unit_id}/profit_cnt",
             status_code=status.HTTP_200_OK, response_model=List[ProfitCntOut])
async def get_profits_cnt(skip: int = 0, limit: int = 100):
    try:
        service = ProfitCntService.build_service()
        return service.query(offset=skip, limit=limit)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@hrp_api.get("/units/{unit_id}/profit_cnt/{profit_cnt_id}",
             status_code=status.HTTP_200_OK, response_model=ProfitCntOut)
async def get_profit_cnt(profit_cnt_id: str):
    try:
        service = ProfitCntService.build_service()
        return service.read(profit_cnt_id)
    except NoResultFound as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

""" """


""" Profit  endpoint """


@hrp_api.post("/units/{unit_id}/profit",
              status_code=status.HTTP_201_CREATED,
              response_model=ProfitOut)
async def create_profit(profit: ProfitIn):
    try:
        service = ProfitService.build_service()
        return service.create(profit)
    except Exception as error:
        raise HTTPException(status_code=409, detail=str(error))


@hrp_api.get("/units/{unit_id}/profit",
             status_code=status.HTTP_200_OK, response_model=List[ProfitOut])
async def get_profits(skip: int = 0, limit: int = 100):
    try:
        service = ProfitService.build_service()
        return service.query(offset=skip, limit=limit)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@hrp_api.get("/units/{unit_id}/profit/{profit_id}",
             status_code=status.HTTP_200_OK, response_model=ProfitOut)
async def get_profit(profit_id: str):
    try:
        service = ProfitService.build_service()
        return service.read(profit_id)
    except NoResultFound as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


""" Real Estate  endpoint """


@hrp_api.post("/units/{unit_id}/real_estate",
              status_code=status.HTTP_201_CREATED, response_model=RealEstateOut)
async def create_real_estate(real_estate: RealEstateIn):
    try:
        service = RealEstateService.build_service()
        return service.create(real_estate)
    except Exception as error:
        raise HTTPException(status_code=409, detail=str(error))


@hrp_api.get("/units/{unit_id}/real_estate",
             status_code=status.HTTP_200_OK, response_model=List[RealEstateOut])
async def get_real_estates(skip: int = 0, limit: int = 100):
    try:
        service = RealEstateService.build_service()
        return service.query(offset=skip, limit=limit)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@hrp_api.get("/units/{unit_id}/real_estate/{real_estate_id}",
             status_code=status.HTTP_200_OK, response_model=RealEstateOut)
async def get_real_estate(real_estate_id: str):
    try:
        service = RealEstateService.build_service()
        return service.read(real_estate_id)
    except NoResultFound as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


""" """

""" Assert endpoint """


@hrp_api.post("/units/{unit_id}/asset",
              status_code=status.HTTP_201_CREATED, response_model=AssetOut)
async def create_asset(asset: AssetIn):
    try:
        service = AssetService.build_service()
        return service.create(asset)
    except Exception as error:
        raise HTTPException(status_code=409, detail=str(error))


@hrp_api.get("/units/{unit_id}/asset",
             status_code=status.HTTP_200_OK, response_model=List[AssetOut])
async def get_assets(skip: int = 0, limit: int = 100):
    try:
        service = AssetService.build_service()
        return service.query(offset=skip, limit=limit)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@hrp_api.get("/units/{unit_id}/asset/{asset_id}",
             status_code=status.HTTP_200_OK, response_model=AssetOut)
async def get_asset(asset_id: str):
    try:
        service = AssetService.build_service()
        return service.read(asset_id)
    except NoResultFound as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


""" """
