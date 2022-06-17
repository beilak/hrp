import unittest
from models.org.unit import UnitCollection
from models.org.db_schemas.unit import Unit
from models.org.pydatic_schemas.schemas import UnitIn
import datetime


class UnitTestCase(unittest.TestCase):
    TEST_UNITS = dict(test_unit_1=UnitIn(unit_id="test_unit_id_1", description="TEST UNIT",
                                         admin="TEST_USER1", join_pass="MyJoinPass"))

    @classmethod
    def setUpClass(cls):
        test_unit = cls.TEST_UNITS["test_unit_1"]
        if UnitCollection.is_unit_exist(test_unit.unit_id) is False:
            UnitCollection.create(test_unit)

    def test_create_unit(self):
        test_unit = self.TEST_UNITS["test_unit_1"]

        while True:
            test_unit.unit_id = "test_unit_id{}".format(str(datetime.datetime.now().microsecond))
            if UnitCollection.is_unit_exist(test_unit.unit_id) is True:
                continue
            break
        unit: Unit = UnitCollection.create(test_unit)
        is_created = False if unit is None else True
        self.assertEqual(is_created, True)


if __name__ == '__main__':
    unittest.main()
