def is_prime(n):
	if n == 1:
		return False
	for i in range(2, int(n ** .5) + 1):
		if n % i == 0:
			return False
	return True


def looks_like_prime(n):
	if is_prime(n):
		return True
	elif (n != 1) and (n % 2 != 0) and (n % 3 != 0) and (n % 5 != 0):
		return True
	else:
		return False


N = int(input())
if looks_like_prime(N):
	print("Prime")
else:
	print("Not Prime")
