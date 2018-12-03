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

    def test_part_1(self):

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

    def test_part_2(self):

        test_data = [
            'abcde',
            'fghij',
            'klmno',
            'pqrst',
            'fguij',
            'axcye',
            'wvxyz'
        ]

        self.assertEqual(week1.day2_part2(test_data), 'fgij')


class TestDay3(TestCase):


    def test_parser(self):

        test_data = ["#1 @ 1,3: 4x4"]
        self.assertListEqual(
            week1.day3.day3_parser(test_data),
            [
                {
                    "id": "1",
                    "left_start": 1,
                    "top_start": 3,
                    "width": 4,
                    "height": 4
                }
            ]
        )


    def test_part_1(self):

        test_data = [
            "#1 @ 1,3: 4x4",
            "#2 @ 3,1: 4x4",
            "#3 @ 5,5: 2x2"
        ]

        self.assertEqual(week1.day3_part1(test_data), 4)



if __name__ == '__main__':
    main()
