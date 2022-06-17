from sqlalchemy import Integer, Column, String, DateTime, func
from sqlalchemy.orm import relationship
from sqlalchemy_utils import PasswordType, EmailType
from models.db.db_conn import Base
from models.org.db_schemas.unit_user import UnitUser


class User(Base):
    __tablename__ = "users"
    user_id_type = Integer()
    login = Column(String(32), primary_key=True)
    password = Column(PasswordType(schemes=['pbkdf2_sha512']))
    first_name = Column(String(32))
    last_name = Column(String(32))
    email = Column(EmailType)
    cr_date = Column(DateTime(timezone=True), server_default=func.now())
    upd_date = Column(DateTime(timezone=True), onupdate=func.now())
    units = relationship('Unit', secondary=UnitUser, uselist=True,
                         back_populates="users", lazy='joined')
