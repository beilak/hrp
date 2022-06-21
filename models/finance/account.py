from models.main_tool.abstract_crud import CRUD
from models.finance.valid_schemas.acc_valid import AccIn, AccOut
from models.finance.db_schemas.db_acc import Account
from db.db_conn import DBConn
from sqlalchemy.sql import exists
from typing import List
from models.main_tool.factory import Factory


class AccountFactory(Factory):

    def __init__(self):
        self.DB_class = Account
        self.valid_out_class = AccOut
        self.id_field = "acc_id"

    def is_exist(self, obj_id):
        with DBConn.get_new_session() as session:
            return session.query(exists().where(Account.acc_id == obj_id)).scalar()

    def get_obj(self, obj_id) -> Account:
        with DBConn.get_new_session() as session:
            return session.query(Account).filter(Account.acc_id == obj_id).one()


class AccountService(CRUD):

    @classmethod
    def create(cls, acc_in: AccIn) -> AccOut:
        return AccOut(**AccountFactory().create_entity(Account(**acc_in.__dict__)).__dict__)

    @classmethod
    def read(cls, acc_id) -> AccOut:
        return AccOut(**AccountFactory().get_entity(acc_id).__dict__)

    @classmethod
    def query(cls, offset=0, limit=100) -> List[AccOut]:
        return [AccOut(**i.__dict__) for i in AccountFactory().get_entity_set(offset=0, limit=100)]

    @classmethod
    def update(cls):
        AccountFactory().update_entity()

    @classmethod
    def delete(cls, acc: AccIn):
        AccountFactory().delete_entity(acc)
