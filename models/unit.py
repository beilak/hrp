import os
from sqlalchemy import Column, String, ForeignKey, DateTime, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func, exists
from sqlalchemy_utils import PasswordType
from models.db.db_conn import DBConn
from models.model_exceptions.ModelError import ModelError
from models.unit_user import UnitUser
from models.pydatic_schemas.schemas import UnitIn

from models.db.db_conn import Base


class Unit(Base):
    __tablename__ = "units"
    unit_id_type = String(32)
    unit_id = Column(unit_id_type, primary_key=True)
    description = Column(String(32))
    admin = Column(String(32), ForeignKey("users.login"), nullable=False)
    join_pass = Column(PasswordType(schemes=['pbkdf2_sha512']))
    cr_date = Column(DateTime(timezone=True), server_default=func.now())
    upd_date = Column(DateTime(timezone=True), onupdate=func.now())
    users = relationship("User", secondary=UnitUser, uselist=True,
                         back_populates="units", lazy='joined')


class UnitCollection:
    # ToDo Add list of units

    @classmethod
    def create(cls, unit_in: UnitIn):
        unit_id = unit_in.unit_id
        if cls.is_unit_exist(unit_id) is True:
            raise ModelError("Unit already exist")

        if unit_in.join_pass is None:
            unit_in.join_pass = os.urandom()
        unit = Unit(**unit_in.__dict__)
        DBConn.insert((unit,))
        unit = cls.get_unit(unit_id)
        return unit

    @classmethod
    def is_unit_exist(cls, unit_id):
        with DBConn.get_new_session() as session:
            return session.query(exists().where(Unit.unit_id == unit_id)).scalar()

    @classmethod
    def get_unit(cls, unit_id):
        with DBConn.get_new_session() as session:
            return session.query(Unit).filter(Unit.unit_id == unit_id).one()

    @classmethod
    def get_units(cls, offset=0, limit=100):
        with DBConn.get_new_session() as session:
            query = session.query(Unit).offset(offset).limit(limit)
            return query.all()

    @classmethod
    def delete_unit(cls, unit):
        with DBConn.get_new_session() as session:
            session.query(Unit).filter(Unit.unit_id == unit.unit_id).delete()
            session.commit()
