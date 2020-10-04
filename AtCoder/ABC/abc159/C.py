# a + b + c = L のとき
# max(abc) は
# abc <= ((a+b+c)/3)^3
# 等号成立条件が a = b = c よりこれは成立し
# max(abc) = (L/3)^3
L = int(input())
print((L/3)**3)
