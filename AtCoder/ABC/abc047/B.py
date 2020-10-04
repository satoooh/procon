W, H, N = map(int, input().split())
xl, xh = 0, W
yl, yh = 0, H
for i in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        xl = max(xl, x)
    elif a == 2:
        xh = min(xh, x)
    elif a == 3:
        yl = max(yl, y)
    else:
        yh = min(yh, y)

if xl >= xh or yl >= yh:
    print(0)
else:
    print((xh-xl) * (yh-yl))
