import numpy as np
from bisect import bisect_right

N = int(input())
A, B = [0 for _ in range(N)], [0 for _ in range(N)]
for i in range(N):
    A[i], B[i] = map(int, input().split())

# もともと青木氏 sum(A) 票、高橋氏 0 票持っているとする。差は sum(A) だけある。
# 高橋氏が町 i で演説を行った場合、高橋氏の票が A[i] + B[i] 票増え、青木氏の票が A[i] 票減る。
# よって差が 2*A[i] + B[i] だけ縮む。

# 2*A[i] + B[i] の降順ソートしたリストで、その累積和が sum(A) をはじめて超える点を求めればよい。
x = sorted([2*A[i] + B[i] for i in range(N)], reverse=True)
cumsum = np.cumsum(x)

ans = bisect_right(cumsum, sum(A))
print(ans+1)
