import unittest
from fastapi.testclient import TestClient
from fastapi import status
from web_server.hrp_server import hrp_api
import datetime


class HRPWebServerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.TEST_USER = "TEST_USER1"
        cls.TEST_UNIT = "test_unit_id_1"
        cls.client = TestClient(hrp_api)

    def test_get_users(self):
        response = self.client.get("/users/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user(self):
        link = "/users/{}".format(self.TEST_USER)
        response = self.client.get(link)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_login = response.json()['login']
        self.assertEqual(response_login, self.TEST_USER)

    def test_create_user(self):
        new_user_login = "TEST_USR_WEB_{}".format(str(datetime.datetime.now().hour) +
                                                  str(datetime.datetime.now().minute) +
                                                  str(datetime.datetime.now().microsecond))
        response = self.client.post("/users/",
                                    json={"login": new_user_login, "first_name": "First",
                                          "last_name": "Last", "password": "TestPass",
                                          "email": "test@test.ru"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=response.text)
        response_login = response.json()['login']
        self.assertEqual(response_login, new_user_login)

    def test_update_user(self):
        # ToDo Add test after implemented service method
        pass

    def test_create_unit(self):
        new_unit_id = "TEST_UNIT{}".format(str(datetime.datetime.now().hour) +
                                           str(datetime.datetime.now().minute) +
                                           str(datetime.datetime.now().microsecond))
        response = self.client.post("/units/",
                                    json={"unit_id": new_unit_id, "description": "Unit desc",
                                          "admin": self.TEST_USER,
                                          "join_pass": "UnitTestPass"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=response.text)
        response_unit_id = response.json()['unit_id']
        self.assertEqual(response_unit_id, new_unit_id)

    def test_get_units(self):
        response = self.client.get("/units/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_unit(self):
        response = self.client.get("/units/{}".format(self.TEST_UNIT))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_unit_id = response.json()["unit_id"]
        self.assertEqual(response_unit_id, self.TEST_UNIT)

    def test_user_join_to_unit(self):
        new_unit_id = "TEST_UNIT{}".format(str(datetime.datetime.now().hour) +
                                           str(datetime.datetime.now().minute) +
                                           str(datetime.datetime.now().microsecond))
        response = self.client.post("/units/",
                                    json={"unit_id": new_unit_id, "description": "Unit desc",
                                          "admin": self.TEST_USER,
                                          "join_pass": "UnitTestPass"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=response.text)
        response_unit_id = response.json()['unit_id']

        response = self.client.put("/users/{}/join_to_unit".format(self.TEST_USER),
                                   json={"login": self.TEST_USER,
                                         "unit_id": response_unit_id})
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.text)
        response_login = response.json()["login"]
        self.assertEqual(response_login, self.TEST_USER)
        is_unit_joined = False
        for item in response.json()["units"]:
            if self.TEST_UNIT == item["unit_id"]:
                is_unit_joined = True
                break
        self.assertTrue(is_unit_joined)

    def test_get_unit_users(self):
        response = self.client.get("/units/{}/users".format(self.TEST_USER))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


if __name__ == '__main__':
    unittest.main()
