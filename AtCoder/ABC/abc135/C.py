N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans, surplus = 0, 0
for i in range(N):
    tmp = min(A[i], surplus)
    ans += tmp
    A[i] -= tmp
    if B[i] > A[i]:
        ans += A[i]
        surplus = B[i] - A[i]
    else:
        ans += B[i]
        surplus = 0
tmp = min(A[N], surplus)
ans += tmp
print(ans)
