N, M, Q = map(int, input().split())
g = [[] for _ in range(N)]  # g[i]: 頂点iに隣接する頂点のリスト
for _ in range(M):
    u, v = map(int, input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)

c = list(map(int, input().split()))

for _ in range(Q):
    s = input()
    if s[0] == "1":
        x = int(s[2:]) - 1
        print(c[x])
        for y in g[x]:
            c[y] = c[x]
    else:
        x, y = map(int, s[2:].split())
        x -= 1
        print(c[x])
        c[x] = y
