from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import declarative_base, relationship
from models.db.db_conn import DBConn
from models.unit import Unit

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    user_id_type = String(32)
    user_id = Column(user_id_type, primary_key=True)
    unit_id = Column(Unit.unit_id_type, ForeignKey(Unit.unit_id))
    first_name = Column(String(32))
    last_name = Column(String(32))


def users_singleton(cls):
    def get_singleton():
        if cls.users_singleton is None:
            cls.users_singleton = cls()
        return cls.users_singleton

    return get_singleton


@users_singleton
class Users:
    users_singleton = None

    def __init__(self):
        self._new_users = set()

    def create(self, user_id, unit_id, first_name, last_name) -> User:
        user = User(user_id=user_id, unit_id=unit_id, first_name=first_name, last_name=last_name)
        self._new_users.add(user)
        return user

    def insert(self):
        DBConn.insert(self._new_users)
        users_id = [item.user_id for item in self._users]
        return self.get_users(users_id)

    def get_users(self, users_id: list):
        session = DBConn.get_new_session()
        return session.query(User).filter(User.user_id.in_(users_id)).all()