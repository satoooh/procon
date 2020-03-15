N = int(input())
for X in [-int(-N/1.08), int((N+1)/1.08)]:
    if int(X * 1.08) == N:
        print(X)
        exit()
print(":(")
