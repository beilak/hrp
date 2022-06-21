from db.db_conn import DBConn
from db.db_conn import Base
from pydantic import BaseModel
from abc import ABC, abstractmethod
from typing import List


class Factory(ABC):

    @abstractmethod
    def __init__(self):
        self.DB_class = Base
        # self.valid_out_class = BaseModel
        self.id_field = ""

    def create_entity(self, obj):
        with DBConn.get_new_session() as session:
            session.add(obj)
            session.flush()
            obj_id = getattr(obj, self.id_field)
            session.commit()
        return self.get_obj(obj_id)  # self.valid_out_class(**self.get_obj(obj_id).__dict__)

    def get_entity(self, obj_id):
        return self.get_obj(obj_id)  # self.valid_out_class(**self.get_obj(obj_id).__dict__)

    def get_entity_set(self, offset=0, limit=100) -> List:
        with DBConn.get_new_session() as session:
            query = session.query(self.DB_class).offset(offset).limit(limit)
            return query.all()  # [self.valid_out_class(**i.__dict__) for i in query.all()]

    def update_entity(self, *args, **kwarg):
        # ToDo implant upd account
        pass

    def delete_entity(self, obj_id):
        obj = self.get_obj(obj_id)
        with DBConn.get_new_session() as session:
            session.delete(obj)
            session.commit()
        return self.get_obj(obj_id)  # self.valid_out_class(**self.get_obj(obj_id).__dict__)

    @abstractmethod
    def is_exist(self, obj_id):
        pass

    @abstractmethod
    def get_obj(self, obj_id):
        pass
