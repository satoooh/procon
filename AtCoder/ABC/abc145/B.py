N = int(input())
S = input()

if N % 2 == 0:
    if S == S[: N//2] + S[: N//2]:
        print("Yes")
        exit()
print("No")
