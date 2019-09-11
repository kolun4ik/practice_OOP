import unittest
from modules.fraction import Fraction
from unittest import skip


class FractionsSubMethodTests(unittest.TestCase):
    """Тестируем действия с дробями: разность"""

    def setUp(self) -> None:
        self.A = Fraction(2, 3)
        self.B = Fraction(4, 7)
        self.C = Fraction(3, 3)
        self.D = Fraction(4, 2)
        self.E = Fraction(-2, 3)

    def test_sub_two_fraction(self):
        """тест: вычитание дробей"""
        F = self.A - self.B
        self.assertEqual(F.__str__(), '2/21')

        F1 = self.B - self.A
        self.assertEqual(F1.__str__(), '-2/21')

        F2 = self.A - self.D
        self.assertEqual(F2.__str__(), '-1(1/3)')

        F3 = self.A - self.E
        self.assertEqual(F3.__str__(), '1(1/3)')

        F4 = self.C - self.E
        self.assertEqual(F4.__str__(), '1(2/3)')


if __name__ == "__main__":
    unittest.main()
