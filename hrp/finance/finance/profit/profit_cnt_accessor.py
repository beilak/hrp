from sqlalchemy.sql import exists

from hrp.db.db_conn import DBConn
from models.finance.db_schemas.db_profit_cnt import ProfitCnt
from hrp.main_tool.accessor import Accessor


class ProfitCntAccessor(Accessor):
    def is_exist(self, obj_id):
        with DBConn.get_new_session() as session:
            return session.query(exists().where(ProfitCnt.profit_cnt_id
                                                == obj_id)).scalar()

    def get_obj(self, obj_id) -> ProfitCnt:
        with DBConn.get_new_session() as session:
            return session.query(ProfitCnt).filter(ProfitCnt.profit_cnt_id
                                                   == obj_id).one()
