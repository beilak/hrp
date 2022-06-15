import unittest
from models.unit import Unit


class UnitTestCase(unittest.TestCase):
    TEST_UNIT_ID = "TEST_UNIT"
    TEST_UNIT_NAME = "Test unit"

    def test_create_unit(self):
        unit = Unit.create_unit(self.TEST_UNIT_ID, self.TEST_UNIT_NAME)
        is_created = False if unit is None else True
        self.assertEqual(is_created, True)

    def test_get_unit(self):
        print(Unit.get_unit(self.TEST_UNIT_ID))


if __name__ == '__main__':
    unittest.main()
