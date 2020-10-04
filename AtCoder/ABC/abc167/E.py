def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

N, M, K = map(int, input().split())
MOD = 998244353

fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % MOD)
    inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
    factinv.append((factinv[-1] * inv[-1]) % MOD)

ans = M * pow(M-1, N-1, MOD)

for k in range(1, K+1):
    res = 0
    for i in range(min(k, N-k)):
        ans += M * pow(M-1, N-k-i-1, MOD) * (cmb(N-k+i, i+1, MOD) - res)
        ans %= MOD
        res += cmb(N-k+i, i+1, MOD)

print(ans%MOD)
