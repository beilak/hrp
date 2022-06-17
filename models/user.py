from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func, exists
from sqlalchemy_utils import EmailType, PasswordType
from models.db.db_conn import DBConn
from models.collection import Collection

from models.model_exceptions.ModelError import ModelError

from models.unit_user import UnitUser
from models.pydatic_schemas.schemas import UserIn

#from models.unit import Unit

#Base = declarative_base()
from models.db.db_conn import Base


class User(Base):
    __tablename__ = "users"
    user_id_type = Integer()
    login = Column(String(32), primary_key=True)
    password = Column(PasswordType(schemes=['pbkdf2_sha512']))
    first_name = Column(String(32))
    last_name = Column(String(32))
    email = Column(EmailType)
    cr_date = Column(DateTime(timezone=True), server_default=func.now())
    upd_date = Column(DateTime(timezone=True), onupdate=func.now())
    units = relationship('Unit', secondary=UnitUser, uselist=True,
                         back_populates="users", lazy='joined')


class UserCollection(Collection):

    @classmethod
    def create(cls, cr_user: UserIn) -> User:
        login = cr_user.login
        if cls.is_user_exist(login) is True:
            raise ModelError("User already exist")
        user = User(**cr_user.dict())
        cls._insert_db({user})
        user = cls.get_user(login)
        return user

    @classmethod
    def is_user_exist(cls, login):
        with DBConn.get_new_session() as session:
            return session.query(exists().where(User.login == login)).scalar()

    @classmethod
    def get_users(cls, login: list | None = None, offset=0, limit=100):
        with DBConn.get_new_session() as session:
            query = session.query(User).offset(offset).limit(limit)
            if login is not None:
                query = query.filter(User.login.in_(login))
            return query.all()

    @classmethod
    def get_user(cls, login):
        with DBConn.get_new_session() as session:
            user = session.query(User).filter(User.login == login).one()
            return user

    @classmethod
    def delete_user(cls, user):
        with DBConn.get_new_session() as session:
            session.query(User).filter(User.login == user.login).delete()
            session.commit()

    @classmethod
    def is_user_in_unit(cls, user: User, unit_id):
        for exist_unit in user.units:
            if unit_id == exist_unit.unit_id:
                return True
        return False

    @classmethod
    def join_to_unit(cls, login: str, unit) -> User:
        with DBConn.get_new_session() as session:
            user = session.query(User).filter(User.login == login).one()
            if cls.is_user_in_unit(user, unit.unit_id) is True:
                raise ModelError("User already assigned to Unit")
            user.units.append(unit)
            session.commit()

        user = cls.get_user(login)
        return user

    def __iter__(self):
        # ToDo
        pass

    def __next__(self):
        # ToDo
        pass



