from hrp.db.db_conn import DBConn, Base
import models.org as org
import models.finance.db_schemas as finance_db
import models.material.db_schemas as material_db
import models.directory as directory_db
"""
Setup database tables. (Create/Delete)
"""


def get_table_exist_status():
    tb_obj = {directory_db.AccType, directory_db.Measure,
              org.User, org.Unit, org.UnitUser, finance_db.Account,
              finance_db.TargetCnt, finance_db.Target, finance_db.ProfitCnt, finance_db.Profit,
              material_db.RealEstate}
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
