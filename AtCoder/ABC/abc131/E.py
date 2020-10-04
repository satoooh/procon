"""
スター作って結んでいく方針で
"""

N, K = map(int, input().split())
K0 = (N - 1) * (N - 2) // 2
if K > K0:
	print(-1)
else:
	print((N - 1) + (K0 - K))  # K0-Kがスターに追加する個数
	# まずは頂点1を中心にしてスターを作る
	for i in range(2, N + 1):
		print(1, i)
	# 追加分を出力
	cnt = 0
	for i in range(2, N):
		for j in range(i + 1, N + 1):
			cnt += 1
			if cnt > K0 - K:
				break
			print(i, j)
