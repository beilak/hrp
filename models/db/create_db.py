from sqlalchemy.orm import declarative_base
from models.db.db_conn import DBConn
from models.unit import Unit
from models.user import User
from models.unit_user import UnitUser
from models.db.db_conn import Base

Base.metadata.drop_all(DBConn.get_db_connect())
Base.metadata.create_all(DBConn.get_db_connect())

