from sqlalchemy.sql import exists

from db.db_conn import DBConn
from models.finance import Target
from models.main_tool import Accessor


class TargetAccessor(Accessor):
    def is_exist(self, obj_id):
        with DBConn.get_new_session() as session:
            return session.query(exists().where(Target.target_id
                                                == obj_id)).scalar()

    def get_obj(self, obj_id) -> Target:
        with DBConn.get_new_session() as session:
            return session.query(Target).filter(Target.target_id
                                                == obj_id).one()
