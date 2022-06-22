import unittest
from db.db_conn import DBConn
import setup.setup_db as db_stup


class DBTest(unittest.TestCase):

    def test_get_db_connect(self):
        db_engine = DBConn.get_db_connect()
        print(db_engine)
        self.assertEqual(True, True)

    def test_db_connect(self):
        db_connect = DBConn.db_connect()
        self.assertEqual(True, db_connect, db_connect)

    def test_are_tables_created(self):
        table_is_created = db_stup.get_table_exist_status()
        for key, val in table_is_created.items():
            self.assertTrue(val, msg=key)


if __name__ == '__main__':
    unittest.main()
