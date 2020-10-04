def cmb(n, r, mod):
    if (r < 0) or (r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod

mod = 10 ** 9 + 7
N = 10 ** 6
g1 = [1, 1]  # 元
g2 = [1, 1]  # 逆元
inverse = [0, 1]  # 逆元計算用

for i in range(2, N + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)


X, Y = map(int, input().split())

if ((2 * X - Y) >= 0) and ((2 * X - Y) % 3 == 0):
    t = (2 * X - Y) // 3
else:
    print(0)
    exit()

if ((2 * Y - X) >= 0) and ((2 * Y - X) % 3 == 0):
    s = (2 * Y - X) // 3
else:
    print(0)
    exit()

print(cmb(s + t, s, mod))
