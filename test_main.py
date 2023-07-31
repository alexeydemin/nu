from main import CapitalGains
import unittest


class TestCapitalGains(unittest.TestCase):
    def setUp(self):
        self.cg = CapitalGains()

    def test_get_result_1(self):
        case1_res = self.cg.get_result('[{"operation":"buy", "unit-cost":10.00, "quantity": 100}, {"operation":"sell", "unit-cost":15.00, "quantity": 50}, {"operation":"sell", "unit-cost":15.00, "quantity": 50}]')
        self.assertEqual(case1_res, '[{"tax": 0.00},{"tax": 0.00},{"tax": 0.00}]')

    def test_get_result_2(self):
        case2_res = self.cg.get_result('[{"operation":"buy", "unit-cost":10.00, "quantity": 10000}, {"operation":"sell", "unit-cost":20.00, "quantity": 5000}, {"operation":"sell", "unit-cost":5.00, "quantity": 5000}]')
        self.assertEqual(case2_res, '[{"tax": 0.00},{"tax": 10000.00},{"tax": 0.00}]')

    def test_get_result_3(self):
        case3_res = self.cg.get_result('[{"operation":"buy", "unit-cost":10.00, "quantity": 10000}, {"operation":"sell", "unit-cost":5.00, "quantity": 5000}, {"operation":"sell", "unit-cost":20.00, "quantity": 3000}]')
        self.assertEqual(case3_res, '[{"tax": 0.00},{"tax": 0.00},{"tax": 1000.00}]')

    def test_get_result_4(self):
        case4_res = self.cg.get_result('[{"operation":"buy", "unit-cost":10.00, "quantity": 10000}, {"operation":"buy", "unit-cost":25.00, "quantity": 5000}, {"operation":"sell", "unit-cost":15.00, "quantity": 10000}]')
        self.assertEqual(case4_res, '[{"tax": 0.00},{"tax": 0.00},{"tax": 0.00}]')

    def test_get_result_5(self):
        case5_res = self.cg.get_result('[{"operation":"buy", "unit-cost":10.00, "quantity": 10000}, {"operation":"buy", "unit-cost":25.00, "quantity": 5000}, {"operation":"sell", "unit-cost":15.00, "quantity": 10000}, {"operation":"sell", "unit-cost":25.00, "quantity": 5000}]')
        self.assertEqual(case5_res, '[{"tax": 0.00},{"tax": 0.00},{"tax": 0.00},{"tax": 10000.00}]')

    def test_get_result_6(self):
        case6_res = self.cg.get_result('[{"operation":"buy", "unit-cost":10.00, "quantity": 10000},{"operation":"sell", "unit-cost":2.00, "quantity": 5000},{"operation":"sell", "unit-cost":20.00, "quantity": 2000},{"operation":"sell", "unit-cost":20.00, "quantity": 2000},{"operation":"sell", "unit-cost":25.00, "quantity": 1000}]')
        self.assertEqual(case6_res, '[{"tax": 0.00},{"tax": 0.00},{"tax": 0.00},{"tax": 0.00},{"tax": 3000.00}]')

    def test_get_result_7(self):
        case7_res = self.cg.get_result('[{"operation":"buy", "unit-cost":10.00, "quantity": 10000},{"operation":"sell", "unit-cost":2.00, "quantity": 5000},{"operation":"sell", "unit-cost":20.00, "quantity": 2000},{"operation":"sell", "unit-cost":20.00, "quantity": 2000},{"operation":"sell", "unit-cost":25.00, "quantity": 1000},{"operation":"buy", "unit-cost":20.00, "quantity": 10000},{"operation":"sell", "unit-cost":15.00, "quantity": 5000},{"operation":"sell", "unit-cost":30.00, "quantity": 4350},{"operation":"sell", "unit-cost":30.00, "quantity": 650}]')
        self.assertEqual(case7_res, '[{"tax": 0.00},{"tax": 0.00},{"tax": 0.00},{"tax": 0.00},{"tax": 3000.00},{"tax": 0.00},{"tax": 0.00},{"tax": 3700.00},{"tax": 0.00}]')

    def test_get_result_8(self):
        case8_res = self.cg.get_result('[{"operation":"buy", "unit-cost":10.00, "quantity": 10000},{"operation":"sell", "unit-cost":50.00, "quantity": 10000},{"operation":"buy", "unit-cost":20.00, "quantity": 10000},{"operation":"sell", "unit-cost":50.00, "quantity": 10000}]')
        self.assertEqual(case8_res, '[{"tax": 0.00},{"tax": 80000.00},{"tax": 0.00},{"tax": 60000.00}]')