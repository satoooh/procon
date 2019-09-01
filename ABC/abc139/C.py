N = int(input())
H = list(map(int, input().split()))
ans = [0] * N
for i in range(N - 1, 0, -1):
    if H[i] <= H[i - 1]:
        ans[i - 1] = ans[i] + 1
    else:
        ans[i - 1] = 0
print(max(ans))
