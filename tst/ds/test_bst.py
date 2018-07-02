import unittest
import  random

from lib.ds.bst import Bst


class TestBST(unittest.TestCase):
    def setUp(self):
        self.inputs = [random.randint(1, 200) for i in range(0,10)]
        self.bst = Bst(self.inputs[0])
        for i in self.inputs[1:]:
            self.bst.insert(i)

    def test_bst_parse(self):
        arr = []
        self.bst.parse(arr)
        self.assertEqual(sorted(self.inputs), arr)

    def test_bst_greatest_smallest(self):
        self.assertEquals(min(self.inputs), self.bst.smallest())
        self.assertEquals(max(self.inputs), self.bst.greatest())

    def test_is_bst(self):
        self.assertTrue(self.bst.is_bst())

    def test_false_test_is_bst(self):
        self.bst.left.val= 1000
        self.assertFalse(self.bst.is_bst())