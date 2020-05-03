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


X = int(input())
divs = make_divisors(X)

# a = b+p
for p in divs:
    for b in range(-10000, 10000):
        a = b+p
        if a**5 - b**5 == X:
            print(a, b)
            exit()
