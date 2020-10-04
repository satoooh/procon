def is_prime(n):
	if n <= 1:
		return False

	elif n == 2:
		return True

	for p in range(3, int(n ** 0.5) + 1, 2):
		if n % p == 0:
			return False

	return True


ans = 2
for i in range(3, 2000001, 2):
	if is_prime(i):
		ans += i
print(ans)
