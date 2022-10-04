from abc import ABC, abstractmethod


class CRUD(ABC):

    @classmethod
    @abstractmethod
    def create(cls, *args, **kwarg):
        pass

    @classmethod
    @abstractmethod
    def read(cls, *args, **kwarg):
        pass

    @classmethod
    @abstractmethod
    def query(cls, offset=0, limit=100):
        pass

    @classmethod
    @abstractmethod
    def update(cls, *args, **kwarg):
        pass

    @classmethod
    @abstractmethod
    def delete(cls, *args, **kwarg):
        pass

