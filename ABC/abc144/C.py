def make_divisors(n):
	divisors = []
	for i in range(1, int(n ** 0.5) + 1):
		if n % i == 0:
			divisors.append(i)
			if i != n // i:
				divisors.append(n // i)
	divisors.sort()
	return divisors


N = int(input())
divs = make_divisors(N)
if len(divs) % 2 == 0:
    print(divs[len(divs)//2 - 1] + divs[len(divs)//2] - 2)
else:
    print(divs[len(divs)//2] * 2 - 2)
