from models.db.db_conn import DBConn


class Collection:

    @classmethod
    def _insert_db(cls, objects: set):
        DBConn.insert(objects)
