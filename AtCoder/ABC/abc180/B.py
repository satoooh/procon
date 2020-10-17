import numpy as np

N = int(input())
x = list(map(int, input().split()))

print(np.linalg.norm(x, ord=1))
print(np.linalg.norm(x, ord=2))
print(np.linalg.norm(x, ord=np.inf))
