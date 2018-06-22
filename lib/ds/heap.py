class MinHeap:
    def __init__(self, arr, key=lambda x: x):
        self.arr = arr[:]
        self.key = key
        self.create_min_heap(arr)

    def create_min_heap(self, arr):
        N = len(arr) - 1
        for idx in range(N / 2, -1, -1):
            self.min_heapify(idx)

    @staticmethod
    def get_left_child_idx(idx):
        return 2 * idx + 1

    @staticmethod
    def get_right_child_idx(idx):
        return 2 * idx + 2

    def min_heapify(self, idx):
        if idx >= (len(self.arr) - 1) / 2:
            return

        left = MinHeap.get_left_child_idx(idx)
        right = MinHeap.get_right_child_idx(idx)

        small = left
        if right < len(self.arr):
            if self.arr[right] and self.key(self.arr[small]) > self.key(self.arr[right]):
                small = right
        if self.arr[small]:
            if self.key(self.arr[idx]) > self.key(self.arr[small]):
                temp = self.arr[idx]
                self.arr[idx] = self.arr[small]
                self.arr[small] = temp
            self.min_heapify(small)

    def update_key(self, node):
        idx = self.arr.index(node)
        self.min_heapify(idx)


    def extract_min(self):
        retval = self.arr[0]
        self.arr[0] = self.arr[-1]
        del self.arr[-1]
        self.min_heapify(0)
        return retval
