from sqlalchemy import String, Column, ForeignKey, DateTime, func, Integer
from sqlalchemy_utils.types.currency import CurrencyType

from hrp.db.db_conn import Base
from models.finance.db_schemas.db_account import Account
from models.org import Unit


class ProfitCnt(Base):
    """
    DB object. Profits Center
    """
    __tablename__ = "profits_cnt"
    profit_cnt_id_type = Integer()
    profit_cnt_id = Column(profit_cnt_id_type, primary_key=True,
                           autoincrement=True)
    unit_id = Column(Unit.unit_id_type,
                     ForeignKey(Unit.unit_id))
    name = Column(String(32))
    description = Column(String(128))
    account_id = Column(Account.account_id_type,
                        ForeignKey(Account.acc_id))
    currency = Column(CurrencyType)
    cr_date = Column(DateTime(timezone=True), server_default=func.now())
    upd_date = Column(DateTime(timezone=True), onupdate=func.now())
