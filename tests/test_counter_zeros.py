import unittest
from modules.zeros import zeros
from unittest import skip

class TestZerosFunction(unittest.TestCase):
    """Test function calculate the number of trailing zeros"""
    def test_calculate_none_trailing_zeros(self):
        """test: return  none trailing zeros"""
        self.assertEqual(zeros(0), 0)
    
    def test_calculate_one_trailing_zeros(self):
        """test: return one trailing zeros"""
        self.assertEqual(zeros(6), 1)

    def test_calculate_seven_trailing_zeros(self):
        """test: return seven trailing zeros"""
        self.assertEqual(zeros(30), 7)