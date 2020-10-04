# 番号nのカットラインの長さを返す関数を定義
def l(n, N, R):
    if n <= 0 or n >= N:
        return 0
    else:
        return 4 * R * ((n * (N - n)) ** 0.5) / N


R, N, M = map(int, input().split())
ans = 0
for i in range(1, N + M):
    ans += max(l(i, N, R), l(i - M, N, R))
print(ans)
