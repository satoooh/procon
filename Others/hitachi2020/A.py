S = input()
for i in range(1, 6):
    if S == "hi" * i:
        print("Yes")
        exit()
print("No")
