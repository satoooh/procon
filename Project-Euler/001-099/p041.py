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


ans = 0

for n in range(1, 10):
    s = ""
    for i in range(n):
        s += str(i+1)
    cand = ["".join(v) for v in permutations(s)]
    for ci in cand:
        if is_prime(int(ci)):
            ans = max(ans, int(ci))

print(ans)
