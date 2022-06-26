from sqlalchemy import Column, ForeignKey, DateTime, func, Numeric, Integer, String
from sqlalchemy.orm import composite
from sqlalchemy_utils.types.currency import CurrencyType

from db.db_conn import Base
from models.directory.money_currency import Money
from models.org.user import User
from models.org.unit import Unit


class RealEstate(Base):
    """
    Tables storage real estate.
    city and address could be Null (privacy reason)
    # ToDo add reference to credits
    """

    __tablename__ = "real_estates"
    real_estate_id_type = Integer()

    real_estate_id = Column(real_estate_id_type, primary_key=True, autoincrement=True)
    name = Column(String(32))
    unit_id = Column(Unit.unit_id_type, ForeignKey("units.unit_id"), nullable=False)
    user_login = Column(User.user_login_type, ForeignKey("users.login"), nullable=False)
    city = Column(String(32), nullable=True)
    address = Column(String(32), nullable=True)
    price = Column(Numeric(precision=8))
    currency = Column(CurrencyType)
    cr_date = Column(DateTime(timezone=True), server_default=func.now())
    upd_date = Column(DateTime(timezone=True), onupdate=func.now())

    item_cost = composite(Money, price, currency)
