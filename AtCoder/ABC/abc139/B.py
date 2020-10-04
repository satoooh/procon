A, B = map(int, input().split())
n = 0
while 1 + n * (A - 1) < B:
    n += 1
print(n)
