from models.material.db_schemas.db_asset import Asset
from hrp.main_tool.specification import Specification


class AssetSpecification(Specification):

    @classmethod
    def get_specification(cls):
        return cls(Asset)
