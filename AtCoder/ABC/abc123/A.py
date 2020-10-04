# a~e,kを定義
a, b, c, d, e, k = [int(input()) for _ in range(6)]
# 条件に合わせて出力
if e - a > k:
	print(":(")
else:
	print("Yay!")
