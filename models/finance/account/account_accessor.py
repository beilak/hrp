from models.main_tool import Accessor
from db.db_conn import DBConn
from sqlalchemy.sql import exists
from models.finance import Account


class AccountAccessor(Accessor):
    def is_exist(self, obj_id):
        with DBConn.get_new_session() as session:
            return session.query(exists().where(Account.acc_id
                                                == obj_id)).scalar()

    def get_obj(self, obj_id) -> Account:
        with DBConn.get_new_session() as session:
            return session.query(Account).filter(Account.acc_id
                                                 == obj_id).one()
