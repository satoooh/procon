def is_prime(n):  # 素数かどうかを判定する関数isPrime()を定義
	if n == 1:
		return False

	for p in range(2, int(n ** 0.5) + 1):
		if n % p == 0:
			return False

	return True


Primes = []
i = 2
while True:
	if is_prime(i):
		Primes.append(i)
	if len(Primes) == 10001:
		print(Primes[-1])
		exit()
	i += 1
