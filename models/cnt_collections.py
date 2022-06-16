from models.db.db_conn import DBConn


class CntCollections:
    cnt_collections_obj = None

    def __init__(self):
        self._new_cnt = set()
        self._exist_cnt = set()

    def insert(self):
        return DBConn.insert(self._new_cnt)

