import unittest

from lib.algos.string_problems import split_string, split_string_memoized, check_balanced_parantheses


class TestStringProblems(unittest.TestCase):
    def test_split_string(self):
        num_ways = split_string("peachpie", {"pea", "ch", "pie", "peach"})
        self.assertEquals(2, num_ways)

    def test_split_string_memoized(self):
        num_ways = split_string_memoized("peachpie", {"pea", "ch", "pie", "peach"}, {})
        self.assertEquals(2, num_ways)

    def test_check_balanced_parantheses(self):
        input_str = "[project]{}[[]])("
        self.assertFalse(check_balanced_parantheses(input_str))
        input_str = ""
        self.assertTrue(check_balanced_parantheses(input_str))
        input_str = "(tree)[]{}(((())))"
        self.assertTrue(check_balanced_parantheses(input_str))
