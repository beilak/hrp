from models.finance.db_schemas.db_target import Target
from models.main_tool.service import Specification


class TargetSpecification(Specification):

    @classmethod
    def get_specification(cls):
        return cls(Target)
