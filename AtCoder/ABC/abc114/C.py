N = int(input())

q = ["3", "5", "7"]
ans = 0
while q:
    now = q.pop(0)
    if int(now) <= N:
        for c in ("3", "5", "7"):
            q.append(now + c)
        if len(set(now)) == 3:
            ans += 1

print(ans)
