N, K = map(int, input().split())

# 2 <= a+b <= 2N
# 2 <= c+d <= 2N
# a+b が決まれば c+d = a+b-K で決まることに着目

ans = 0
for M in range(2+K, 2*N+1):
    ans += max(0, (min(N, M-1) - max(1, M-N) + 1) * (min(N, M-K-1) - max(1, M-K-N) + 1))
print(ans)
