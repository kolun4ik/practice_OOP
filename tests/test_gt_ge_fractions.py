import unittest
from modules.fraction import Fraction
from unittest import skip


class FractionsGtMethodTests(unittest.TestCase):
    """Тестируем действия с дробями: дробь1 > дробь 2 """

    def setUp(self) -> None:
        self.A = Fraction(2, 3)
        self.B = Fraction(1, 3)

    def test_first_fr_gt_second_fr(self):
        """тест: первая дробь больше второй"""
        self.assertTrue(self.A.__gt__(self.B))

    def test_first_fr_not_gt_second_fr(self):
        """тест: первая дробь больше второй"""
        self.assertFalse(self.B.__gt__(self.A))


class FractionsGeMethodTests(unittest.TestCase):
    """Тестируем действия с дробями: дробь1 >= дробь 2 """

    def setUp(self) -> None:
        self.A = Fraction(2, 3)
        self.B = Fraction(1, 3)

    def test_first_fr_ge_second_fr(self):
        """тест: первая дробь больше второй"""
        self.assertTrue(self.A.__ge__(self.B))

    def test_first_fr_equal_second_fr(self):
        """тест: первая дробь равна второй"""
        F = Fraction(2, 3)
        self.assertTrue(self.A.__ge__(F))

    def test_first_fr_not_ge_second_fr(self):
        """тест: вторая дробь не больше превой"""
        self.assertFalse(self.B.__ge__(self.A))


if __name__ == "__main__":
    unittest.main()
