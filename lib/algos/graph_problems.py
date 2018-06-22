from lib.ds.heap import MinHeap


class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.sibling = None


def sibling_ptr(tree):
    frontier = [tree]
    while len(frontier) > 0:
        nxt = []
        for u in frontier:
            if u.left:
                nxt.append(u.left)
            if u.right:
                nxt.append(u.right)

        for i in range(0, len(nxt) - 1):
            nxt[i].sibling = nxt[i + 1]
        frontier = nxt


def dijkstra(G, s):
    S = {s: None}
    d = {}
    for vertex in G.keys():
        d[vertex] = float("Inf")
    d[s] = 0.0
    Q = MinHeap(list(G.keys()), lambda x: d[x])

    while len(Q.arr) > 0:
        u = Q.extract_min()
        for v, w in G[u]:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                S[v] = u
                if v in Q.arr:
                    Q.update_key(v)
    return d


def bellman_ford(G, s):
    S = {s: None}
    d = {}
    for vertex in G.keys():
        d[vertex] = float("Inf")
    d[s] = 0.0

    for i in range(0, len(G.keys()) - 1):
        for u in G.keys():
            for v, w in G[u]:
                if d[v] > d[u] + w:
                    d[v] = d[u] + w
                    S[v] = u

    for u in G.keys():
        for v, w in G[u]:
            if d[v] > d[u] + w:
                d[v] = -float("Inf")
    return d
