from sqlalchemy.sql import exists

from hrp.db.db_conn import DBConn
from models.finance.db_schemas.db_target_cnt import TargetCnt
from hrp.main_tool.accessor import Accessor


class TargetCntAccessor(Accessor):
    def is_exist(self, obj_id):
        with DBConn.get_new_session() as session:
            return session.query(exists().where(TargetCnt.target_cnt_id
                                                == obj_id)).scalar()

    def get_obj(self, obj_id) -> TargetCnt:
        with DBConn.get_new_session() as session:
            return session.query(TargetCnt).filter(TargetCnt.target_cnt_id
                                                   == obj_id).one()
