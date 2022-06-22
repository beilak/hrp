from db.db_conn import Base
from .singleton import Singleton
from abc import ABC, abstractmethod


class Convertor():
    def __init__(self, conv_specific):
        self.conv_specific = conv_specific

    def convert(self, obj):
        return self.conv_specific.convert(obj)

    def convert_list(self, *args):
        return self.conv_specific.convert_list(*args)


class ConvertorSpecific(ABC):
    @abstractmethod
    def __init__(self, *args):
        pass

    @abstractmethod
    def convert(self, *args):
        pass

    def convert_list(self, *args):
        for item in args:
            yield self.convert(item)


class ValidOutConvertor(ConvertorSpecific):
    def __init__(self, valid_class_out):
        self.valid_class_out = valid_class_out

    def convert(self, base_obj):
        return self.valid_class_out(**base_obj.__dict__)


class BaseConvertor(ConvertorSpecific):
    def __init__(self, base_class):
        self.base_class = base_class

    def convert(self, in_obj):
        return self.base_class(**in_obj.__dict__)

