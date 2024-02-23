from average_calc import AverageCalc
import unittest


class TestAverageCalc(unittest.TestCase):
    def test_average_normal_list(self):
        self.assertEqual(AverageCalc.average_calc([1, 2, 3, 4, 5]), 3.0)

    def test_average_empty_list(self):
        self.assertEqual(AverageCalc.average_calc([]), 0)

    def test_average_single_element(self):
        self.assertEqual(AverageCalc.average_calc([7]), 7)

    def test_average_negative_numbers(self):
        self.assertEqual(AverageCalc.average_calc([-1, -2, -3, -4, -5]), -3.0)

    def test_average_mixed_numbers(self):
        self.assertEqual(AverageCalc.average_calc([-1, 2, -3, 4, 5]), 1.4)
