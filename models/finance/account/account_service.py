from typing import List

from models.finance.account.account_factory import AccountFactory
from models.finance.db_schemas.db_acc import Account
from models.finance.valid_schemas.acc_valid import AccIn, AccOut
from models.finance.account.account_accessor import AccountAccessor
from models.finance.account.account_specification import AccountSpecification
from models.main_tool import Convertor, ValidOutConvertor, BaseConvertor
from models.main_tool import Service
from models.main_tool import Singleton


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


if __name__ == '__main__':
    service = AccountService.build_service()
    print(service.query())

    acc_in = AccIn(acc_number="12345", unit_id="test_unit_id_1",
                   user_login="TEST_USER1",acc_type="DEBIT_CARD",
                   description="blabla", bank="dddd")
    print(service.create(acc_in))
#    print(service.read(8))

