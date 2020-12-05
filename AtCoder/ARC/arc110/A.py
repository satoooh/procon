import math

N = int(input())

lcm = 2
for i in range(3, N+1):
    lcm = lcm * i // math.gcd(lcm, i)
ans = lcm + 1

print(ans)
