"""
三角数は1, 2, 3, ... と順番に足せば得られるので、約数の個数を数える関数 divisors_cnt(n) を定義して考える
"""


def divisors_cnt(n):
	cnt = 0
	for i in range(1, int(n ** 0.5) + 1):
		if n % i == 0:
			cnt += 1
			if i != n // i:
				cnt += 1
	return cnt


i, tmp = 1, 1
while True:
	if divisors_cnt(i) > 500:
		print(i)
		exit()
	else:
		tmp += 1
		i += tmp
