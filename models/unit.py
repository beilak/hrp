import os
from sqlalchemy import Column, String, ForeignKey, DateTime, Integer
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func
from sqlalchemy_utils import PasswordType
from models.db.db_conn import DBConn
from models.user import User

Base = declarative_base()


class Unit(Base):
    __tablename__ = "units"
    unit_id_type = Integer()
    unit_id = Column(unit_id_type, primary_key=True, autoincrement=True)
    name = Column(String(32))
    #users = relationship("users", backref="unit_user_ref")
    admin = Column(String(32), ForeignKey(User.login), nullable=False)
    join_pass = Column(PasswordType(schemes=['pbkdf2_sha512']))
    cr_date = Column(DateTime(timezone=True), server_default=func.now())
    upd_date = Column(DateTime(timezone=True), onupdate=func.now())


class UnitCollections:
    # ToDo Add list of units

    @classmethod
    def create_unit(cls, name, admin, join_pass=None):
        if join_pass is None:
            join_pass = os.urandom()
        unit = Unit(name=name, admin=admin,
                    unit_joining_pass=join_pass)
        DBConn.insert((unit,))
        return unit

    @classmethod
    def get_units(cls, unit_id):
        session = DBConn.get_new_session()
        return session.query(Unit).filter(Unit.unit_id == unit_id).one()