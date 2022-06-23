from models.main_tool import Specification
from models.finance import TargetCnt


class TargetCntSpecification(Specification):

    @classmethod
    def get_specification(cls):
        return cls(TargetCnt)
