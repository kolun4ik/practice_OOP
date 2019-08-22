import unittest
from modules.fraction import Fraction
from unittest import skip


class FractionsLtMethodTests(unittest.TestCase):
    """Тестируем действия с дробями: дробь1 < дробь 2 """

    def setUp(self):
        self.A = Fraction(1, 3)
        self.B = Fraction(2, 3)

    def test_first_fr_lt_second_fr(self):
        """тест: первая дробь меньше второй"""
        self.assertTrue(self.A.__lt__(self.B))

    def test_first_fr_not_gt_second_fr(self):
        """тест: первая дробь не больше второй"""
        self.assertFalse(self.B.__lt__(self.A))


class FractionsLeMethodTests(unittest.TestCase):
    """Тестируем действия с дробями: дробь1 <= дробь 2 """

    def setUp(self):
        self.A = Fraction(1, 3)
        self.B = Fraction(2, 3)

    def test_first_fr_ge_second_fr(self):
        """тест: первая дробь меньше второй"""
        self.assertTrue(self.A < self.B)

    def test_first_fr_equal_second_fr(self):
        """тест: первая дробь эквивалентна второй"""
        F = Fraction(2, 3)
        self.assertTrue(self.A <= F)

    def test_first_fr_not_ge_second_fr(self):
        """тест: вторая дробь не меньше превой"""
        self.assertFalse(self.B < self.A)




if "__name__" == "__main__":
    unittest.main()