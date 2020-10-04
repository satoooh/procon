"""
愚直に求める。初期値のxは奇数なのでansに足さなくてもok
"""

x, y = 1, 2
ans = 0
while y <= 4000000:
    if y % 2 == 0:
        ans += y
    x, y = y, x + y
print(ans)
