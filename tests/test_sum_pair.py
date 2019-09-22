import unittest
from modules.pairs import sum_pairs


class TestSumPairsFunction(unittest.TestCase):
    """Tesing function who returns  sum pair value"""

    def test_sum_list_1(self):
        l = [1, 4, 8, 7, 3, 15]
        self.assertEqual(sum_pairs(l, 8), [1, 7])

    def test_sum_list_2(self):
        l = [1, -2, 3, 0, -6, 1]
        self.assertEqual(sum_pairs(l, -6), [0, -6])

    def test_sum_list_3(self):
        l = [20, -13, 40]
        self.assertEqual(sum_pairs(l, -7), None)

    def test_sum_list_4(self):
        l = [1, 2, 3, 4, 1, 0]
        self.assertEqual(sum_pairs(l, 2), [1, 1])

    def test_sum_list_5(self):
        l = [10, 5, 2, 3, 7, 5]
        print(sum_pairs(l, 10))
        self.assertEqual(sum_pairs(l, 10), [3, 7])

# l5= [10, 5, 2, 3, 7, 5]
# l6= [4, -2, 3, 3, 4]
# l7= [0, 2, 0]
# l8= [5, 9, 13, -3]
#
#
# test.expect(sum_pairs(l5, 10) == [3, 7], "First Match From Left REDUX!: %s should return [3, 7] for sum = 10 " % l5)
# test.expect(sum_pairs(l6, 8) == [4, 4], "Duplicates: %s should return [4, 4] for sum = 8" % l6)
# test.expect(sum_pairs(l7, 0) == [0, 0], "Zeroes: %s should return [0, 0] for sum = 0" % l7)
# test.expect(sum_pairs(l8, 10) == [13, -3], "Subtraction: %s should return [13, -3] for sum = 10" % l8)



if __name__ == '__main__':
    unittest.main()
