from models.material.db_schemas.db_real_estate import RealEstate
from models.main_tool.specification import Specification


class RealEstateSpecification(Specification):

    @classmethod
    def get_specification(cls):
        return cls(RealEstate)
