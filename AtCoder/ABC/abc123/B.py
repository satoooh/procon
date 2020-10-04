import math

# 定義
minutes = [int(input()) for i in range(5)]
m = [math.ceil(minutes[k] / 10) * 10 for k in range(5)]

# 最後に注文するやつを決める
last = min((minutes[l] - 1) % 10 for l in range(5))
last += 1

# 出力
print(m[0] + m[1] + m[2] + m[3] + m[4] + last - 10)
