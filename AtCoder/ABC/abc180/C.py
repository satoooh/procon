def make_divisors(n):
    """約数を全列挙する
    """
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
for d in divs:
    print(d)
