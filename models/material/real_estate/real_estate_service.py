from models.material.db_schemas.db_real_estate import RealEstate
from models.material.real_estate.real_estate_accessor import RealEstateAccessor
from models.material.real_estate.real_estate_factory import RealEstateFactory
from models.material.real_estate.real_estate_specification import RealEstateSpecification
from models.material.valid_schemas.real_estate_valid import RealEstateOut
from models.main_tool.convertor.valid_convertor import (Convertor, ValidOutConvertor,
                                                        BaseConvertor, CurrencyInConvertor,
                                                        CurrencyOutConvertor)
from models.main_tool.service import Service


class RealEstateService(Service):

    @classmethod
    def build_service(cls):
        service = cls()
        specific = RealEstateSpecification.get_specification()
        service.factory = RealEstateFactory(specific)
        service.obj_access = RealEstateAccessor(specific)
        valid_out = ValidOutConvertor(RealEstateOut,
                                      fields_covert=[CurrencyOutConvertor("currency")])
        service.out_convertor = Convertor(valid_out)
        base_conv = BaseConvertor(RealEstate,
                                  fields_covert=[CurrencyInConvertor("currency")])
        service.base_convertor = Convertor(base_conv)

        return service
