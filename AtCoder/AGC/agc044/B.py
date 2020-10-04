from heapq import heappush, heappop

def dijkstra_heap(s):
    """頂点sから各頂点への最短距離"""
    d = [float("inf") for _ in range(N**2)]
    used = [True for _ in range(N**2)]  # True: 未確定
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

#N = int(input())
#P = list(map(int, input().split()))

##### test case
from tqdm import tqdm
import random
N = 500
P = [i for i in range(1, N**2+1)]
random.shuffle(P)
#####

edge = [[] for _ in range(N**2)]  # edge[i]: i から出る道の[重み、行き先]の配列


# 辺をはる
for i in range(1, N-1):
    edge[i].append([1, i+N])
    edge[i+N].append([1, i])
    edge[N*(N-2)+i].append([1, N*(N-1)+i])
    edge[N*(N-1)+i].append([1, N*(N-2)+i])

for j in range(1, N-1):
    edge[j*N].append([1, j*N+1])
    edge[j*N+1].append([1, j*N])
    edge[(j+1)*N-2].append([1, (j+1)*N-1])
    edge[(j+1)*N-1].append([1, (j+1)*N-2])

for i in range(1, N-1):
    for j in range(1, N-1):
        x = i + j*N
        y1, y2 = x+1, x+N
        if [1, y1] not in edge[x]:
            edge[x].append([1, y1])
            edge[y1].append([1, x])
        if [1, y2] not in edge[x]:
            edge[x].append([1, y2])
            edge[y2].append([1, x])

goal = [i for i in range(1, N-1)] + [i*N for i in range(1, N-1)] + [(i+1)*N-1 for i in range(1, N-1)] + [i+(N-1)*N for i in range(1, N-1)]

ans = 0
for pi in tqdm(range(len(P))):
    tar = P[pi]-1
    if tar in [0, N-1, (N-1)*N, N**2-1]:
        continue  # 端点は計算から省く
    elif tar in goal:
        # ノードの更新だけ
        for r in edge[edge[tar][0][1]]:
            if r[1] == tar:
                r[0] = 0
    else:
        # 最小コストを計算
        d = dijkstra_heap(tar)
        res = min([d[i] for i in goal])
        ans += res
        # ノードの更新
        if tar%N > 0:
            for r in edge[tar-1]:
                if r[1] == tar:
                    r[0] = 0
        if tar%N < N-1:
            for r in edge[tar+1]:
                if r[1] == tar:
                    r[0] = 0
        if tar//N > 0:
            for r in edge[tar-N]:
                if r[1] == tar:
                    r[0] = 0
        if tar//N < N-1:
            for r in edge[tar+N]:
                if r[1] == tar:
                    r[0] = 0

print(ans)
