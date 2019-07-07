def is_prime(k):
	if k == 1:
		return False
	for i in range(2, int(k ** 0.5) + 1):
		if k % i == 0:
			return False
	return True


n = int(input())
N = n * (n + 1) // 2
if is_prime(N):
	print("WANWAN")
else:
	print("BOWWOW")
