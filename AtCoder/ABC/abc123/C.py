import math
# 入力値を定義
N, A, B, C, D, E = eval("int(input())," * 6)
# Nをmin(A~E)で割った商を繰り上げた分だけ、移動が余計にかかる
print(4 + math.ceil(N / min(A, B, C, D, E)))
