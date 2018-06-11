import unittest

from lib.ds.heap import MinHeap


class TestHeap(unittest.TestCase):
    def setUp(self):
        self.test_heap = MinHeap([12, 4, 2, 7, 10, 11, 8, 9])

    def test_heap_order(self):
        for i in range(0, len(self.test_heap.arr) // 2):
            self.assertTrue(self.test_heap.arr[i] < self.test_heap.arr[2 * i + 1])
            if 2 * i + 2 < len(self.test_heap.arr):
                self.assertTrue(self.test_heap.arr[i] < self.test_heap.arr[2 * i + 2])
