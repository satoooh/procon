N = int(input())
p = list(map(int, input().split()))

cnt = 0
for i in range(N):
    if i + 1 == p[i]:
        cnt += 1

if cnt >= N - 2:
    print("YES")
else:
    print("NO")
