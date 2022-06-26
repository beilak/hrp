from models.material.db_schemas.db_asset import Asset
from models.material.asset.asset_accessor import AssetAccessor
from models.material.asset.asset_factory import AssetFactory
from models.material.asset.asset_specification import AssetSpecification
from models.material.valid_schemas.asset_valid import AssetOut
from models.main_tool.convertor.valid_convertor import (Convertor, ValidOutConvertor,
                                                        BaseConvertor, CurrencyInConvertor,
                                                        CurrencyOutConvertor)
from models.main_tool.service import Service


class AssetService(Service):

    @classmethod
    def build_service(cls):
        service = cls()
        specific = AssetSpecification.get_specification()
        service.factory = AssetFactory(specific)
        service.obj_access = AssetAccessor(specific)
        valid_out = ValidOutConvertor(AssetOut,
                                      fields_covert=[CurrencyOutConvertor("currency")])
        service.out_convertor = Convertor(valid_out)
        base_conv = BaseConvertor(Asset,
                                  fields_covert=[CurrencyInConvertor("currency")])
        service.base_convertor = Convertor(base_conv)

        return service
