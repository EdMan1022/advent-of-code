from unittest import TestCase

from src.main.week1 import day2


class TestDay2(TestCase):

    def test_ex_1(self):
        test_data = [1, -1]
        self.assertEqual(day2(test_data), 0)
    
    def test_ex_2(self):
        test_data = [3, 3, 4, -2, -4]
        self.assertEqual(day2(test_data), 10)

    def test_ex_3(self):
        test_data = [-6, 3, 8, 5, -6]
        self.assertEqual(day2(test_data), 5)

    def test_ex_4(self):
        test_data = [7, 7, -2, -7, -4]
        self.assertEqual(day2(test_data), 14)
