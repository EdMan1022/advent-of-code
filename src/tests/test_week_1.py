from unittest import TestCase, main

from src.main import week1


class TestDay1(TestCase):

    def test_ex_1(self):
        test_data = [1, -1]
        self.assertEqual(week1.day1(test_data), 0)
    
    def test_ex_2(self):
        test_data = [3, 3, 4, -2, -4]
        self.assertEqual(week1.day1(test_data), 10)

    def test_ex_3(self):
        test_data = [-6, 3, 8, 5, -6]
        self.assertEqual(week1.day1(test_data), 5)

    def test_ex_4(self):
        test_data = [7, 7, -2, -7, -4]
        self.assertEqual(week1.day1(test_data), 14)

class TestDay2(TestCase):

    def test_ex_1(self):

        test_data = [
            'abcdef',
            'bababc',
            'abbcde',
            'abcccd',
            'aabcdd',
            'abcdee',
            'ababab'
            ]
        
        self.assertEqual(week1.day2(test_data), 12)


if __name__ == '__main__':
    main()
