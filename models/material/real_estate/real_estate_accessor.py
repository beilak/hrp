from sqlalchemy.sql import exists

from db.db_conn import DBConn
from models.material.db_schemas.db_real_estate import RealEstate
from models.main_tool.accessor import Accessor


class RealEstateAccessor(Accessor):
    def is_exist(self, obj_id):
        with DBConn.get_new_session() as session:
            return session.query(exists().where(RealEstate.real_estate_id
                                                == obj_id)).scalar()

    def get_obj(self, obj_id) -> RealEstate:
        with DBConn.get_new_session() as session:
            return session.query(RealEstate).filter(RealEstate.real_estate_id
                                                    == obj_id).one()
