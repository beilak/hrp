import unittest
from models.user import UserCollection, User, UserIn, UserOut
from models.unit import Unit


class UserTestCase(unittest.TestCase):
    TEST_USERS = dict(test_user_1=UserIn(login="TEST_USER1", first_name="Test_name",
                                         last_name="Test_last_name", password="MyPass",
                                         email="test_user@test.ru"))

    @classmethod
    def setUpClass(cls):
        for user in cls.TEST_USERS.values():
            UserCollection.delete_user(user)

    def test_creating_user(self):
        test_user_1 = self.TEST_USERS["test_user_1"]
        user: User = UserCollection.create(test_user_1)

        is_user_created = False if user is None else True
        self.assertEqual(is_user_created, True)  # add assertion here

    def test_get_user(self):
        test_user_1 = self.TEST_USERS["test_user_1"]
        user: User = UserCollection.get_user(test_user_1.login)
        is_user_found = False if user is None else True
        self.assertEqual(is_user_found, True)  # add assertion here

    '''
    def test_create_existing_user(self):
        test_user_1 = self.TEST_USERS["test_user_1"]
        users = UserCollection()
        user: User = users.create(test_user_1)

        is_user_created = False if user is None else True
        self.assertEqual(is_user_created, False)  # add assertion here
    '''


    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
