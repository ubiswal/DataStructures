import unittest

from lib.algos.graph_problems import *
from lib.ds.bst import Bst


class TestSiblingTree(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree(5)
        self.tree.left = BinaryTree(10)
        self.tree.right = BinaryTree(20)
        self.tree.left.left = BinaryTree(30)
        self.tree.right.left = BinaryTree(40)
        self.tree.right.right = BinaryTree(50)
        self.adj_list = {
            "A": [("B", 10), ("C", 3)],
            "B": [("C", 1), ("D", 2)],
            "C": [("B", 4), ("D", 8), ("E", 2)],
            "D": [("E", 7), ],
            "E": [("D", 9)]
        }
        self.bst = Bst(50)
        self.bst.left = Bst(25)
        self.bst.left.left = Bst(12)
        self.bst.left.right = Bst(35)
        self.bst.left.right.left = Bst(33)
        self.bst.left.right.left.right = Bst(34)
        self.bst.left.right.left.left = Bst(32)
        self.bst.right = Bst(100)
        self.bst.right.right = Bst(150)
        self.bst.right.left = Bst(75)
        self.bst.right.left.left = Bst(60)
        self.bst.right.left.left.right = Bst(65)
        self.bst.right.left.left.right.right = Bst(66)
        self.bst.right.left.right = Bst(80)
        self.bst.right.left.right.left = Bst(77)

    def test_sibling_ptr(self):
        sibling_ptr(self.tree)
        self.assertEquals(20, self.tree.left.sibling.val)
        self.assertEquals(40, self.tree.left.left.sibling.val)
        self.assertEquals(50, self.tree.right.left.sibling.val)

    def test_dijkstra(self):
        expected_distances = {
            "A": 0,
            "B": 7,
            "C": 3,
            "D": 9,
            "E": 5
        }
        self.assertEquals(dijkstra(self.adj_list, "A"), expected_distances)

    def test_bellman_ford(self):
        expected_distances = {
            "A": 0,
            "B": 7,
            "C": 3,
            "D": 9,
            "E": 5
        }
        self.assertEquals(bellman_ford(self.adj_list, "A"), expected_distances)

    def test_smaller_closest(self):
        self.assertEqual(50, find_closest_smaller(self.bst, 56))
        self.assertEqual(60, find_closest_smaller(self.bst, 62))
        self.assertEqual(35, find_closest_smaller(self.bst, 36))
