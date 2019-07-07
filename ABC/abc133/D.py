N = int(input())
A = list(map(int, input().split()))
X = [0] * N

X[0] = sum(A) - 2 * (sum([A[i] for i in range(N) if i % 2 == 1]))

for i in range(N - 1):
	X[i + 1] = 2 * A[i] - X[i]

print(" ".join(map(str, X)))
