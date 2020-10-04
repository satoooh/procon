from fractions import gcd

N = int(input())
A = list(map(int, input().split()))
Asort = sorted(A)[:: -1]
L = [0] * N  # 左からi番目までのgcdをメモった配列
R = [0] * N  # 右からi番目までのgcdをメモった配列
L[0] = A[0]
R[0] = A[N - 1]
for i in range(1, N):
	L[i] = gcd(L[i - 1], A[i])
	R[i] = gcd(R[i - 1], A[N - 1 - i])

ans = max(L[N - 2], R[N - 2])
for j in range(1, N - 1):
	ans = max(ans, gcd(L[j - 1], R[N - j - 2]))
print(ans)
