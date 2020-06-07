import numpy as np

A, R, N = map(int, input().split())

if (N-1)*np.log(R) > np.log(10**9/A):
    print("large")
    exit()

res = A * pow(R, N-1)
if res > 10**9:
    print("large")
else:
    print(res)
