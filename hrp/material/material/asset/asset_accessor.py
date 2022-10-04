from sqlalchemy.sql import exists

from hrp.db.db_conn import DBConn
from models.material.db_schemas.db_asset import Asset
from hrp.main_tool.accessor import Accessor


class AssetAccessor(Accessor):
    def is_exist(self, obj_id):
        with DBConn.get_new_session() as session:
            return session.query(exists().where(Asset.asset_id
                                                == obj_id)).scalar()

    def get_obj(self, obj_id) -> Asset:
        with DBConn.get_new_session() as session:
            return session.query(Asset).filter(Asset.asset_id
                                               == obj_id).one()
