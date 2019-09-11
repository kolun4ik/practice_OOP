import unittest
from modules.fraction import Fraction
from unittest import skip

# “Oбычное” сложение some_object + other.
# Отраженное выражение, отличается порядком слагаемых other + some_object
# Объект слева от оператора (other в примере) не должен иметь обычной
# неотражённой версии этого метода.
# В нашем примере, some_object.__radd__ будет вызван только если в other не
# определён __add__.


class FractionsRaddMethodTests(unittest.TestCase):
    """Тестируем действия с дробями: отраженое сложение"""

    def setUp(self):
        self.A = Fraction(1, 3)
        self.B = Fraction(2, 3)

    def test_radd_int_with_fraction(self):
        """тест: сложение целого числа с дробью"""
        F = 2 + self.A
        self.assertEqual(F.__str__(), '2(1/3)')

    def test_radd_negative_int_with_fraction(self):
        """тест: сложение отрицательного целого с дробью"""
        F = -2 + self.A
        self.assertEqual(F.__str__(), '-1(2/3)')


if __name__ == '__main__':
    unittest.main()
