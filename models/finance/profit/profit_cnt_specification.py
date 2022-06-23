from models.finance.db_schemas.db_profit_cnt import ProfitCnt
from models.main_tool.specification import Specification


class ProfitCntSpecification(Specification):

    @classmethod
    def get_specification(cls):
        return cls(ProfitCnt)
