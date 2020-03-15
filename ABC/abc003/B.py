N = int(input())
s = [""] * N
for i in range(N):
    s[i] = input()[::-1]
for si in sorted(s):
    print(si[::-1])
