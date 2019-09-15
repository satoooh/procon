N, K, Q = map(int, input().split())
A = [int(input()) for _ in range(Q)]
cnt = [0] * N
for a in A:
    cnt[a - 1] += 1

for ai in range(N):
    if K - Q + cnt[ai] > 0:
        print("Yes")
    else:
        print("No")
