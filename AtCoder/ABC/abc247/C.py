N = int(input())

ans = '1'

for i in range(1, N):
    ans = ans + f' {i+1} ' + ans

print(ans)
