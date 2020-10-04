#WIP
from collections import deque

def bfs(s):
    dist = [-1] * (N + 1)
    que = deque([s])
    dist[s] = 0
    while que:
        v = que.popleft()
        d = dist[v]
        for w in g[v]:
            if dist[w] != -1:
                continue
            dist[w] = d + 1
            que.append(w)
    d = max(dist)
    return dist.index(d), d

N = int(input())
S = [input() for _ in range(N)]

# グラフの構築
g = [[] for i in range(N + 1)]
for i in range(N):
    for j in range(i + 1, N):
        if S[i][j] == "1":
            g[i + 1].append(j + 1)
            g[j + 1].append(i + 1)
#print(g)

# 三角loopが存在する場合は-1を出力（例外処理）
for i in range(1, len(g)):
    for v in g[i]:
        for v2 in g[v]:
            if i == v2:
                continue
            if i in g[v2]:
                print(-1)
                exit()

# 木の直径が答え（double-sweep）
u, _ = bfs(1)
v, d = bfs(u)
print(d + 1)
