N = int(input())
A = list(map(int, input().split()))

ans, cnt = 0, 0
for k in range(2, max(A)+1):
    if len([aj for aj in A if aj%k == 0]) > cnt:
        ans = k
        cnt = len([aj for aj in A if aj%k == 0])

print(ans)
