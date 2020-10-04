N = int(input())
X = list(map(int, input().split()))

M_small = sorted(X)[N // 2 - 1]
M_large = sorted(X)[N // 2]

for xi in X:
    if xi <= M_small:
        print(M_large)
    else:
        print(M_small)
