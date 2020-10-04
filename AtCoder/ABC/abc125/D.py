N = int(input())
A = list(map(int, input().split()))
B = []
count = 0  # Aの中の負の要素の個数
for i in range(N):
	if A[i] != abs(A[i]):
		count += 1
	B.append(abs(A[i]))
if count % 2 == 0:
	print(sum(B))
else:
	print(sum(B) - min(B) * 2)
