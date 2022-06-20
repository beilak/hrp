from models.db.db_conn import DBConn
from models.db.db_conn import Base
from models.directory.acc_type import *
from models.org.db_schemas.db_unit import *
from models.org.db_schemas.db_user import *
from models.org.db_schemas.db_unit_user import *
from models.finance.db_schemas.db_acc import *


Base.metadata.drop_all(DBConn.get_db_connect())
Base.metadata.create_all(DBConn.get_db_connect())

