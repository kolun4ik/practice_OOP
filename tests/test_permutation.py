import unittest
from modules.permutation import permutations


class PermutationTest(unittest.TestCase):
    def test_one_symbol(self):
        """test: permitation  function return one symbol"""
        self.assertEqual(permutations('a'), ['a'])

    def test_two_symbol_permutation(self):
        """test: permutation two symbols"""
        self.assertEqual(sorted(permutations('ab')), ['ab', 'ba'])

    def test_four_symbol_permutation(self):
        """test: permutation four symbols"""
        self.assertEqual(
            sorted(permutations('aabb')),
            ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
        )


if __name__ == '__main__':
    unittest.main()
