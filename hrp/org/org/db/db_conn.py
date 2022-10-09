from sqlalchemy import create_engine
from .key_tool import readKeys
import sqlalchemy.exc
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine
from typing import Callable
from contextlib import contextmanager, AbstractContextManager


Base = declarative_base()

# DB = "HRP"
DB_SYS = "postgresql"
DRIVER = "asyncpg"  #"psycopg2"


class DBEngineProvider:
    """DataBase Engine provider"""
    def __init__(self, db_user, db_pwd, db_host, db_port, db_name):
        db_url = f"{DB_SYS}+{DRIVER}://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}"
        self._engine = create_async_engine(db_url, echo=True)

    @property
    def engine(self):
        return self._engine


class ORGDatabase:
    """DataBase Session"""
    def __init__(self, engine_provider: DBEngineProvider):
        self._engine: DBEngineProvider = engine_provider.engine
        self._async_session_factory = sessionmaker(
            self._engine,
            class_=AsyncSession,
            expire_on_commit=False,
        )

    def new_session(self) -> AsyncSession:
        return self._async_session_factory()

#
# class DBConn:
#     _db_engine = None
#
#     @classmethod
#     def get_db_connect(cls):
#         db_user = readKeys(key="hrp", storage="HRP")
#         db_pass = readKeys(key=db_user, storage="HRP")
#         if cls._db_engine is None:
#             cls._db_engine = cls._get_db_engine(host="localhost", user=db_user, password=db_pass)
#         return cls._db_engine
#
#     @classmethod
#     def db_connect(cls):
#         db_engine = cls.get_db_connect()
#         try:
#             db_engine.connect()
#             return True
#         except sqlalchemy.exc.OperationalError as error:
#             return error.code, error.__str__()
#
#     @classmethod
#     def get_new_session(cls) -> Session:
#         session = sessionmaker()
#         session.configure(bind=DBConn.get_db_connect())
#
#         return session()
#
#     @classmethod
#     def is_table_exist(cls, tb_name):
#         engine_provider = cls.get_db_connect()
#         return engine_provider.dialect.has_table(engine_provider.connect(), tb_name)
#
#     @classmethod
#     def insert(cls, tb_obj):
#         with cls.get_new_session() as session:
#             session.add_all(tb_obj)
#             session.commit()
#
#     @classmethod
#     def query(self):
#         pass
