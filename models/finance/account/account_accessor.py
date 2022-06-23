from sqlalchemy.sql import exists

from db.db_conn import DBConn
from models.finance.db_schemas.db_account import Account
from models.main_tool.accessor import Accessor


class AccountAccessor(Accessor):
    def is_exist(self, obj_id):
        with DBConn.get_new_session() as session:
            return session.query(exists().where(Account.acc_id
                                                == obj_id)).scalar()

    def get_obj(self, obj_id) -> Account:
        with DBConn.get_new_session() as session:
            return session.query(Account).filter(Account.acc_id
                                                 == obj_id).one()
