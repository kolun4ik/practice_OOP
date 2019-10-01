import unittest
from modules.pairs import sum_pairs
from unittest import skip


class TestSumPairsFunction(unittest.TestCase):
    """Tesing function who returns  sum pair value"""

    def test_sum_list_1(self):
        pairs = [1, 4, 8, 7, 3, 15]
        self.assertEqual(sum_pairs(pairs, 8), [1, 7])

    # @skip('test')
    def test_sum_list_2(self):
        pairs = [1, -2, 3, 0, -6, 1]
        self.assertEqual(sum_pairs(pairs, -6), [0, -6])

    # @skip('test')
    def test_sum_list_3(self):
        pairs = [20, -13, 40]
        self.assertEqual(sum_pairs(pairs, -7), None)

    # @skip('test')
    def test_sum_list_4(self):
        pairs = [1, 2, 3, 4, 1, 0]
        self.assertEqual(sum_pairs(pairs, 2), [1, 1])

    # @skip('test')
    def test_sum_list_5(self):
        pairs = [10, 5, 2, 3, 7, 5]
        self.assertEqual(sum_pairs(pairs, 10), [3, 7])

    # @skip('test')
    def test_sum_list_6(self):
        pairs = [4, -2, 3, 3, 4]
        self.assertEqual(sum_pairs(pairs, 8), [4, 4])


if __name__ == '__main__':
    unittest.main()
