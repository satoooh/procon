INF = 10 ** 9 + 7

S = input()
# dp[i][j]はうしろからi桁を13で割った余りがjであるものの個数
dp = [[0] * 13 for _ in range(len(S) + 1)]
dp[0][0] = 1
mul = 1

for i in range(len(S)):
    x = S[-(i + 1)]
    if x == "?":
        for k in range(10):
            for j in range(13):
                dp[i + 1][(mul * k + j) % 13] += dp[i][j]
                dp[i + 1][(mul * k + j) % 13] %= INF
    else:
        k = int(x)
        for j in range(13):
            dp[i + 1][(mul * k + j) % 13] += dp[i][j]
            dp[i + 1][(mul * k + j) % 13] %= INF
    mul = mul * 10 % 13  # 計算量削減のためここで13で割っている

print(dp[len(S)][5])
