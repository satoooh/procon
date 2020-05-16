from heapq import heappush, heappop

def dijkstra_heap(s):
    """頂点sから各頂点への最短距離"""
    d = [float("inf") for _ in range(N)]
    used = [True for _ in range(N)]  # True: 未確定
    d[s] = 0
    used[s] = False
    edgelist = []
    for e in edge[s]:
        heappush(edgelist, e)
    while len(edgelist):
        min_edge = heappop(edgelist)
        # まだ使われていない頂点の中から最小距離のものを探す
        if not used[min_edge[1]]:
            continue
        v = min_edge[1]
        d[v] = min_edge[0]
        used[v] = False
        for e in edge[v]:
            if used[e[1]]:
                heappush(edgelist, [e[0]+d[v], e[1]])
    return d

N = int(input())

edge = [[] for _ in range(N)]  # edge[i]: i から出る道の[重み、行き先]の配列

for _ in range(N-1):
    x, y, z = map(int, input().split())
    edge[x-1].append([z, y-1])
    edge[y-1].append([z, x-1])

Q, K = map(int, input().split())
z = dijkstra_heap(K-1)

for _ in range(Q):
    x, y = map(int, input().split())
    print(z[x-1] + z[y-1])
