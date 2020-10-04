# 全方向についてそれぞれ調べる

import numpy as np

numbers = np.zeros((20, 20))

data = open("./src/p011-numbers.txt")
line_index = 0
for line in data.readlines():
    numbers[line_index] = line.split()
    line_index += 1

ans = 0

# vertical
for i in range(20 - 4):
    for j in range(20):
        res = numbers[i][j] * numbers[i + 1][j] * numbers[i + 2][j] * numbers[i + 3][j]
        ans = max(ans, res)

# horizontal
for i in range(20):
    for j in range(20 - 4):
        res = numbers[i][j] * numbers[i][j + 1] * numbers[i][j + 2] * numbers[i][j + 3]
        ans = max(ans, res)

# right down
for i in range(20 - 4):
    for j in range(20 - 4):
        res = numbers[i][j] * numbers[i + 1][j + 1] * numbers[i + 2][j + 2] * numbers[i + 3][j + 3]
        ans = max(ans, res)

# left down
for i in range(3, 20):
    for j in range(20 - 4):
        res = numbers[i][j] * numbers[i - 1][j + 1] * numbers[i - 2][j + 2] * numbers[i - 3][j + 3]
        ans = max(ans, res)

print(int(ans))