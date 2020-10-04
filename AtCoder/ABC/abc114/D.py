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

def multiply_primes(a, b):
    """素因数分解系のCounter型のa, bに対してa*bの素因数分解系を計算する"""
    res = Counter([])
    keys = a.keys() | b.keys()
    for k in keys:
        res[k] = a[k] + b[k]
    return res

N = int(input())

# 答えは N! の約数かつ
# 素因数分解が x^2 y^4 z^4 の形になるもの
# 素因数分解が x^74 の形になるもの
# 素因数分解が x^2 y^24 の形になるもの
# 素因数分解が x^4 y^14 の形になるもの
# しかない

f = Counter([])  # f が N! の素因数分解になる
for n in range(2, N+1):
    f = multiply_primes(f, Counter(prime_factorize(n)))

c2, c4, c14, c24, c74 = 0, 0, 0, 0, 0

for item in f.items():
    k = item[1]
    c2 += (k >= 2)
    c4 += (k >= 4)
    c14 += (k >= 14)
    c24 += (k >= 24)
    c74 += (k >= 74)

ans_2_4_4 = (c4 * (c4 - 1))//2 * (c2 - 2)
ans_74 = c74
ans_2_24 = c24 * (c2 - 1)
ans_4_14 = c14 * (c4 - 1)

ans = ans_2_4_4 + ans_74 + ans_2_24 + ans_4_14
print(ans)
