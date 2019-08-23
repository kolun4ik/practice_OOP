import unittest
from modules.fraction import Fraction
from unittest import skip

# Составное присваивание
# x += 1 #другими словами x = x + 1

class FractionsIaddMethodTests(unittest.TestCase):
    """Тестируем действия с дробями: сложение с присваиванием"""

    def setUp(self):
        self.A = Fraction(1, 3)
        self.B = Fraction(2, 3)

    def test_iadd_fraction(self):
        """тест: составное присваивание - накопление результата"""
        for i in range(1,5):
            self.A += 1
        self.assertEqual(self.A.__str__(), '4(1/3)')
        
    def test_iadd_two_fractions(self):
        """тест: накопление одной дроби в другой"""
        for i in range(1,5):
            self.A += self.B
        self.assertEqual(self.A.__str__(), '3')


if __name__ == '__main__':
    unittest.main()
