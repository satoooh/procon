# x = 10B + y と表現できるので...

A, B = map(int, input().split())
for i in range(10):
    if int((10*B + i) * 0.08) == A:
        print(10*B + i)
        exit()
print(-1)
