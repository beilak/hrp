from models.finance.db_schemas.db_target_cnt import TargetCnt
from models.main_tool.specification import Specification


class TargetCntSpecification(Specification):

    @classmethod
    def get_specification(cls):
        return cls(TargetCnt)
