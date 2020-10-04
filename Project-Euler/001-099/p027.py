def is_prime(n):
    """素数判定
    """
    if n < 2:
        return 0
    elif n == 2:
        return 1
    if n%2 == 0:
        return 0
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return 0
    return 1

nmax = 0

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        def f(x):
            return x**2 + a*x + b
        n = 0
        while (is_prime(f(n))):
            n += 1
        if n > nmax:
            nmax = n
            ans = a*b

print(ans)
