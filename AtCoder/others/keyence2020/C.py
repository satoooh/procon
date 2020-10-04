N, K, S = map(int, input().split())

ans = [S] * K

if S == 10**9:
    for _ in range(N-K):
        ans.append(1)
else:
    for _ in range(N-K):
        ans.append(S+1)
print(*ans)
