N, L = map(int, input().split())
S = input()
now = 1
ans = 0
for i in range(N):
    if S[i] == "+":
        now += 1
        if now > L:
            ans += 1
            now = 1
    else:
        now = max(0, now-1)
print(ans)
