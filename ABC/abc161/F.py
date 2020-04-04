# 約数を全列挙する関数
def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors

N0 = int(input())
ans = 0

# N = K^a (bK + 1) と表現できるので K は N or N-1 の約数であることが必要
K_cand = set(make_divisors(N0) + make_divisors(N0-1))

for K in K_cand:
    N = N0
    if K == 1:  # K = 1 を除外
        continue
    else:
        while N%K == 0:
            N = N // K  # 割れるだけ割る
        N = N%K  # 引けるだけ引く
        if N == 1:
            ans += 1

print(ans)
