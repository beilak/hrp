from sqlalchemy import Column, ForeignKey, DateTime, func, Numeric, Integer
from sqlalchemy.orm import composite
from db.db_conn import Base
from models.org.user import User
from sqlalchemy_utils.types.currency import CurrencyType
from models.finance.db_schemas.db_target_cnt import TargetCnt
from models.directory.money_currency import Money


class Target(Base):
    __tablename__ = "targets"
    target_id_type = Integer()
    target_id = Column(target_id_type, primary_key=True,
                       autoincrement=True)
    target_cnt_id = Column(TargetCnt.target_cnt_id_type,
                           ForeignKey(TargetCnt.target_cnt_id))
    user_login = Column(User.user_login_type, ForeignKey(User.login))
    value = Column(Numeric(precision=8))
    currency = Column(CurrencyType)
    cr_date = Column(DateTime(timezone=True), server_default=func.now())
    upd_date = Column(DateTime(timezone=True), onupdate=func.now())

    target_money = composite(Money, value, currency)
