class Bst:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, val):
        if val < self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = Bst(val)
                self.left.parent = self
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = Bst(val)
                self.right.parent = self

    def greatest(self):
        if self.right:
            return self.right.greatest()
        else:
            return self.val

    def smallest(self):
        if self.left:
            return self.left.smallest()
        else:
            return self.val

    def is_bst(self):
        check_left = self.left is None or (self.left and self.left.is_bst() and self.val > self.left.greatest())
        check_right = self.right is None or (self.right and self.right.is_bst() and self.val < self.right.smallest())
        return check_left and check_right

    def parse(self, arr):
        if self.left:
            self.left.parse(arr)
        arr.append(self.val)

        if self.right:
            self.right.parse(arr)
