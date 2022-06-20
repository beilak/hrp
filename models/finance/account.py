from models.main_tool.abstract_crud import CRUD
from models.finance.valid_schemas.acc_valid import AccIn, AccOut
from models.model_exceptions.ModelError import ModelError
from models.finance.db_schemas.db_acc import Account
from models.db.db_conn import DBConn
from sqlalchemy.sql import exists
from typing import List
import uuid


class AccountFactory:
    @classmethod
    def create_entity(cls, acc_in: AccIn) -> AccOut:
        acc = Account(**acc_in.__dict__)
        DBConn.insert({acc})
        with DBConn.get_new_session() as session:
            session.add(acc)
            session.flush()
            acc_id = acc.acc_id
            session.commit()
        return AccOut(**cls.get_acc(acc_id).__dict__)

    @classmethod
    def get_entity(cls, acc_id) -> AccOut:
        return AccOut(**cls.get_acc(acc_id).__dict__)

    @classmethod
    def get_entity_set(cls, offset=0, limit=100) -> List[AccOut]:
        with DBConn.get_new_session() as session:
            query = session.query(Account).offset(offset).limit(limit)
            return [AccOut(**i.__dict__) for i in query.all()]

    @classmethod
    def update_entity(cls):
        # ToDo implant upd account
        pass

    @classmethod
    def delete_entity(cls, acc: AccIn):
        account = Account(**acc.__dict__)
        with DBConn.get_new_session() as session:
            session.query(account).filter(account.unit_id == account.unit_id).delete()
            session.commit()

    @classmethod
    def is_acc_exist(cls, acc_id):
        with DBConn.get_new_session() as session:
            return session.query(exists().where(Account.acc_id == acc_id)).scalar()

    @classmethod
    def get_acc(cls, acc_id) -> Account:
        with DBConn.get_new_session() as session:
            return session.query(Account).filter(Account.acc_id == acc_id).one()


class AccountService(CRUD):

    @classmethod
    def create(cls, acc_in: AccIn) -> AccOut:
        return AccountFactory.create_entity(acc_in)

    @classmethod
    def read(cls, acc_id) -> AccOut:
        return AccountFactory.get_entity(acc_id)

    @classmethod
    def query(cls, offset=0, limit=100) -> List[AccOut]:
        return AccountFactory.get_entity_set(offset=0, limit=100)

    @classmethod
    def update(cls):
        AccountFactory.update_entity()

    @classmethod
    def delete(cls, acc: AccIn):
        AccountFactory.delete_entity(acc)