N, M = map(int, input().split())
A = list(map(int, input().split()))

B = sorted(A)[:: -1]
ans = 0

# Mがm(>=1)群にあるとしてmをもとめる
m = 1
while (m*(m+1)//2 < M):
    m += 1
print("M =", M, "は第", m, "群")

# m-1群までは普通に足す
for i in range(1, m):
    for j in range(i):
        ans += 2 * B[j]
    print(i, "群までの和は", ans)


# m群の残りを足す
group_m = sorted([B[i]+B[m-i-1] for i in range(m)])[::-1]
index = M-m*(m-1)//2
ans += sum(group_m[:index])

print(ans)
