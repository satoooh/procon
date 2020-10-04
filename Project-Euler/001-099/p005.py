"""
1~20のlcmを求めればok
"""
from math import gcd

ans = 1
N = 1
for i in range(2, 21):
    ans = ans * i // gcd(ans, i)

print(ans)
