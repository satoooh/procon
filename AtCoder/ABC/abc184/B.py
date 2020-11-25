N, X = map(int, input().split())
S = input()

ans = X
for i in range(N):
    if S[i] == "o":
        ans += 1
    else:
        if ans > 0:
            ans -= 1

print(ans)
