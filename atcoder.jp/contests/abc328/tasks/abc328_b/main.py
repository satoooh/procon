N = int(input())
D = list(map(int, input().split()))

ans = 0

for i in range(N):
    month = i+1
    for j in range(D[i]):
        day = j+1
        if len(set(str(month)+str(day))) == 1:
            ans += 1

print(ans)
