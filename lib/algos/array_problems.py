def ring_to_arr(ring_num, rows, cols, input_arr, idx, new_arr):
    ##convert 1st row
    for i in range(ring_num, cols - ring_num):
        new_arr.append(input_arr[ring_num][i])
        idx = idx + 1
    ##convert end column
    for i in range(ring_num, rows - ring_num):
        new_arr.append(input_arr[i][cols - ring_num])
        idx = idx + 1
    ##convert end row
    for i in range(cols - ring_num, ring_num, -1):
        new_arr.append(input_arr[rows - ring_num][i])
        idx = idx + 1
    ##convert 1st col
    for i in range(rows - ring_num, ring_num, -1):
        new_arr.append(input_arr[i][ring_num])
        idx = idx + 1


def convert_square_matrix_to_spiral_arr(input_arr, num_rows):
    num_rings = num_rows // 2
    spiral_arr = []
    idx = 0
    rows = cols = num_rows - 1
    for i in range(0, num_rings):
        ring_to_arr(i, rows, cols, input_arr, idx, spiral_arr)
    return spiral_arr


# https://leetcode.com/problems/flipping-an-image/description/
def find_mirror_image(matrix):
    for row in matrix:
        for i in range(0, len(row)):
            if row[i] == 0:
                row[i] = 1
            else:
                row[i] = 0

        for j in range(0, len(row) // 2):
            temp = row[j]
            row[j] = row[len(row) - 1 - j]
            row[len(row) - 1 - j] = temp


# https://leetcode.com/problems/array-partition-i/description/
def find_max_sum_in_min_pairs(arr):
    sorted_arr = sorted(arr)
    max_sum = 0
    for i in range(0, len(sorted_arr), 2):
        max_sum = max_sum + sorted_arr[i]
    return max_sum


def find_pascals_triangle(row, col, memo):
    if (row, col) in memo:
        return memo[(row, col)]
    if col == 0:
        return 1
    if row == 0:
        return 0
    retval = find_pascals_triangle(row - 1, col, memo) + find_pascals_triangle(row - 1, col - 1, memo)
    memo[(row, col)] = retval
    return retval


def generate_n_level_pascals_triangle(n):
    memo = {}
    matrix = []
    for i in range(0, n):
        matrix.append([])
        for j in range(0, i + 1):
            matrix[i].append(find_pascals_triangle(i, j, memo))
    return matrix
