import unittest
from fastapi.testclient import TestClient
from fastapi import status
from web_server import hrp_api
import datetime

# ToDo Optimize test (reformat prepare to test)


class HRPWebServerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        test_user = "TEST_USER1"
        cls.TEST_USER = test_user
        test_unit = "test_unit_id_1"
        cls.TEST_UNIT = test_unit
        test_debit_number = "010203040506070809"
        cls.TEST_DEBIT_ACC_NUMBER = "010203040506070809"
        client = TestClient(hrp_api)
        cls.client = client

        client.post("/users/",
                    json={"login": test_user, "first_name": "First",
                          "last_name": "Last", "password": "TestPass",
                          "email": "test@test.ru"})
        client.post("/units/",
                    json={"unit_id": test_unit, "description": "Unit desc",
                          "admin": test_user,
                          "join_pass": "UnitTestPass"})
        client.put("/users/{}/join_to_unit".format(test_user),
                   json={"login": test_user,
                         "unit_id": test_unit})

        response = client.post("/units/" + test_unit + "/account",
                               json={"acc_number": test_debit_number,
                                     "unit_id": test_unit,
                                     "user_login": test_user,
                                     "acc_type": "DEBIT_CARD",
                                     "description": "",
                                     "bank": ""})
        if 'acc_id' in response.json():
            test_acc_id = response.json()['acc_id']
            cls.TEST_ACC_ID = int(test_acc_id)

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
            if new_unit_id == item["unit_id"]:
                is_unit_joined = True
                break
        self.assertTrue(is_unit_joined)

    def test_get_unit_users(self):
        response = self.client.get("/units/{}/users".format(self.TEST_UNIT))
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.text)

    """ { TEST Account"""

    def test_create_debit_acc(self):
        response = self.client.post("/units/" + self.TEST_UNIT + "/account",
                                    json={"acc_number": self.TEST_DEBIT_ACC_NUMBER,
                                          "unit_id": self.TEST_UNIT,
                                          "user_login": self.TEST_USER,
                                          "acc_type": "DEBIT_CARD",
                                          "description": "Зарплатная карта",
                                          "bank": "Тенькофф"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=response.text)
        response_acc_num = response.json()['acc_number']
        self.assertEqual(response_acc_num, self.TEST_DEBIT_ACC_NUMBER)
        response_acc_id = response.json()['acc_id']
        self.assertIsNotNone(response_acc_id)

    def test_create_chase_acc(self):
        response = self.client.post("/units/" + self.TEST_UNIT + "/account",
                                    json={"unit_id": self.TEST_UNIT,
                                          "user_login": self.TEST_USER,
                                          "acc_type": "CHASE",
                                          "description": "Наличка",
                                          "bank": "Тенькофф"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=response.text)
        response_acc_num = response.json()['acc_number']
        self.assertIsNone(response_acc_num)
        response_acc_id = response.json()['acc_id']
        self.assertIsNotNone(response_acc_id)

    def test_get_accounts(self):
        response = self.client.get("/units/{}/account".format(self.TEST_UNIT))
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.text)

    def __post_new_acc(self, unit, user, acc_type, description):
        return self.client.post("/units/" + unit + "/account",
                                json={"unit_id": unit,
                                      "user_login": user,
                                      "acc_type": acc_type,
                                      "description": description,
                                      "bank": "Тенькофф"})

    def test_get_account(self):
        response = self.__post_new_acc(self.TEST_UNIT, self.TEST_USER,
                                       "CHASE", "description")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=response.text)
        acc_id = response.json()['acc_id']

        response = self.client.get("/units/{}/account/{}".format(self.TEST_UNIT, acc_id))
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.text)
        response_acc_id = response.json()['acc_id']
        self.assertEqual(response_acc_id, acc_id)

    """ }"""

    """ { TEST Target Center endpoint """

    def __post_target_cnt(self, unit, account_id, init_value="100_000.00", init_currency="USD",
                          name="Test target Name", description="description target cnt",
                          value="100_000.00", currency="USD"):
        return self.client.post("/units/" + unit + "/target_cnt",
                                json={"unit_id": unit, "name": name, "description": description,
                                      "account_id": account_id,
                                      "value": value, "currency": currency,
                                      "init_value": init_value, "init_currency": init_currency})

    def test_create_target_cnt(self):
        response = self.__post_new_acc(self.TEST_UNIT, self.TEST_USER,
                                       "CHASE", "description")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=response.text)
        acc_id = response.json()['acc_id']
        response = self.__post_target_cnt(unit=self.TEST_UNIT, account_id=acc_id)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=response.text)
        response_target_cnt_id = response.json()['target_cnt_id']
        self.assertIsNotNone(response_target_cnt_id, msg=response.text)

    def __prepare_target_cnt(self):
        response = self.__post_new_acc(self.TEST_UNIT, self.TEST_USER,
                                       "CHASE", "description")
        acc_id = response.json()['acc_id']
        response = self.__post_target_cnt(unit=self.TEST_UNIT, account_id=acc_id)
        return response.json()['target_cnt_id'], self.TEST_UNIT

    def test_get_targets_cnt(self):
        target_cnt_id, unit_id = self.__prepare_target_cnt()
        resource = self.client.get("/units/{}/target_cnt".format(unit_id))
        self.assertEqual(resource.status_code, status.HTTP_200_OK, msg=resource.text)

    def test_get_target_cnt(self):
        target_cnt_id, unit_id = self.__prepare_target_cnt()
        resource = self.client.get("/units/{}/target_cnt/{}".format(unit_id, target_cnt_id))
        self.assertEqual(resource.status_code, status.HTTP_200_OK, msg=resource.text)
        resource_trg_cnt_id = resource.json()["target_cnt_id"]
        self.assertEqual(resource_trg_cnt_id, target_cnt_id, msg=resource.text)

    """ } """

    """ TEST Target endpoint """

    def __prepare_target_crt_test(self):
        response = self.__post_new_acc(self.TEST_UNIT, self.TEST_USER,
                                       "CHASE", "description")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=response.text)
        acc_id = response.json()['acc_id']
        response = self.__post_target_cnt(unit=self.TEST_UNIT, account_id=acc_id)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=response.text)
        response_target_cnt_id = response.json()['target_cnt_id']
        self.assertIsNotNone(response_target_cnt_id, msg=response.text)
        return self.TEST_UNIT, self.TEST_USER, acc_id, response_target_cnt_id

    def __create_target(self, unit, target_cnt_id, user):
        link = "/units/{}/target".format(unit)
        return self.client.post(link,
                                json={"target_cnt_id": target_cnt_id,
                                      "user_login": user,
                                      "value": "100.00",
                                      "currency": "RUB"})

    def test_create_target(self):
        unit, user, acc_id, target_cnt_id = self.__prepare_target_crt_test()
        response = self.__create_target(unit, target_cnt_id, user)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=response.text)
        response_target_id = response.json()['target_id']
        self.assertIsNotNone(response_target_id, msg=response.text)

    def __prepare_read_target(self):
        unit, user, acc_id, target_cnt_id = self.__prepare_target_crt_test()
        response = self.__create_target(unit, target_cnt_id, user)
        target_id = response.json()['target_id']
        return unit, target_id

    def test_get_target(self):
        unit, target_id = self.__prepare_read_target()
        link = "/units/{}/target/{}".format(unit, target_id)
        response = self.client.get(link)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.text)
        resp_target_id = response.json()['target_id']
        self.assertEqual(resp_target_id, target_id, msg=response.text)

    def test_get_targets(self):
        unit, target_id = self.__prepare_read_target()
        link = "/units/{}/target".format(unit)
        response = self.client.get(link)
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         msg=response.text)
        is_test_trg_got = False
        for i in response.json():
            if i["target_id"] == target_id:
                is_test_trg_got = True
        self.assertTrue(is_test_trg_got, msg=response.text)

    """ """
    def __create_profit_cnt(self, unit, user, acc_id):
        link = "/units/{}/profit_cnt".format(unit)
        return self.client.post(link,
                                json={"unit_id": unit,
                                      "name": user,
                                      "description": "desc",
                                      "account_id": acc_id,
                                      "currency": "RUB"})

    def test_create_profit_cnt(self):
        response = self.__create_profit_cnt(self.TEST_UNIT, self.TEST_USER,
                                            self.TEST_ACC_ID)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=response.text)
        profit_cnt_id = response.json()['profit_cnt_id']
        self.assertIsNotNone(profit_cnt_id, msg=response.text)

    def __prepare_read_profit_cnt(self):
        response = self.__create_profit_cnt(self.TEST_UNIT, self.TEST_USER,
                                            self.TEST_ACC_ID)
        profit_cnt_id = response.json()['profit_cnt_id']
        return self.TEST_UNIT, profit_cnt_id

    def test_get_profit_cnt(self):
        unit, profit_cnt_id = self.__prepare_read_profit_cnt()
        link = "/units/{}/profit_cnt/{}".format(unit, profit_cnt_id)
        response = self.client.get(link)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.text)
        resp_profit_cnt_id = response.json()['profit_cnt_id']
        self.assertEqual(resp_profit_cnt_id, profit_cnt_id, msg=response.text)

    def test_get_profits_cnt(self):
        unit, profit_cnt_id = self.__prepare_read_profit_cnt()
        link = "/units/{}/profit_cnt".format(unit)
        response = self.client.get(link)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.text)
        is_profit_cnt_got = False
        for i in response.json():
            if profit_cnt_id == i['profit_cnt_id']:
                is_profit_cnt_got = True
        self.assertTrue(is_profit_cnt_got, msg=response.text)













    """ """
    def __create_profit(self, unit, profit_cnt_id, user):
        link = "/units/{}/profit".format(unit)
        return self.client.post(link,
                                json={"profit_cnt_id": profit_cnt_id, "user_login": user,
                                      "value": "100.00", "currency": "RUB"})

    def test_create_profit(self):
        unit, profit_cnt_id = self.__prepare_read_profit_cnt()
        response = self.__create_profit(unit, profit_cnt_id, self.TEST_USER)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=response.text)
        profit_id = response.json()['profit_id']
        self.assertIsNotNone(profit_id, msg=response.text)

    def __prepare_read_profit(self):
        unit, profit_cnt_id = self.__prepare_read_profit_cnt()
        response = self.__create_profit(unit, profit_cnt_id, self.TEST_USER)
        profit_id = response.json()['profit_id']
        return unit, profit_id

    def test_get_profit(self):
        unit, profit_id = self.__prepare_read_profit()

        link = "/units/{}/profit/{}".format(unit, profit_id)
        response = self.client.get(link)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.text)
        resp_profit_id = response.json()['profit_id']
        self.assertEqual(resp_profit_id, profit_id, msg=response.text)

    def test_get_profits(self):
        unit, profit_id = self.__prepare_read_profit()
        link = "/units/{}/profit".format(unit)
        response = self.client.get(link)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.text)
        is_profit_got = False
        for i in response.json():
            if profit_id == i['profit_id']:
                is_profit_got = True
        self.assertTrue(is_profit_got, msg=response.text)


if __name__ == '__main__':
    unittest.main()
