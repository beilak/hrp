from sqlalchemy.sql import exists

from hrp.db.db_conn import DBConn
from models.finance.db_schemas.db_profit import Profit
from hrp.main_tool.accessor import Accessor


class ProfitAccessor(Accessor):
    def is_exist(self, obj_id):
        with DBConn.get_new_session() as session:
            return session.query(exists().where(Profit.profit_id
                                                == obj_id)).scalar()

    def get_obj(self, obj_id) -> Profit:
        with DBConn.get_new_session() as session:
            return session.query(Profit).filter(Profit.profit_id
                                                == obj_id).one()
