# スーパーFizzBuzz!
for i in range(1, int(input()) + 1):
	ans = ""
	if i % 2 == 0:
		ans += "a"
	if i % 3 == 0:
		ans += "b"
	if i % 4 == 0:
		ans += "c"
	if i % 5 == 0:
		ans += "d"
	if i % 6 == 0:
		ans += "e"
	# 出力
	if ans == "":
		print(i)
	else:
		print(ans)
