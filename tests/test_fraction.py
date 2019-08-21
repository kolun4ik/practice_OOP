import unittest
from modules.fraction import Fraction

class FractionTests(unittest.TestCase):
    """Тестируем класс Fraction - дробь"""

    def setUp(self):
        """Дроби для тестов"""
        self.A = Fraction(3,4)

    def test_fraction(self):
        """тест: у дроби есть числитель и знаменатель"""
        self.assertEqual(self.A.num, 3)
        self.assertEqual(self.A.den, 4)

    def test_showing_fraction(self):
        """тест: представление дроби"""
        self.assertEqual(self.A.__str__() , '3/4')

    def test_showing_correct_fraction(self):
        """тест: правильная дробь"""
        B = Fraction(7,3)
        self.assertEqual(B.__str__(), '2(1/3)')

    def test_showing_num_equal_den(self):
        """тест: числитель равен знаменателю"""
        C = Fraction(3,3)
        self.assertEqual(C.__str__(), '1')

    def test_snowing_num_equals_den_(self):
        """тест: числитель еквивалентен знаменателю"""
        D = Fraction(6,6)
        self.assertEqual(D.__str__(), '1')

    def test_showing_num_div_den_none_remain(self):
        """тест: числитель делится на знаменатель без остатка"""
        E = Fraction(6,2)
        self.assertEqual(E.__str__(), '3')

    def test_showing_fraction_simplified_gcd(self):
        """тест: дробь упрощается с помошью НОД (наименьшее общее кратное)"""
        F = Fraction(8, 16)
        self.assertEqual(F.__str__(), '1/2')




if "__name__" == "__main__":
    unittest.main()