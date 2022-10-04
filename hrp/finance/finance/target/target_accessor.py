from sqlalchemy.sql import exists

from hrp.db.db_conn import DBConn
from models.finance.db_schemas.db_target import Target
from hrp.main_tool.accessor import Accessor


class TargetAccessor(Accessor):
    def is_exist(self, obj_id):
        with DBConn.get_new_session() as session:
            return session.query(exists().where(Target.target_id
                                                == obj_id)).scalar()

    def get_obj(self, obj_id) -> Target:
        with DBConn.get_new_session() as session:
            return session.query(Target).filter(Target.target_id
                                                == obj_id).one()
