from models.finance.db_schemas.db_target import Target
from models.finance.target.target_accessor import TargetAccessor
from models.finance.target.target_factory import TargetFactory
from models.finance.target.target_specification import TargetSpecification
from hrp.finance.finance.valid_schemas.target_valid import TrgOut
from hrp.main_tool.convertor.valid_convertor import (Convertor, ValidOutConvertor, BaseConvertor,
                                                     CurrencyInConvertor, CurrencyOutConvertor)
from hrp.main_tool.service import Service


class TargetService(Service):

    @classmethod
    def build_service(cls):
        service = cls()
        specific = TargetSpecification.get_specification()
        service.factory = TargetFactory(specific)
        service.obj_access = TargetAccessor(specific)
        valid_out = ValidOutConvertor(TrgOut,
                                      fields_covert=[CurrencyOutConvertor("currency")])
        service.out_convertor = Convertor(valid_out)
        base_conv = BaseConvertor(Target,
                                  fields_covert=[CurrencyInConvertor("currency")])
        service.base_convertor = Convertor(base_conv)

        return service
