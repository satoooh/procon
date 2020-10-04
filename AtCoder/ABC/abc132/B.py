"""
p[i + 1]が真ん中に来るのは2通りしかないので、愚直にforループ回してカウントする
"""

n = int(input())
p = list(map(int, input().split()))
ans = 0
for i in range(n - 2):
	if p[i] < p[i + 1] < p[i + 2] or p[i + 2] < p[i + 1] < p[i]:
		ans += 1
print(ans)
