from models.main_tool import Specification
from models.finance import Account


class AccountSpecification(Specification):

    @staticmethod
    def get_specification():
        return AccountSpecification(Account)
