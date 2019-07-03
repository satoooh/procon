n, m = map(int, input().split())
n = n % 12
N = 30 * (n + m / 60)  # 度数法に変換
M = 6 * m  # 度数法に変換
x = abs(N - M)
print(min(x, 360 - x))
