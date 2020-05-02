X = int(input())

now = 100
ans = 0
while (now < X):
    ans += 1
    now += now//100

print(ans)
