N, K = map(int, input().split())
ans = 1
k = K
while N >= k:
    k *= K
    ans += 1
print(ans)
