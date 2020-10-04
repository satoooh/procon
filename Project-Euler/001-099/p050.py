from numpy import cumsum

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

cand = [i for i in range(3, 1000000, 2) if is_prime(i)]
cand_cum = cumsum(cand)

ans = 0

# 長さを k とする
for k in range(21, len(cand)):
    for i in range(1, len(cand)-k):
        res = cand_cum[i+k] - cand_cum[i-1]
        if res > 1000000:
            break
        if is_prime(res):
            ans = res  # 更新してれば最後に答えが得られる

print(ans)
