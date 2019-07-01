"""
制約から何も考えず全探索でイケる
"""

N = int(input())
*W, = map(int, input().split())
s1, s2 = 0, sum(W)
ans = sum(W)
for i in range(N):
	s1 += W[i]
	s2 -= W[i]
	ans = min(ans, abs(s1 - s2))
print(ans)
