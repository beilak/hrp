from sqlalchemy import Column, Integer, ForeignKey, String, Numeric, CHAR
from sqlalchemy.orm import declarative_base
from models.db.db_conn import DBConn
from models.unit import Unit
from models.cnt_list import CntList

Base = declarative_base()


class TargetCnt(Base):
    __tablename__ = "targets_cnt"
    target_cnt_id_type = Integer()
    target_cnt_id = Column(target_cnt_id_type, primary_key=True, autoincrement=True)
    unit_id = Column(Unit.unit_id_type, ForeignKey(Unit.unit_id))
    name = Column(String(32))
    value = Numeric(precision=8)
    currency = Column(CHAR(3))


def target_cnt_singleton(cls):
    def get_singleton():
        if cls.trg_cnt_list_singleton is None:
            cls.trg_cnt_list_singleton = cls()
        return cls.trg_cnt_list_singleton

    return get_singleton


@target_cnt_singleton
class TargetCntList(CntList):
    trg_cnt_list_singleton = None

    def create(self, name, value, currency) -> TargetCnt:
        user = TargetCnt(name=name, value=value,
                         currency=currency)
        self._new_users.add(user)
        return user

    def get_target_cnt(self, trg_id: list):
        session = DBConn.get_new_session()
        cnt = session.query(TargetCnt).filter(TargetCnt.target_cnt_id.in_(trg_id)).all()
        for item in cnt:
            self._exist_cnt.remove(item)
            self._exist_cnt.add(item)
        return cnt
