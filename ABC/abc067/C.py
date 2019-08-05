N = int(input())
a = list(map(int, input().split()))
# 初期値
snuke = a[0]
araiguma = sum(a) - a[0]
ans = abs(snuke - araiguma)
# 更新
for i in range(1, N - 1):
    snuke += a[i]
    araiguma -= a[i]
    ans = min(ans, abs(snuke - araiguma))
# 出力
print(ans)
