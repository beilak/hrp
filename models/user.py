from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func
from sqlalchemy_utils import EmailType
from sqlalchemy_utils import PasswordType
from models.db.db_conn import DBConn
from models.collection import Collection
from sqlalchemy.sql import exists
from pydantic import BaseModel, EmailStr
from models.model_exceptions.ModelError import ModelError

Base = declarative_base()


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


class UserIn(BaseModel):
    login: str
    first_name: str
    last_name: str
    password: str
    email: EmailStr | None


class UserOut(BaseModel):
    login: str
    first_name: str
    last_name: str
    email: EmailStr | None


class UserCollection(Collection):

    @classmethod
    def create(cls, user: UserIn) -> User | None:
        login = user.login
        if cls.is_user_exist(login) is True:
            raise ModelError

        user = User(**user.dict())
        cls._insert_db({user})
        user = cls.get_user(login)
        return user

    @classmethod
    def is_user_exist(cls, login):
        session = DBConn.get_new_session()
        return session.query(exists().where(User.login == login)).scalar()

    @classmethod
    def get_users(cls, login: list | None = None, offset=0, limit=20):
        session = DBConn.get_new_session()
        query = session.query(User).offset(offset).limit(limit)
        if login is not None:
            query = query.filter(User.login.in_(login))
        return query.all()

    @classmethod
    def get_user(cls, login):
        session = DBConn.get_new_session()
        user = session.query(User).filter(User.login == login).one()
        return user

    @classmethod
    def delete_user(cls, user):
        session = DBConn.get_new_session()
        session.query(User).filter(User.login == user.login).delete()
        session.commit()

    def __iter__(self):
        # ToDo
        pass

    def __next__(self):
        # ToDo
        pass



