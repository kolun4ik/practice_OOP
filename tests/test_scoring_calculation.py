import unittest
from modules.mystring import scoring_calculation


class TestScoringCalculation(unittest.TestCase):
    """Function calculate scoring for word"""
    def test_scoring_calculation_return_type_int(self):
        """тест: скоринг возвращает значение типа int"""
        self.assertTrue(isinstance(scoring_calculation(), int))

    def test_scoring_calculation(self):
        """тест: расет скоринга для заданного слова"""
        self.assertEqual(scoring_calculation('abc'), 6)
