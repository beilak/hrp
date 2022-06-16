from sqlalchemy.orm import declarative_base
from models.db.db_conn import DBConn
from models.unit import Unit
from models.user import User

Base = declarative_base()


User.metadata.create_all(DBConn.get_db_connect())
Unit.metadata.create_all(DBConn.get_db_connect())


