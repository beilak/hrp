from sqlalchemy.sql import exists
from models.db.db_conn import DBConn
from models.model_exceptions.ModelError import ModelError
from models.org.db_schemas.db_user import User
from models.org.pydatic_schemas.user_model import UserIn


class UserFactory:

    @classmethod
    def create(cls, cr_user: UserIn) -> User:
        login = cr_user.login
        if cls.is_user_exist(login) is True:
            raise ModelError("User already exist")
        user = User(**cr_user.dict())
        DBConn.insert({user})
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



