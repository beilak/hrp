from models.finance.valid_schemas.acc_valid import AccOut
from models.finance.db_schemas.db_acc import Account
from db.db_conn import DBConn
from sqlalchemy.sql import exists
from models.main_tool import Factory
from models.finance.account.account_specification import AccountSpecification


class AccountFactory(Factory):
    pass
