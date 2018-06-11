import unittest

from lib.algos.array_problems import convert_square_matrix_to_spiral_arr, find_mirror_image, find_max_sum_in_min_pairs
from lib.algos.array_problems import find_pascals_triangle, generate_n_level_pascals_triangle


class TestArrayProblems(unittest.TestCase):
    def test_convert_square_matrix_to_spiral_arr(self):
        input_arr = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
        self.assertEquals([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                          convert_square_matrix_to_spiral_arr(input_arr, len(input_arr[0])))

    def test_find_mirror_image(self):
        input_arr = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
        find_mirror_image(input_arr)
        self.assertEquals([[1, 0, 0], [0, 1, 0], [1, 1, 1]], input_arr)

    def test_find_max_sum_min_pair(self):
        arr = [1, 4, 2, 3]
        self.assertEquals(4, find_max_sum_in_min_pairs(arr))

    def test_find_pascals_traingle(self):
        self.assertEquals(1, find_pascals_triangle(1, 0, {}))
        self.assertEquals(3, find_pascals_triangle(3, 1, {}))
        self.assertEquals(0, find_pascals_triangle(2, 4, {}))

    def test_gen_pascal_triangle(self):
        expected = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ]
        actual = generate_n_level_pascals_triangle(5)
        self.assertEquals(expected, actual)
