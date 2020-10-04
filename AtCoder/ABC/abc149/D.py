N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

win = {"r":"p", "s":"r", "p":"s"}  # 勝つ手に変換
points = {"r":R, "s":S, "p":P}  # 得点換算

hands = []
ans = 0

for i in range(N):
    if i < K:
        hands.append(str(win[T[i]]))
        ans += points[str(win[T[i]])]
    elif str(win[T[i]]) == hands[-K]:
        hands.append("n")
    else:
        hands.append(str(win[T[i]]))
        ans += points[str(win[T[i]])]

print(ans)
