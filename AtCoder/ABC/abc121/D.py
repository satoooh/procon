def xor(n):
	if n % 4 == 0:
		return n
	elif n % 4 == 1:
		return 1
	elif n % 4 == 2:
		return n + 1
	else:
		return 0

A, B = map(int, input().split())
print(xor(A - 1) ^ xor(B))
