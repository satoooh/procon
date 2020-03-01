A = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(3):
    A[3*i], A[3*i+1], A[3*i+2] = map(int, input().split())
A_bingo = [0, 0, 0, 0, 0, 0, 0, 0, 0]

N = int(input())
for _ in range(N):
    b = int(input())
    if b in A:
        A_bingo[A.index(b)] = 1

# check
for i in range(3):
    if (A_bingo[3*i] == 1 and A_bingo[3*i+1] == 1 and A_bingo[3*i+2] == 1):
        print("Yes")
        exit()
    elif (A_bingo[i] == 1 and A_bingo[i+3] == 1 and A_bingo[i+6] == 1):
        print("Yes")
        exit()
if (A_bingo[0] == 1 and A_bingo[4] == 1 and A_bingo[8] == 1) or (A_bingo[2] == 1 and A_bingo[4] == 1 and A_bingo[6] == 1):
    print("Yes")
    exit()

print("No")
