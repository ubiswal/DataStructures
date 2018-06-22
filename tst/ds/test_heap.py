import unittest

from lib.ds.heap import MinHeap



class TestHeap(unittest.TestCase):
    def setUp(self):
        self.my_arr = [12, 4, 2, 7, 10, 11, 8, 9]
        self.test_heap = MinHeap(self.my_arr)

    def test_heap_extract_min(self):
        arr =[]
        for i in range(0, len(self.my_arr)):
            arr.append(self.test_heap.extract_min())

        expected_arr = sorted(self.my_arr)
        print(arr)
        for i in range(len(arr)):
            self.assertFalse(arr[i] != expected_arr[i])

'''
    def test_heap_order(self):
        for i in range(0, len(self.test_heap.arr) // 2):
            self.assertTrue(self.test_heap.arr[i] < self.test_heap.arr[2 * i + 1])
            if 2 * i + 2 < len(self.test_heap.arr):
                self.assertTrue(self.test_heap.arr[i] < self.test_heap.arr[2 * i + 2])
        print("min heap is: "+str(self.test_heap.arr))
'''
