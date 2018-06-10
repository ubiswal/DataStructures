import sys
import os
import unittest
from nose.tools import *

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../")

from lib.algos.sibling_ptr import sibling_ptr, BinaryTree


class TestSiblingTree (unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree(5)
        self.tree.left = BinaryTree(10)
        self.tree.right = BinaryTree(20)
        self.tree.left.left = BinaryTree(30)
        self.tree.right.left = BinaryTree(40)
        self.tree.right.right = BinaryTree(50)
        
    def test_sibling_ptr(self):
        sibling_ptr(self.tree)
        self.assertEquals(20, self.tree.left.sibling.val)
        self.assertEquals(40, self.tree.left.left.sibling.val)
        self.assertEquals(50, self.tree.right.left.sibling.val)