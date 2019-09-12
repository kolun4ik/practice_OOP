import unittest
from modules.mystring import high
from unittest import skip


class TestHighFunction(unittest.TestCase):
    """test high score word in list"""
    def test_high_function_return_type_str(self):
        """тест: high возвращает результат строку"""
        self.assertTrue(isinstance(high('a'), str))

    def test_high_return_one_world_string(self):
        """тест: ф-ция принимает строку из одного слова
            и возвращает это слово"""
        self.assertEqual(high('test'), 'test')

    def test_high_return_highscore_word(self):
        """тест: ф-ция возвращает слово с наибольшим весовым индексом"""
        self.assertEqual(high('a b'), 'b')

    def test_high_return_firt_word_for_two_equal_score_rank(self):
        """тест: вернуть первое слово из двух одинаковых по скорингу слов"""
        self.assertEqual(high('ab ba'), 'ab')
        self.assertNotEqual(high('ab ba'), 'ba')
