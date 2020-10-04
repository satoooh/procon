# 昔レシート見ながら気になったことあったけど、消費税って合計に対して計算すればいいんだね

N = int(input())
x = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
	ans += x[i][0] * x[i][1]
print(int(ans * 1.05))
