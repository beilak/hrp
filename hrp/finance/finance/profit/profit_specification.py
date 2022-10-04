from models.finance.db_schemas.db_profit import Profit
from hrp.main_tool.specification import Specification


class ProfitSpecification(Specification):

    @classmethod
    def get_specification(cls):
        return cls(Profit)
