from collections import Counter

MOD = 10**9 + 7

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

def multiply_primes(a, b):
    """素因数分解系のCounter型のa, bに対してa*bの素因数分解系を計算する"""
    res = Counter([])
    keys = a.keys() | b.keys()
    for k in keys:
        res[k] = a[k] + b[k]
    return res

A, B = map(int, input().split())

res = Counter([])

for x in range(B+1, A+1):
    fx = Counter(prime_factorize(x))
    res = multiply_primes(res, fx)

ans = 1
for k in res.keys():
    ans *= res[k]+1
    ans %= MOD

print(ans)
