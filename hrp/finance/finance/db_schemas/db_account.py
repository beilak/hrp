from sqlalchemy import String, Column, ForeignKey, DateTime, func, Integer

from hrp.db.db_conn import Base
from models.directory.db_acc_type import AccType
from models.org import Unit
from models.org import User


class Account(Base):
    __tablename__ = "accounts"
    account_id_type = Integer()

    acc_id = Column(account_id_type, primary_key=True, autoincrement=True)
    acc_type = Column(AccType.acc_type_id_type, ForeignKey("acc_types.acc_type_id"), nullable=False)
    acc_number = Column(String(32), nullable=True)
    description = Column(String(32))
    bank = Column(String(32))
    unit_id = Column(Unit.unit_id_type, ForeignKey("units.unit_id"), nullable=False)
    user_login = Column(User.user_login_type, ForeignKey("users.login"), nullable=False)
    cr_date = Column(DateTime(timezone=True), server_default=func.now())
    upd_date = Column(DateTime(timezone=True), onupdate=func.now())
