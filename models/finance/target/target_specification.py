from models.main_tool import Specification
from models.finance import Target


class TargetSpecification(Specification):

    @classmethod
    def get_specification(cls):
        return cls(Target)
