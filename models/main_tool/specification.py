from abc import ABC, abstractmethod


class Specification(ABC):
    specification_instance = None

    def __init__(self, db_class):
        self._db_class = db_class
        self._id_field = self.db_class.__table__.primary_key.columns.keys()[0]

    @property
    def db_class(self):
        return self._db_class

    @property
    def id_field(self):
        return self._id_field

    @classmethod
    @abstractmethod
    def get_specification(cls):
        db_class = None
        return cls(db_class)
