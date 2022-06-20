from sqlalchemy import String, Column, ForeignKey, DateTime, func, Numeric, CHAR, Integer
from models.db.db_conn import Base
from models.org.unit import Unit
from models.org.user import User


class TargetCnt(Base):
    __tablename__ = "targets_cnt"
    target_cnt_id_type = Integer()
    target_cnt_id = Column(target_cnt_id_type, primary_key=True, autoincrement=True)
    unit_id = Column(Unit.unit_id_type, ForeignKey(Unit.unit_id))
    name = Column(String(32))
    value = Numeric(precision=8)
    currency = Column(CHAR(3))