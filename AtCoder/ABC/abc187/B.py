N = int(input())
x, y = [0 for _ in range(N)], [0 for _ in range(N)]
for i in range(N):
    x[i], y[i] = map(int, input().split())

count = 0
for i in range(N-1):
    for j in range(i+1, N):
        if -1 <= (y[i] - y[j]) / (x[i] - x[j]) <= 1:
            count += 1
print(count)
