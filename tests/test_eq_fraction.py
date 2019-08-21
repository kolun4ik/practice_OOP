import unittest
from modules.fraction import Fraction
from unittest import skip


class FractionsEqualMethodTests(unittest.TestCase):
    """Тестируем действия с дробями: разность"""

    def setUp(self) -> None:
        self.A = Fraction(2, 3)
        self.B = Fraction(2, 3)

    def test_equals_two_correct_fraction(self):
        """тест: эквивалентность дробей"""
        self.assertTrue(self.A == self.B)

    def test_not_equals_two_correct_fraction(self):
        """тест: дробы не экивалентны"""
        F = Fraction(1, 3)
        self.assertFalse(self.A == F)

    def test_not_equals_two_incorrect_fraction(self):
        """тест: дробы не экивалентны"""
        F = Fraction(4, 3)
        self.assertFalse(self.A == F)

    def test_equals_two_negative_fraction(self):
        F = Fraction(-2,3)
        F1 = Fraction(-2,3)
        self.assertTrue(F == F1)


if "__name__" == "__main__":
    unittest.main()