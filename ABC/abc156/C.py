N = int(input())
X = list(map(int, input().split()))
# 最小二乗法とやってること同じなので平均で最小になると考えて
P1, P2 = sum(X) // N, -(-sum(X) // N)
ans1, ans2 = 0, 0
for x in X:
    ans1 += (x - P1)**2
    ans2 += (x - P2)**2
print(min(ans1, ans2))
