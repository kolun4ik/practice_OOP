import unittest
from modules.currying import add


class TestCurringAddFunction(unittest.TestCase):
    """Testing curring call function"""
    
    def test_add_with_one_arg(self):
        """test: call add() with one argument"""
        self.assertEqual(add(1), 1)
        
    def test_add_with_two_args(self):
        """test: call add() with two args"""
        self.assertEqual(add(1)(1), 2)