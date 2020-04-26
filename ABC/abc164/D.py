from collections import Counter

S = input()

p = 2019
N = len(S)

# p は 10 と互いに素なのであんまり桁のずれは関係ないはずなので、とりあえず位は大きいのに合わせる
m = [(int(S[i]) * pow(10, N-i, p)) % p for i in range(N)]# m は各桁の mod

# m の mod 累積和をもとめる
r = [0] * N
r[0] = m[0]
for ri in range(1, N):
    r[ri] = (r[ri-1] + m[ri]) % p

# この r[i] が一致するような区間が答えになるのでこれをもとめる（0は別途対応）
c = Counter(r)

ans = 0
for ci in [cv for cv in c.values() if cv >= 2]:
    ans += ci * (ci-1) // 2

if 0 in c.keys():
    ans += c[0]

print(ans)
