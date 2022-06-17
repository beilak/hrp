import unittest
from unittest import TestSuite

from models.db.test.test_db import DBTest
from models.org.test.test_user import UserTest
from models.org.test.test_unit import UnitTest
from web_server.test.test_hrp_server import HRPWebServerTest


def load_tests(loader, tests, pattern):
    tests_class = {DBTest, UserTest, UnitTest, HRPWebServerTest}
    suite = TestSuite()
    for test_class in tests_class:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    return suite


unittest.main(verbosity=2)
