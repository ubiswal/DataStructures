import unittest

from lib.algos.graph_problems import sibling_ptr, BinaryTree
from lib.algos.dijkstra import dijkstra, bellman_ford


class TestGraphProblems(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree(5)
        self.tree.left = BinaryTree(10)
        self.tree.right = BinaryTree(20)
        self.tree.left.left = BinaryTree(30)
        self.tree.right.left = BinaryTree(40)
        self.tree.right.right = BinaryTree(50)

        ##for dijkstra
        self.adj_list = {
            "A":[("B", 10),("C", 3)],
            "B":[("C",1),("D",2)],
            "C":[("B",4),("D",8),("E",2)],
            "D":[("E",7),],
            "E":[("D",9)]
        }


    def test_sibling_ptr(self):
        sibling_ptr(self.tree)
        self.assertEquals(20, self.tree.left.sibling.val)
        self.assertEquals(40, self.tree.left.left.sibling.val)
        self.assertEquals(50, self.tree.right.left.sibling.val)


    def test_dijkstra(self):
        self.assertEquals(dijkstra(self.adj_list, "A"),{"A": 0,"B": 7, "C":3 , "D":9, "E":5} )

    def test_bellman_ford(self):
        self.assertEquals(bellman_ford(self.adj_list, "A"), {"A": 0, "B": 7, "C": 3, "D": 9, "E": 5})