import unittest
from modules.fraction import Fraction
from unittest import skip


class FractionsAddMethodTests(unittest.TestCase):
    """Тестируем действия с дробями: сложение"""

    def setUp(self):
        self.A = Fraction(2, 3)
        self.B = Fraction(4, 7)
        self.C = Fraction(3, 3)
        self.D = Fraction(4, 2)
        self.E = Fraction(-2, 3)

    def test_add_two_fraction(self):
        """тест: сложение дробей"""
        F = self.A + self.B
        self.assertEqual(F.__str__(), '1(5/21)')

        F1 = self.A + self.C
        self.assertEqual(F1.__str__(), '1(2/3)')

        F2 = self.B + self.D
        self.assertEqual(F2.__str__(), '2(4/7)')

        F3 = self.C + self.E
        self.assertEqual(F3.__str__(), '1/3')

        F4 = self.A + self.E
        self.assertEqual(F4.__str__(), '0')

    def test_add_fraction_with_int(self):
        """тест: сложим дробь с целым числом"""
        F = self.A + 2
        self.assertEqual(F.__str__(), '2(2/3)')


if __name__ == "__main__":
    unittest.main()
