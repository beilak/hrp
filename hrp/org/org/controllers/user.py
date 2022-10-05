from sqlalchemy.sql import exists

from ..db.db_conn import DBConn
from ..db_schemas.db_user import User
from .error import UserExist, UserAssignedUnit
from ..models.user import UserRequestModel


class UserFactory:
    def __init__(
            self,
    ) -> None:
        ...
    # ToDo Add DB session

    async def create(self, cr_user: UserRequestModel) -> User:
        login = cr_user.login
        if self.is_user_exist(login) is True:
            raise UserExist(login)
        user = User(**cr_user.dict())
        DBConn.insert({user})
        user = self.get_user(login)
        return await user

    async def is_user_exist(self, login):
        with DBConn.get_new_session() as session:
            return session.query(exists().where(User.login == login)).scalar()

    async def get_users(self, login: list | None = None, offset=0, limit=100):
        with DBConn.get_new_session() as session:
            query = session.query(User).offset(offset).limit(limit)
            if login is not None:
                query = query.filter(User.login.in_(login))
            return query.all()

    async def get_user(self, login):
        with DBConn.get_new_session() as session:
            user = session.query(User).filter(User.login == login).one()
            return user

    async def delete_user(self, user):
        with DBConn.get_new_session() as session:
            session.query(User).filter(User.login == user.login).delete()
            session.commit()

    async def is_user_in_unit(self, user: User, unit_id):
        for exist_unit in user.units:
            if unit_id == exist_unit.unit_id:
                return True
        return False

    async def join_to_unit(self, login: str, unit) -> User:
        with DBConn.get_new_session() as session:
            user = session.query(User).filter(User.login == login).one()
            if self.is_user_in_unit(user, unit.unit_id) is True:
                raise UserAssignedUnit(user, unit.unit_id)
            user.units.append(unit)
            session.commit()

        user = self.get_user(login)
        return await user
