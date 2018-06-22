from lib.ds.heap import MinHeap

def dijkstra(G,s):
    S = {s: None}
    d = {}
    for vertex in G.keys():
        d[vertex] = float("Inf")
    d[s] = 0.0
    Q = MinHeap(G.keys(), lambda x: d[x])

    while len(Q.arr)>0:
        u = Q.extract_min()
        for v,w in G[u]:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                S[v] = u
                if v in Q.arr:
                    Q.update_key(v)
        print(Q.arr)
        print(d)
    return d


def bellman_ford(G, s):
    S = {s: None}
    d = {}
    heap_arr = []
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