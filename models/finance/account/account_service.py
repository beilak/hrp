from models.finance.account.account_accessor import AccountAccessor
from models.finance.account.account_factory import AccountFactory
from models.finance.account.account_specification import AccountSpecification
from models.finance.db_schemas.db_account import Account
from models.finance.valid_schemas.account_valid import AccIn, AccOut
from models.main_tool.convertor.valid_convertor import Convertor, ValidOutConvertor, BaseConvertor
from models.main_tool.service import Service


class AccountService(Service):

    @classmethod
    def build_service(cls):
        acc_service = cls()
        acc_specific = AccountSpecification.get_specification()
        acc_service.factory = AccountFactory(acc_specific)
        acc_service.obj_access = AccountAccessor(acc_specific)
        acc_service.out_convertor = Convertor(ValidOutConvertor(AccOut))
        acc_service.base_convertor = Convertor(BaseConvertor(Account))
        return acc_service
