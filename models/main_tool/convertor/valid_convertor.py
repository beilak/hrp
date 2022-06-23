from abc import ABC, abstractmethod

from sqlalchemy_utils.types.currency import Currency

from db.db_conn import Base


class Convertor:
    def __init__(self, conv_specific):
        self.conv_specific = conv_specific

    def convert(self, obj):
        return self.conv_specific.convert(obj)

    def convert_list(self, *args):
        return self.conv_specific.convert_list(*args)


class ConvertorSpecific(ABC):
    @abstractmethod
    def __init__(self, *args):
        self.fields_covert = None
        pass

    @abstractmethod
    def convert(self, *args):
        pass

    def convert_fields(self, field_dict) -> dict:
        if self.fields_covert is not None:
            for field in self.fields_covert:
                field_dict[field.name] = field.convert(field_dict[field.name])
        return field_dict

    def convert_list(self, *args):
        for item in args:
            yield self.convert(item)


class FieldCovertSpecific(ConvertorSpecific):
    def __init__(self, name):
        self.name = name

    def convert(self, field_val):
        pass


class ValidOutConvertor(ConvertorSpecific):
    def __init__(self, valid_class_out, fields_covert: list[FieldCovertSpecific] = None):
        self.valid_class_out = valid_class_out
        self.fields_covert = fields_covert

    def convert(self, base_obj):
        obj_base_dict = dict(**base_obj.__dict__)
        obj_base_dict = self.convert_fields(obj_base_dict)
        return self.valid_class_out(**obj_base_dict)


class BaseConvertor(ConvertorSpecific):
    def __init__(self, base_class: Base,  fields_covert: list[FieldCovertSpecific] = None):
        self.base_class = base_class
        self.fields_covert = fields_covert

    def convert(self, in_obj):
        obj_in_dict = dict(**in_obj.__dict__)
        if hasattr(in_obj, "target_id"):
            print("obj_in_dict", in_obj.target_id)
        obj_in_dict = self.convert_fields(obj_in_dict)
        return self.base_class(**obj_in_dict)


class CurrencyInConvertor(FieldCovertSpecific):
    def convert(self, field_val):
        return Currency(field_val)


class CurrencyOutConvertor(FieldCovertSpecific):
    def convert(self, field_val):
        return str(field_val)
