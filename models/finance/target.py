from models.main_tool.factory import Factory
from models.finance.db_schemas.db_target import Target
from models.finance.valid_schemas.target_valid import TrgOut, TrgIn
from db.db_conn import DBConn
from sqlalchemy.sql import exists
from models.main_tool.abstract_crud import CRUD
from typing import List
from sqlalchemy_utils.types.currency import Currency


class TargetFactory(Factory):
    def __init__(self):
        self.DB_class = Target
        self.valid_out_class = TrgOut
        self.id_field = "target_id"

    @classmethod
    def is_exist(cls, obj_id):
        with DBConn.get_new_session() as session:
            return session.query(exists().where(Target.target_id == obj_id)).scalar()

    @classmethod
    def get_obj(cls, obj_id) -> Target:
        with DBConn.get_new_session() as session:
            return session.query(Target).filter(Target.target_id == obj_id).one()


class TargetService(CRUD):

    @classmethod
    def create(cls, trg_in: TrgIn) -> TrgOut:
        obj_in_dict = dict(**trg_in.__dict__)
        obj_in_dict['currency'] = Currency(trg_in.currency)
        target = Target(**obj_in_dict)
        return TargetFactory().create_entity(target)

    @classmethod
    def read(cls, trg_id) -> TrgOut:
        return TargetFactory().get_entity(trg_id)

    @classmethod
    def query(cls, offset=0, limit=100) -> List[TrgOut]:
        return TargetFactory().get_entity_set(offset=0, limit=100)

    @classmethod
    def update(cls):
        TargetFactory().update_entity()

    @classmethod
    def delete(cls, trg__id: TrgIn):
        TargetFactory().delete_entity(trg__id)
