from main import CapitalGains
import unittest


class TestCapitalGains(unittest.TestCase):
    def setUp(self):
        self.cg = CapitalGains()

    def test_get_result_1(self):
        res = self.cg.get_taxes('[{"operation":"buy", "unit-cost":10.00, "quantity": 100}, {"operation":"sell", "unit-cost":15.00, "quantity": 50}, {"operation":"sell", "unit-cost":15.00, "quantity": 50}]')
        self.assertEqual(res, '[{"tax": 0.00},{"tax": 0.00},{"tax": 0.00}]')

    def test_get_result_2(self):
        res = self.cg.get_taxes('[{"operation":"buy", "unit-cost":10.00, "quantity": 10000}, {"operation":"sell", "unit-cost":20.00, "quantity": 5000}, {"operation":"sell", "unit-cost":5.00, "quantity": 5000}]')
        self.assertEqual(res, '[{"tax": 0.00},{"tax": 10000.00},{"tax": 0.00}]')

    def test_get_result_3(self):
        res = self.cg.get_taxes('[{"operation":"buy", "unit-cost":10.00, "quantity": 10000}, {"operation":"sell", "unit-cost":5.00, "quantity": 5000}, {"operation":"sell", "unit-cost":20.00, "quantity": 3000}]')
        self.assertEqual(res, '[{"tax": 0.00},{"tax": 0.00},{"tax": 1000.00}]')

    def test_get_result_4(self):
        res = self.cg.get_taxes('[{"operation":"buy", "unit-cost":10.00, "quantity": 10000}, {"operation":"buy", "unit-cost":25.00, "quantity": 5000}, {"operation":"sell", "unit-cost":15.00, "quantity": 10000}]')
        self.assertEqual(res, '[{"tax": 0.00},{"tax": 0.00},{"tax": 0.00}]')

    def test_get_result_5(self):
        case5_res = self.cg.get_taxes('[{"operation":"buy", "unit-cost":10.00, "quantity": 10000}, {"operation":"buy", "unit-cost":25.00, "quantity": 5000}, {"operation":"sell", "unit-cost":15.00, "quantity": 10000}, {"operation":"sell", "unit-cost":25.00, "quantity": 5000}]')
        self.assertEqual(case5_res, '[{"tax": 0.00},{"tax": 0.00},{"tax": 0.00},{"tax": 10000.00}]')

    def test_get_result_6(self):
        res = self.cg.get_taxes('[{"operation":"buy", "unit-cost":10.00, "quantity": 10000},{"operation":"sell", "unit-cost":2.00, "quantity": 5000},{"operation":"sell", "unit-cost":20.00, "quantity": 2000},{"operation":"sell", "unit-cost":20.00, "quantity": 2000},{"operation":"sell", "unit-cost":25.00, "quantity": 1000}]')
        self.assertEqual(res, '[{"tax": 0.00},{"tax": 0.00},{"tax": 0.00},{"tax": 0.00},{"tax": 3000.00}]')

    def test_get_result_7(self):
        res = self.cg.get_taxes('[{"operation":"buy", "unit-cost":10.00, "quantity": 10000},{"operation":"sell", "unit-cost":2.00, "quantity": 5000},{"operation":"sell", "unit-cost":20.00, "quantity": 2000},{"operation":"sell", "unit-cost":20.00, "quantity": 2000},{"operation":"sell", "unit-cost":25.00, "quantity": 1000},{"operation":"buy", "unit-cost":20.00, "quantity": 10000},{"operation":"sell", "unit-cost":15.00, "quantity": 5000},{"operation":"sell", "unit-cost":30.00, "quantity": 4350},{"operation":"sell", "unit-cost":30.00, "quantity": 650}]')
        self.assertEqual(res, '[{"tax": 0.00},{"tax": 0.00},{"tax": 0.00},{"tax": 0.00},{"tax": 3000.00},{"tax": 0.00},{"tax": 0.00},{"tax": 3700.00},{"tax": 0.00}]')

    def test_get_result_8(self):
        res = self.cg.get_taxes('[{"operation":"buy", "unit-cost":10.00, "quantity": 10000},{"operation":"sell", "unit-cost":50.00, "quantity": 10000},{"operation":"buy", "unit-cost":20.00, "quantity": 10000},{"operation":"sell", "unit-cost":50.00, "quantity": 10000}]')
        self.assertEqual(res, '[{"tax": 0.00},{"tax": 80000.00},{"tax": 0.00},{"tax": 60000.00}]')

    def test_get_result_9(self):
        res = self.cg.get_taxes('[{"operation":"buy", "unit-cost": 5000.00, "quantity": 10},{"operation":"sell", "unit-cost": 4000.00, "quantity": 5},{"operation":"buy", "unit-cost": 15000.00, "quantity": 5},{"operation":"buy", "unit-cost": 4000.00, "quantity": 2},{"operation":"buy", "unit-cost": 23000.00, "quantity": 2},{"operation":"sell", "unit-cost": 20000.00, "quantity": 1},{"operation":"sell", "unit-cost": 12000.00, "quantity": 10},{"operation":"sell", "unit-cost": 15000.00, "quantity": 3}]')
        self.assertEqual(res, '[{"tax": 0.00},{"tax": 0.00},{"tax": 0.00},{"tax": 0.00},{"tax": 0.00},{"tax": 0.00},{"tax": 1000.00},{"tax": 2400.00}]')

