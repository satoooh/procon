N = int(input())
A = [int(input()) for _ in range(N)]
first = max(A)
second = sorted(A)[:: -1][1]
for ai in A:
	if ai == first:
		print(second)
	else:
		print(first)
