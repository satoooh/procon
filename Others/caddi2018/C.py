from collections import Counter

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

N, P = map(int, input().split())
f = Counter(prime_factorize(P))

ans = 1
for k, v in f.items():
    if v >= N:
        ans *= k ** (v//N)
print(ans)
