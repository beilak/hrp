from models.finance.db_schemas.db_account import Account
from hrp.main_tool.specification import Specification


class AccountSpecification(Specification):
    @classmethod
    def get_specification(cls):
        return cls(Account)
