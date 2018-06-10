class BinaryTree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.sibling = None


def sibling_ptr(tree):
    frontier = [tree]
    while len(frontier)>0:
        nxt = []
        for u in frontier:
            if u.left:
                nxt.append(u.left)
            if u.right:
                nxt.append(u.right)
        
        for i in range(0, len(nxt)-1):
            nxt[i].sibling = nxt[i+1]
        frontier = nxt
        