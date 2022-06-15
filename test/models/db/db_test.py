import unittest
from models.db.db_conn import DBConn


class MyTestCase(unittest.TestCase):

    def test_get_db_connect(self):
        db_engine = DBConn.get_db_connect()
        print(db_engine)
        self.assertEqual(True, True)  # add assertion here

    def test_db_connect(self):
        db_connect = DBConn.db_connect()
        self.assertEqual(True, db_connect, db_connect)  # add assertion here


if __name__ == '__main__':
    unittest.main()
