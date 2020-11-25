sx, sy, gx, gy = map(int, input().split())

# (sx, sy) と (gx, -gy) を結んだ直線と x 軸の交点の x 座標

# y = (-gy-sy) / (gx - sx) * x + B
# B = sy + (gy + sy) / (gx - sx) * sx
# y = 0 として
# 0 = - (gy + sy) * x + sy * (gx - sx) + sx * (gy + sy)
x = sx + sy * (gx - sx) / (gy + sy)
print(x)
