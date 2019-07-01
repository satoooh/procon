"""
累積和+二分探索で時間内に解ける
"""

from bisect import bisect_left

N, K = map(int, input().split())
*a, = map(int, input().split())
sum_a = [a[0]] * N
for i in range(N - 1):
	sum_a[i + 1] = sum_a[i] + a[i + 1]
ans = N - bisect_left(sum_a, K)
for l in range(1, N):
	ans += N - bisect_left(sum_a, K + sum_a[l - 1])
print(ans)
