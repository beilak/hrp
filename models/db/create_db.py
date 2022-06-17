from models.db.db_conn import DBConn
from models.db.db_conn import Base

Base.metadata.drop_all(DBConn.get_db_connect())
Base.metadata.create_all(DBConn.get_db_connect())

