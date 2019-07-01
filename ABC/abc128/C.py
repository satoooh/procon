"""
bit全探索
"""

N, M = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(M)]  # sの各要素のはじめはk
p = list(map(int, input().split()))
ans = 0

# 0をoffとして2進数でパターンを表現

for i in range(2 ** N):
	ptn = bin(i)[2:].rjust(N, "0")  # N桁の2進表現にする
	light = True  # 着目している電球が点灯していないときはこれがFalseになる
	for j in range(M):
		tmp = 0  # 着目している電球について、スイッチのonの個数をカウントする
		for n in range(1, s[j][0] + 1):
			if ptn[s[j][n] - 1] == "1":
				tmp += 1
		if tmp % 2 != p[j] % 2:
			light = False
	if light:
		ans += 1

print(ans)
