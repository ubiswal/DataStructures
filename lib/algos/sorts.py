def bubble_sort(input_arr):
    for i in range(1, len(input_arr)):
        for j in range(i, 0, -1):
            if input_arr[j] < input_arr[j - 1]:
                # Exchange
                temp = input_arr[j]
                input_arr[j] = input_arr[j - 1]
                input_arr[j - 1] = temp
            else:
                break


def merge_sort(arr, start, end):
    if end - start == 1:
        return
    mid = (start + end) // 2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid, end)
    merge(arr, start, end)


def merge(arr, start, end):
    middle = (start + end) // 2
    new_arr = []
    i = start
    j = middle
    while i < middle and j < end:
        if arr[i] < arr[j]:
            new_arr.append(arr[i])
            i = i + 1
        else:
            new_arr.append(arr[j])
            j = j + 1
    if i < middle:
        new_arr.extend(arr[i:middle])

    if j < end:
        new_arr.extend(arr[j:end])
    arr[start:end] = new_arr[:]
