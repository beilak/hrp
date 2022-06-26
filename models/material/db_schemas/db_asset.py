from sqlalchemy import (Column, ForeignKey, DateTime,
                        func, Numeric, String, Float, Integer)
from sqlalchemy.orm import composite
from sqlalchemy_utils.types.currency import CurrencyType

from db.db_conn import Base
from models.directory.money_currency import Money
from models.org.user import User
from models.org.unit import Unit
from models.directory.db_measure import Measure


class Asset(Base):
    """
    Tables storage assets.
    # ToDo add reference to credits
    """

    __tablename__ = "assets"
    id_type = Integer()

    asset_id = Column(id_type, primary_key=True, autoincrement=True)
    name = Column(String(32))
    unit_id = Column(Unit.unit_id_type, ForeignKey("units.unit_id"),
                     nullable=False)
    user_login = Column(User.user_login_type, ForeignKey("users.login"),
                        nullable=False)
    count = Column(Float, nullable=False)
    measure = Column(Measure.id_type, ForeignKey("measures.measure_id"),
                     nullable=False)
    price = Column(Numeric(precision=8))
    currency = Column(CurrencyType)
    city = Column(String(32), nullable=True)
    address = Column(String(32), nullable=True)
    cr_date = Column(DateTime(timezone=True), server_default=func.now())
    upd_date = Column(DateTime(timezone=True), onupdate=func.now())

    item_cost = composite(Money, price, currency)
