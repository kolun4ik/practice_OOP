import unittest
from modules.pairs import sum_pairs


class TestSumPairsFunction(unittest.TestCase):
    """Tesing function who returns  sum pair value"""

    def test_sum_list_1(self):
        pairs = [1, 4, 8, 7, 3, 15]
        self.assertEqual(sum_pairs(pairs, 8), [1, 7])

    def test_sum_list_2(self):
        pairs = [1, -2, 3, 0, -6, 1]
        self.assertEqual(sum_pairs(pairs, -6), [0, -6])

    def test_sum_list_3(self):
        pairs = [20, -13, 40]
        self.assertEqual(sum_pairs(pairs, -7), None)

    def test_sum_list_4(self):
        pairs = [1, 2, 3, 4, 1, 0]
        self.assertEqual(sum_pairs(pairs, 2), [1, 1])

    def test_sum_list_5(self):
        pairs = [10, 5, 2, 3, 7, 5]
        self.assertEqual(sum_pairs(pairs, 10), [3, 7])


if __name__ == '__main__':
    unittest.main()
