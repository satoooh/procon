from math import ceil

A, B, C, D = map(int, input().split())

cnt = ceil(C/B)

if A - D*(cnt-1) > 0:
    print("Yes")
else:
    print("No")
