from sqlalchemy import Column, String
from hrp.db.db_conn import Base


class Measure(Base):
    """
    Tables storage assets.
    # ToDo add reference to credits
    """

    __tablename__ = "measures"
    id_type = String(12)
    measure_id = Column(id_type, primary_key=True)
    name = Column(String(32))
