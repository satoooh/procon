import numpy as np

def pow_k(x, n):
    """
    O(log n)
    """
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K *= x
        x *= x
        n //= 2

    return K * x


A, R, N = map(int, input().split())

if (N-1)*np.log(R) > np.log(10**9/A):
    print("large")
    exit()

res = A * pow_k(R, N-1)
if res > 10**9:
    print("large")
else:
    print(res)
