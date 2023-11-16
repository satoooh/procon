N, X = map(int, input().split())
S = list(map(int, input().split()))


ans = sum([S[i] for i in range(N) if S[i] <= X])
print(ans)
