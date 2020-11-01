import numpy as np

N = int(input())
x, y = [0 for _ in range(N)], [0 for _ in range(N)]
for i in range(N):
    x[i], y[i] = map(int, input().split())

# x の小さい順にソート
x, y = zip(*(sorted(zip(x, y))))

for i in range(N):
    px, py = x[i], y[i]
    # (px, py) を基点として同一直線状にあるか判定

    angle_list = [np.angle(complex(x[k]-px, y[k]-py)) for k in range(i+1, N)]
    if len(angle_list) != len(set(angle_list)):
        print("Yes")
        exit()

print("No")
