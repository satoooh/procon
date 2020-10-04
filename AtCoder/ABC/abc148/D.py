N = int(input())
a = list(map(int, input().split()))

now = 1
for ai in a:
    if ai == now:
        now += 1

if now == 1:
    print(-1)
else:
    print(N - now + 1)
