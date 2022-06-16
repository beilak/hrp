import unittest
from models.unit import UnitCollections, Unit


class UnitTestCase(unittest.TestCase):
    TEST_UNIT_ID = "TEST_UNIT"
    TEST_UNIT_NAME = "Test unit"
    TEST_UNIT_ADMIN = "beilak"

    def test_create_unit(self):
        unit: Unit = UnitCollections.create_unit(unit_id=self.TEST_UNIT_ID, name=self.TEST_UNIT_NAME,
                                                 admin=self.TEST_UNIT_ADMIN)
        is_created = False if unit is None else True
        self.assertEqual(is_created, True)

    def test_get_unit(self):
        print(Unit.get_unit(self.TEST_UNIT_ID))


if __name__ == '__main__':
    unittest.main()
