import unittest
from modules.fraction import Fraction
from unittest import skip


class FractionsTrueDyvMethodTests(unittest.TestCase):
    """Тестируем действия с дробями: деление"""

    def setUp(self) -> None:
        self.A = Fraction(2, 3)
        self.B = Fraction(1, 3)

    def test_true_div_two_fraction(self):
        """тест: умножение двух дробей"""
        F = self.A / self.B
        self.assertEqual(F.__str__(), '2')

    def test_true_div_two_incorect_fraction(self):
        """тест: делим не правильные дроби"""
        F1 = Fraction(14,8)
        F2 = Fraction(2, 1)
        F = F1 / F2
        self.assertEqual(F.__str__(), '7/8')

if "__name__" == "__main__":
    unittest.main()