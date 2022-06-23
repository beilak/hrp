from sqlalchemy import Column, ForeignKey, DateTime, func, Numeric, Integer
from sqlalchemy.orm import composite
from sqlalchemy_utils.types.currency import CurrencyType

from db.db_conn import Base
from models.directory.money_currency import Money
from models.finance.db_schemas.db_profit_cnt import ProfitCnt
from models.org.user import User


class Profit(Base):
    """
    DB object. Profits
    """
    __tablename__ = "profits"
    profit_id_type = Integer()
    profit_id = Column(profit_id_type, primary_key=True,
                       autoincrement=True)
    profit_cnt_id = Column(ProfitCnt.profit_cnt_id_type,
                           ForeignKey(ProfitCnt.profit_cnt_id))
    user_login = Column(User.user_login_type, ForeignKey(User.login))
    value = Column(Numeric(precision=8))
    currency = Column(CurrencyType)
    cr_date = Column(DateTime(timezone=True), server_default=func.now())
    upd_date = Column(DateTime(timezone=True), onupdate=func.now())

    profit_money = composite(Money, value, currency)
