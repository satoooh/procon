def nakayoshi(X, Y):
    return (X[0]*Y[0] + X[1]*Y[1] != 0)

N = int(input())
X = [list(map(int, input().split())) for _ in range(N)]
MOD = 1000000007

g = [[] for _ in range(N)]

for i in range(N):
    for j in range(i+1, N):
        if nakayoshi(X[i], X[j]):
            g[i].append(j)
            g[j].append(i)

print(g)

not_ans = 0
for f in nakayoshi:
    f

print(not_ans)

ans = (pow(2, N, MOD) - not_ans) % MOD

print(ans)
