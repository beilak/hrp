from sqlalchemy import String, Column

from db.db_conn import Base


class AccType(Base):
    __tablename__ = "acc_types"
    acc_type_id_type = String(17)

    acc_type_id = Column(acc_type_id_type, primary_key=True)
    name = Column(String(32))
