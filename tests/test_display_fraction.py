import unittest
from modules.fraction import Fraction
from unittest import skip

class FractionTests(unittest.TestCase):
    """Тестируем класс Fraction - дробь"""

    def setUp(self):
        """Дроби для тестов"""
        self.A = Fraction(3,4)

    def test_fraction(self):
        """тест: у дроби есть числитель и знаменатель"""
        self.assertEqual(self.A.num, 3)
        self.assertEqual(self.A.den, 4)

    def test_display_fraction(self):
        """тест: представление дроби при вызове str(), print()"""
        self.assertEqual(self.A.__str__() , '3/4')

    def test_print_correct_fraction(self):
        """тест: печатает правильную дробь"""
        F = Fraction(7,3)
        self.assertEqual(F.__str__(), '2(1/3)')

    def test_print_negative_correct_fraction(self):
        """тест: печатает отрицательную правильную дробь"""
        F = Fraction(-3, 5)
        self.assertEqual(F.__str__(), '-3/5')

    def test_print_negative_incorrect_fraction(self):
        """тест: показывает отрицательную не правильную дробь"""
        F = Fraction(-9, 5)
        self.assertEqual(F.__str__(), '-1(4/5)')

    def test_display_num_equal_den(self):
        """тест: числитель равен знаменателю"""
        F = Fraction(3,3)
        self.assertEqual(F.__str__(), '1')

    def test_display_num_div_den_none_remain(self):
        """тест: числитель делится на знаменатель без остатка"""
        F = Fraction(6,2)
        self.assertEqual(F.__str__(), '3')

    def test_display_fraction_simplified_gcd(self):
        """тест: дробь упрощается с помошью НОД (наименьшее общее кратное)"""
        F = Fraction(8, 16)
        self.assertEqual(F.__str__(), '1/2')

    def test_getNum_method(self):
        """тест: getNum возвращает числитель"""
        self.assertEqual(self.A.getNum(), '3')

    def test_getDen_method(self):
        """тест: getDen возвращает числитель"""
        self.assertEqual(self.A.getDen(), '4')

    def test_display_error_type_in_input_not_integer(self):
        """тест: возбуждаем исключение, если введены не целые числа"""
        with self.assertRaises(TypeError):
            Fraction(2.3, 3)

    def test_display_if_den_negative(self):
        """тест: если по ошибке введи отрицательный знаменатель"""
        F = Fraction(3, -4)
        self.assertEqual(F.__str__(), '3/4')

    def test_display_if_num_and_den_nedative(self):
        """тест: учитываем знак только в числителе"""
        F = Fraction(-3,-4)
        self.assertEqual(F.__str__(), '-3/4')

    def test_display_repr_method(self):
        """тест: отображаем дробь при вызове repr()"""
        self.assertEqual(repr(self.A), 'Дробь: 3/4')


if __name__ == "__main__":
    unittest.main()