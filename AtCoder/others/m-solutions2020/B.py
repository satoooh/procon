A, B, C = map(int, input().split())
K = int(input())

b = 0
while (b <= K and A >= 2**b * B):
    b += 1

if 2**b * B < 2**(K-b) * C:
    print("Yes")
else:
    print("No")
