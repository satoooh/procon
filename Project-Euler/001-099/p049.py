from itertools import permutations

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


# 4桁の素数を全列挙
cand = [i for i in range(1001, 10000, 2) if is_prime(i)]

for c in cand:
    res = []
    tmp = [int("".join(v)) for v in permutations(str(c))]
    tmp.remove(c)
    for t in set(tmp):
        if len(str(t)) == 4 and is_prime(t):
            res.append(t)
    res.sort()
    for i in range(len(res)-2):
        if res[i+1] - res[i] == res[i+2] - res[i+1]:
            print(str(res[i]) + str(res[i+1]) + str(res[i+2]))
            exit()

