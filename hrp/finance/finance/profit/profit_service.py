from models.finance.db_schemas.db_profit import Profit
from models.finance.profit.profit_accessor import ProfitAccessor
from models.finance.profit.profit_factory import ProfitFactory
from models.finance.profit.profit_specification import ProfitSpecification
from models.finance.valid_schemas.profit_valid import ProfitOut
from hrp.main_tool.convertor.valid_convertor import (Convertor, ValidOutConvertor, BaseConvertor,
                                                     CurrencyInConvertor, CurrencyOutConvertor)
from hrp.main_tool.service import Service


class ProfitService(Service):

    @classmethod
    def build_service(cls):
        service = cls()
        specific = ProfitSpecification.get_specification()
        service.factory = ProfitFactory(specific)
        service.obj_access = ProfitAccessor(specific)
        valid_out = ValidOutConvertor(ProfitOut,
                                      fields_covert=[CurrencyOutConvertor("currency")])
        service.out_convertor = Convertor(valid_out)
        base_conv = BaseConvertor(Profit,
                                  fields_covert=[CurrencyInConvertor("currency")])
        service.base_convertor = Convertor(base_conv)
        return service
