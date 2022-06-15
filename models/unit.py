from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

from sqlalchemy.orm import Session, sessionmaker
from models.db.db_conn import DBConn

Base = declarative_base()


class Unit(Base):
    __tablename__ = "units"
    unit_id_type = String(32)
    unit_id = Column(unit_id_type, primary_key=True)
    name = Column(String(32))

    @classmethod
    def create_unit(cls, unit_id, name):
        unit = Unit(unit_id=unit_id, name=name)
        DBConn.insert((unit,))
        return unit

    @classmethod
    def get_unit(cls, unit_id):
        session = DBConn.get_new_session()
        return session.query(Unit).filter(Unit.unit_id == unit_id).one()