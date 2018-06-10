def bubble_sort(input_arr):
    for i in range(1, len(input_arr)):
        for j in range(i, 0, -1):
            if input_arr[j] < input_arr[j-1]:
                # Exchange
                temp = input_arr[j]
                input_arr[j] = input_arr[j-1]
                input_arr[j-1] = temp
            else:
                break


def merge_sort(input_arr):
    for i in range(1, len(input_arr)):
        for j in range(i, 0, -1):
            if input_arr[j] < input_arr[j-1]:
                # Exchange
                temp = input_arr[j]
                input_arr[j] = input_arr[j-1]
                input_arr[j-1] = temp
            else:
                break