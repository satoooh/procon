N = int(input())
S = input()

diff = 0

for i in range(N):
    if S[i] == "(":
        diff += 1
    else:
        diff -= 1
    if diff < 0:
        print("No")
        exit()

if diff == 0:
    print("Yes")
else:
    print("No")
