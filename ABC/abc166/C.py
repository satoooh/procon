N, M = map(int, input().split())
H = list(map(int, input().split()))

g = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

ans = 0

for i in range(N):
    flag = True
    for j in g[i]:
        if H[i] > H[j]:
            continue
        else:
            flag = False
    if flag:
        ans += 1

print(ans)
