N = int(input())
A, B = [0]*N, [0]*N
for i in range(N):
    A[i], B[i] = map(int, input().split())

ans = 0
for i in range(N):
    now = N-i-1
    ans += (B[now] - (A[now] + ans) % B[now]) % B[now]

print(ans)
