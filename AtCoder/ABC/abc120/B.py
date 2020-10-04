A, B, K = map(int, input().split())
D = []
for i in range(A, 0, -1):
	if A % i == 0 and B % i == 0:
		D.append(i)
print(D[K - 1])
