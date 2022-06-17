from sqlalchemy import create_engine
import models.db.key_tool as key_tool
#import psycopg2 import OperationalError
import sqlalchemy.exc
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()

DB = "HRP"
DB_SYS = "postgresql"
DRIVER = "psycopg2"


class DBConn:
    _db_engine = None

    @classmethod
    def _get_db_engine(cls, host, user, password):
        return create_engine(DB_SYS+"+"+DRIVER+"://"+user+":"+password+"@"+host+"/" + DB, future=True, echo=False)

    @classmethod
    def get_db_connect(cls):
        db_user = key_tool.readKeys(key="hrp", storage="HRP")
        db_pass = key_tool.readKeys(key=db_user, storage="HRP")
        if cls._db_engine is None:
            cls._db_engine = cls._get_db_engine(host="localhost", user=db_user, password=db_pass)
        return cls._db_engine

    @classmethod
    def db_connect(cls):
        db_engine = cls.get_db_connect()
        try:
            db_engine.connect()
            return True
        except sqlalchemy.exc.OperationalError as error:
            return error.code, error.__str__()

    @classmethod
    def get_new_session(cls) -> Session:
        session = sessionmaker()
        session.configure(bind=DBConn.get_db_connect())

        return session()

    @classmethod
    def insert(cls, tb_obj):
        with cls.get_new_session() as session:
            session.add_all(tb_obj)
            session.commit()
