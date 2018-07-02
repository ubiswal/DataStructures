import unittest

from lib.ds.bst import Bst


class TestBST(unittest.TestCase):
    def setUp(self):
        self.inputs = [50, 25, 100, 12, 30, 75, 125]
        self.bst = Bst(self.inputs[0])
        for i in self.inputs[1:]:
            self.bst.insert(i)

    def test_bst_parse(self):
        arr = []
        self.bst.parse(arr)
        self.assertEqual(sorted(self.inputs), arr)
