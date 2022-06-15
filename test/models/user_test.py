import unittest
from models.user import Users, User
from models.unit import Unit


class UserTestCase(unittest.TestCase):
    def test_creating_user(self):
        users = Users()
        user: User = users.create(user_id="Test_user_1", unit_id="TEST_UNIT",
                                  first_name="Test_name", last_name="Test_last_name")
        is_user_created = False if user is None else True
        self.assertEqual(is_user_created, True)  # add assertion here

    def test_save_user(self):
        users = Users()
        saved_user = users.insert()
        is_user_saved = False
        for item in saved_user:
            is_user_saved = False if item is None else True
            if item is None:
                break
        self.assertEqual(is_user_saved, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
