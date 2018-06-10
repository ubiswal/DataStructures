import unittest

from lib.algos.sorts import bubble_sort
from lib.algos.sorts import merge_sort, merge


class TestSorts (unittest.TestCase):
    def test_bubble_sort(self):
        input_arr = [1, 3, 7, 2, 9, 5]
        bubble_sort(input_arr)
        self.assertEquals([1, 2, 3, 5, 7, 9], input_arr)

    def test_bubble_sort_with_repetitions(self):
        input_arr = [1, 1, 3, 7, 2, 2, 9, 5]
        bubble_sort(input_arr)
        self.assertEquals([1, 1, 2, 2, 3, 5, 7, 9], input_arr)

    def test_merge(self):
        arr = [1, 3, 5, 7, 2, 4, 6, 8]
        merge(arr, 0, len(arr))
        self.assertEquals([1, 2, 3, 4, 5, 6, 7, 8], arr)

    def test_merge_sort(self):
        input_arr = [1, 3, 7, 2, 9, 5]
        merge_sort(input_arr,0,len(input_arr))
        self.assertEquals([1, 2, 3, 5, 7, 9], input_arr)


