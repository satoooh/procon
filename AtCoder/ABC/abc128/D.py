N, K = map(int, input().split())
*V, = map(int, input().split())
ans = 0

for l in range(K + 1):
	for r in range(K - l + 1):
		inHand = []
		if l + r > N:  # Nを超えてしまうありえない場合を処理
			break

		# inHandに左からl個、右からr個の要素を追加
		inHand = V[: l]
		inHand.extend(V[N - r:])
		tmp = sum(inHand)  # 現時点でのinHandの和をtmpとして負の要素をtmpから引いていく

		# inHand中の負の要素を消せるだけ消す
		inHand.sort()
		for i in range(min(K - l - r, l + r)):
			if inHand[i] >= 0:
				break
			tmp -= inHand[i]

		ans = max(ans, tmp)

print(ans)
