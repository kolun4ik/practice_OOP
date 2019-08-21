import unittest
from modules.fraction import Fraction

class FractionTests(unittest.TestCase):
    """Тестируем класс Fraction - дробь"""

    def setUp(self):
        """Дроби для тестов"""
        self.A = Fraction(3,4)


    def tearDown(self):
        del self.A

    def test_fraction(self):
        """тест: у дроби есть числитель и знаменатель"""
        self.assertEqual(self.A.num, 3)
        self.assertEqual(self.A.den, 4)


if "__name__" == "__main__":
    unittest.main()