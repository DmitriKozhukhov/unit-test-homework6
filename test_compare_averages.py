import unittest

from compare_averages import CompareAverages


class TestCompareAverages(unittest.TestCase):
    def test_first_average_is_more(self):
        self.assertEqual(CompareAverages.compare_averages(7.5, 5), "Первый список имеет большее среднее значение")

    def test_second_average_is_more(self):
        self.assertEqual(CompareAverages.compare_averages(3, 5), "Второй список имеет большее среднее значение")

    def test_averags_are_equal(self):
        self.assertEqual(CompareAverages.compare_averages(3, 3), "Средние значения равны")
