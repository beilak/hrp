from models.main_tool.abstract_crud import CRUD
from typing import List
from .accessor import Accessor
from .valid_convertor import Convertor, ValidOutConvertor, BaseConvertor
from abc import abstractmethod
from .specification import Specification
from pydantic import BaseModel
from .factory import Factory


class Service(CRUD):

    def __init__(self):
        self.factory: Factory | None = None
        self.obj_access: Accessor | None = None
        self.out_convertor: Convertor | None = None
        self.base_convertor: Convertor | None = None

    @classmethod
    @abstractmethod
    def build_service(cls):
        service = cls()
        specification = Specification.get_specification()
        service.factory = Factory(specification)
        service.obj_access = Accessor(specification)
        service.out_convertor = Convertor(conv_specific=ValidOutConvertor(BaseModel))
        service.base_convertor = Convertor(conv_specific=BaseConvertor(BaseModel))
        return service

    def create(self, obj_in):
        base_obj = self.base_convertor.convert(obj_in)
        created_id = self.factory.create_entity(base_obj)
        return self.read(created_id)

    def read(self, obj_id):
        obj = self.obj_access.get_entity(obj_id)
        return self.out_convertor.convert(obj)

    def query(self, offset=0, limit=100) -> List:
        obj_list = self.obj_access.get_entity_set(offset=offset, limit=limit)
        return [i for i in self.out_convertor.convert_list(*obj_list)]

    def update(self):
        # ToDo
        pass

    def delete(self, obj):
        # ToDo
        pass
