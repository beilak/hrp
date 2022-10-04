from abc import ABC, abstractmethod
from typing import List

from hrp.db.db_conn import DBConn
from hrp.main_tool.specification import Specification


# from .singleton import Singleton


class Accessor(ABC):
    def __init__(self, specification: Specification):
        self.specification = specification

    def get_entity(self, obj_id):
        return self.get_obj(obj_id)

    def get_entity_set(self, offset=0, limit=100) -> List:
        with DBConn.get_new_session() as session:
            query = session.query(self.specification.db_class).offset(offset).limit(limit)
            return query.all()

    def update_entity(self, *args, **kwarg):
        # ToDo implant upd account
        pass

    def delete_entity(self, obj_id):
        obj = self.get_obj(obj_id)
        with DBConn.get_new_session() as session:
            session.delete(obj)
            session.commit()
        return self.get_obj(obj_id)

    @abstractmethod
    def is_exist(self, obj_id):
        pass

    @abstractmethod
    def get_obj(self, obj_id):
        pass

