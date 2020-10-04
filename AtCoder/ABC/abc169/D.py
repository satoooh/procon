"""素因数分解
Returns:
    list -- [[prime, index], ...]
"""

def factorization(n):
    res = []
    tmp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            res.append([i, cnt])
    if tmp != 1:
        res.append([tmp, 1])
    if res == []:
        res.append([n, 1])
    return res

N = int(input())

if N == 1:
    print(0)
    exit()

res = factorization(N)

ans = 0

for r in res:
    m = 1
    while (m*(m+1)//2 <= r[1]):
        m += 1
    ans += m-1

print(ans)

