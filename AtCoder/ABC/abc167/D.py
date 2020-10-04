N, K = map(int, input().split())
A = list(map(int, input().split()))
l = [0 for _ in range(N)]

now = 0
l[now] = 1
count = 0
loop = [0]

while count < K:
    count += 1
    now = A[now]-1
    loop.append(now)
    if l[now] == 1:
        loop = loop[loop.index(now):-1]
        break
    else:
        l[now] = 1

if count == K:
    print(now + 1)
else:
    ans = loop[(K-count) % len(loop)]
    print(ans + 1)
