from scipy.sparse.csgraph import csgraph_from_dense, dijkstra

N, M = map(int, input().split())

INF = float("inf")

edge = [[INF for _ in range(N)] for _ in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    edge[u-1][v-1] = 1
    edge[v-1][u-1] = 1

G = csgraph_from_dense(edge, null_value=INF)

s = int(input())-1
K = int(input())
t = list(map(int, input().split()))

ans = 0

# 貪欲に求める
a = s
while t:
    d = dijkstra(G, indices=a)
    #print("from", a, d)
    min_d = INF
    for i in range(len(t)):
        if d[t[i]-1] < min_d:
            min_d = d[t[i]-1]
            min_ind = i
    ans += min_d
    a = t[min_ind]-1
    #print(t, ans, min_d, min_ind)
    t.remove(t[min_ind])

print(int(ans))
