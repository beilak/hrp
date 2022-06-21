from db.db_conn import DBConn, Base
import models.org as org
import models.finance as finance


def get_table_exist_status():
    tb_obj = {org.User, org.Unit, org.UnitUser, finance.Target, finance.Account, finance.TargetCnt}
    result = dict()
    for obj in tb_obj:
        result[obj] = DBConn.is_table_exist(obj.__tablename__)
    return result


def create_all_tables():
    Base.metadata.create_all(DBConn.get_db_connect())


def drop_all_tables():
    Base.metadata.drop_all(DBConn.get_db_connect())


if __name__ == '__main__':
    drop_all_tables()
    create_all_tables()
