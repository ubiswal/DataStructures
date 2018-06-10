import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../")

from lib.algos.string_problems import split_string, split_string_memoized


class TestStringProblems(unittest.TestCase):
    def test_split_string(self):
        num_ways = split_string("peachpie",{"pea", "ch", "pie", "peach"})
        self.assertEquals(2, num_ways)

    def test_split_string_memoized(self):
        num_ways = split_string_memoized("peachpie",{"pea", "ch", "pie", "peach"}, {})
        self.assertEquals(2, num_ways)