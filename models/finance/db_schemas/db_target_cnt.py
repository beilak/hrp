from sqlalchemy import String, Column, ForeignKey, DateTime, func, Numeric, Integer
from sqlalchemy.orm import composite
from sqlalchemy_utils.types.currency import CurrencyType

from db.db_conn import Base
from models.directory.money_currency import Money
from models.finance.db_schemas.db_account import Account
from models.org.unit import Unit


class TargetCnt(Base):
    __tablename__ = "targets_cnt"
    target_cnt_id_type = Integer()
    target_cnt_id = Column(target_cnt_id_type, primary_key=True, autoincrement=True)
    unit_id = Column(Unit.unit_id_type, ForeignKey(Unit.unit_id))
    name = Column(String(32))
    description = Column(String(128))
    account_id = Column(Account.account_id_type, ForeignKey(Account.acc_id))
    value = Column(Numeric(precision=8))
    currency = Column(CurrencyType)
    init_value = Column(Numeric(precision=8))
    init_currency = Column(CurrencyType)
    cr_date = Column(DateTime(timezone=True), server_default=func.now())
    upd_date = Column(DateTime(timezone=True), onupdate=func.now())

    target_money = composite(Money, value, currency)
    init_money = composite(Money, init_value, init_currency)
