from models.finance.db_schemas.db_target import TargetCnt
from models.finance.target.target_cnt_accessor import TargetCntAccessor
from models.finance.target.target_cnt_factory import TargetCntFactory
from models.finance.target.target_cnt_specification import TargetCntSpecification
from models.finance.valid_schemas.target_cnt_valid import TrgCntOut
from models.main_tool.convertor.valid_convertor import (Convertor, ValidOutConvertor, BaseConvertor,
                                                        CurrencyInConvertor, CurrencyOutConvertor)
from models.main_tool.service import Service


class TargetCntService(Service):
    
    @classmethod
    def build_service(cls):
        service = cls()
        specific = TargetCntSpecification.get_specification()
        service.factory = TargetCntFactory(specific)
        service.obj_access = TargetCntAccessor(specific)
        valid_out = ValidOutConvertor(TrgCntOut,
                                      fields_covert=[CurrencyOutConvertor("currency"),
                                                     CurrencyOutConvertor("init_currency")])
        service.out_convertor = Convertor(valid_out)
        base_conv = BaseConvertor(TargetCnt,
                                  fields_covert=[CurrencyInConvertor("currency"),
                                                 CurrencyInConvertor("init_currency")])
        service.base_convertor = Convertor(base_conv)
        return service
