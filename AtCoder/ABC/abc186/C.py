N = int(input())

ans = 0
for n in range(1, N+1):
    if ("7" not in str(n)) and ("7" not in oct(n)[2:]):
        ans += 1
print(ans)
