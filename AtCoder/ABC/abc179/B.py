N = int(input())
count = 0
for i in range(N):
    d1, d2 = map(int, input().split())
    if d1 == d2:
        if count == 2:
            print("Yes")
            exit()
        else:
            count += 1
    else:
        count = 0
print("No")
