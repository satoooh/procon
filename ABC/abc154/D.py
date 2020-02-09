N, K = map(int, input().split())
p = list(map(int, input().split()))

res = sum(p[:K])
res_max = res
i_max = 0
for i in range(1, N-K+1):
    res += p[i+K-1] - p[i-1]
    if res > res_max:
        res_max = res
        i_max = i

ans = 0
for j in range(K):
    ans += (p[i_max + j] + 1) / 2
print(ans)
