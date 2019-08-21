import unittest
from modules.fraction import Fraction
from unittest import skip


class FractionsMulMethodTests(unittest.TestCase):
    """Тестируем действия с дробями: умножение"""

    def setUp(self) -> None:
        self.A = Fraction(2, 3)
        self.B = Fraction(2, 3)

    def test_mul_two_correct_fraction(self):
        """тест: умножение дробей"""
        F = self.A * self.B
        self.assertEqual(F.__str__(), '4/9')
        
    def test_mul_incorect_fraction(self):
        """тест: умножаем неправильные дроби"""
        F1 = Fraction(4,5)
        F2 = Fraction(-4,5)
        F = F1 * F2
        self.assertEqual(F.__str__(), '-16/25')

    def test_mul_correct_and_incorect_fraction(self):
        """тест: умножаем правильную дробь на неправильную"""
        B = Fraction(2,1)
        F = self.A * B
        self.assertEqual(F.__str__(), '1(1/3)')


if "__name__" == "__main__":
    unittest.main()