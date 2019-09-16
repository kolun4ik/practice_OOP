import unittest
from modules.mystring import first_non_repeating_latter


class TestFirstNonRepeatingLetter(unittest.TestCase):
    """Test function returns first non repeating letter"""
    def test_fnrl_return_type_string(self):
        """test: function returns type string"""
        self.assertTrue(isinstance(first_non_repeating_latter('a'), str))

    def test_fnrl_return_one_letter(self):
        """test: function return one letter equal input letter"""
        self.assertEqual(first_non_repeating_latter('a'), 'a')

    def test_fnrl_return_first_non_repeat_letter(self):
        """test: chould returns 'b' for inputs 'aab'"""
        self.assertEqual(first_non_repeating_latter('aab'), 'b')

    def test_fnrl_return_empty_if_only_repeat_letter(self):
        """test: chould returns '' for inputs 'abba' """
        self.assertEqual(first_non_repeating_latter('abba'), '')

    def test_fnrl_return_non_repeat_letter_in_word(self):
        """test: chould returns 'e' for inputs 'moonmen' """
        self.assertEqual(first_non_repeating_latter('moonmen'), 'e')

    def test_fnrl_return_non_repeat_letter_in_sentence(self):
        """test: chould returns 'w' for inputs 'hello world, eh?' """
        self.assertEqual(first_non_repeating_latter('hello world, eh?'), 'w')

    def test_fnrl_return_non_repeat_letter_if_word_have_uppercase_symbols(self):
        """test: chould returns 'w' for inputs 'hello world, eh?' """
        self.assertEqual(first_non_repeating_latter('sTreSS'), 'T')