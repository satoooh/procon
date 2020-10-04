N = int(input())
A, B = [0] * N, [0] * N
for i in range(N):
	A[i], B[i] = map(int, input().split())

index = A.index(max(A))
print(A[index] + B[index])
