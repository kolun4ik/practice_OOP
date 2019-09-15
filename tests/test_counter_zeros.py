import unittest
from modules.zeros import zeros, zeros_optimized
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


class TestCountZerosOptimized(unittest.TestCase):
    """Test optimized function calculate trailing zeros"""

    def test_optimized_equals_calc_zeros(self):
        """test: optimized function calc zeros equals
        calc zeros function"""
        self.assertEqual(zeros_optimized(0), zeros(0))

    def test_optimized_equals_calc_zeros_with_args_six(self):
        """test: optimized function calc zeros equals
        calc zeros function with arg = 6"""
        self.assertEqual(zeros_optimized(6), zeros(6))

    def test_optimized_equals_calc_zeros_with_args_thirty(self):
        """test: optimized function calc zeros equals
        calc zeros function with arg = 30"""
        self.assertEqual(zeros_optimized(30), zeros(30))
