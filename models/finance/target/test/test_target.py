import unittest
from decimal import Decimal

from models import TargetService
from models.finance.valid_schemas.target_valid import TrgIn, TrgOut


class TargetTest(unittest.TestCase):

    # ToDo generate test id in runtime
    TEST_USER = "TEST_USER1"
    TEST_TRG_CNT_ID = 21

    @classmethod
    def __prepare_trg(cls):
        trg_in = TrgIn(target_cnt_id=cls.TEST_TRG_CNT_ID,
                       user_login=cls.TEST_USER,
                       value=Decimal(10000.00),
                       currency="RUB")
        service = TargetService.build_service()
        trg_out: TrgOut = service.create(trg_in)
        return trg_out.target_id

    @classmethod
    def setUpClass(cls):
        cls.test_trg_id = cls.__prepare_trg()

    def test_something(self):
        service = TargetService.build_service()
        trg = service.read(self.test_trg_id)
        self.assertEqual(trg.target_id, self.test_trg_id)


if __name__ == '__main__':
    unittest.main()
