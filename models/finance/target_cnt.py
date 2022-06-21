from models.main_tool.factory import Factory
from models.finance import TargetCnt, TrgCntOut, TrgCntIn
from db.db_conn import DBConn
from sqlalchemy.sql import exists
from models.main_tool.abstract_crud import CRUD
from typing import List
from sqlalchemy_utils.types.currency import Currency


class TargetCntFactory(Factory):

    def __init__(self):
        self.DB_class = TargetCnt
        self.valid_out_class = TrgCntOut
        self.id_field = "target_cnt_id"

    def is_exist(self, obj_id):
        with DBConn.get_new_session() as session:
            return session.query(exists().where(TargetCnt.target_cnt_id == obj_id)).scalar()

    def get_obj(self, obj_id) -> TargetCnt:
        with DBConn.get_new_session() as session:
            return session.query(TargetCnt).filter(TargetCnt.target_cnt_id == obj_id).one()


class TargetCntService(CRUD):

    @classmethod
    def create(cls, trg_cnt_in: TrgCntIn) -> TrgCntOut:
        obj_in_dict = dict(**trg_cnt_in.__dict__)
        obj_in_dict['currency'] = Currency(obj_in_dict['currency'])
        obj_in_dict['init_currency'] = Currency(obj_in_dict['init_currency'])
        trg_cnt = TargetCnt(**obj_in_dict)
        created_obj = TargetCntFactory().create_entity(trg_cnt)
        created_obj_dict = dict(**created_obj.__dict__)
        created_obj_dict['currency'] = str(created_obj_dict['currency'])
        created_obj_dict['init_currency'] = str(created_obj_dict['init_currency'])
        return TrgCntOut(**created_obj_dict)

    @classmethod
    def read(cls, trg_cnt_id) -> TrgCntOut:
        trg_cnt_dict = dict(**TargetCntFactory().get_entity(trg_cnt_id).__dict__)
        trg_cnt_dict['currency'] = str(trg_cnt_dict['currency'])
        trg_cnt_dict['init_currency'] = str(trg_cnt_dict['init_currency'])
        return TrgCntOut(**trg_cnt_dict)

    @classmethod
    def query(cls, offset=0, limit=100) -> List[TrgCntOut]:
        trg_cnt_list = TargetCntFactory().get_entity_set(offset=0, limit=100)
        out = []
        for i in trg_cnt_list:
            trg_cnt_dict = dict(**i.__dict__)
            trg_cnt_dict['currency'] = str(trg_cnt_dict['currency'])
            trg_cnt_dict['init_currency'] = str(trg_cnt_dict['init_currency'])
            out.append(TrgCntOut(**trg_cnt_dict))
        return out

    @classmethod
    def update(cls):
        TargetCntFactory().update_entity()

    @classmethod
    def delete(cls, trg_cnt_id: TrgCntIn):
        TargetCntFactory().delete_entity(trg_cnt_id)


def main1():
    print("c")
    a = TargetCnt(unit_id = 'TEST',
              name = "n", description ="s",
            account_id = "16",
        value = "100_000.00",
        currency = Currency("USD"),
        init_value = "100_000.00",
        init_currency = Currency("USD"))
    print(type(a))

if __name__ == "__main__":
    main1()