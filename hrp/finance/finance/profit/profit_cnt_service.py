from models.finance.db_schemas.db_profit_cnt import ProfitCnt
from models.finance.profit.profit_cnt_accessor import ProfitCntAccessor
from models.finance.profit.profit_cnt_factory import ProfitCntFactory
from models.finance.profit.profit_cnt_specification import ProfitCntSpecification
from models.finance.valid_schemas.profit_cnt_valid import ProfitCntOut
from hrp.main_tool.convertor.valid_convertor import (Convertor, ValidOutConvertor, BaseConvertor,
                                                     CurrencyInConvertor, CurrencyOutConvertor)
from hrp.main_tool.service import Service


class ProfitCntService(Service):

    @classmethod
    def build_service(cls):
        service = cls()
        specific = ProfitCntSpecification.get_specification()
        service.factory = ProfitCntFactory(specific)
        service.obj_access = ProfitCntAccessor(specific)
        valid_out = ValidOutConvertor(ProfitCntOut,
                                      fields_covert=[CurrencyOutConvertor("currency")])
        service.out_convertor = Convertor(valid_out)
        base_conv = BaseConvertor(ProfitCnt,
                                  fields_covert=[CurrencyInConvertor("currency")])
        service.base_convertor = Convertor(base_conv)
        return service
