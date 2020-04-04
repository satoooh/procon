S = input()
K = int(input())
if S[0] != "1":
    print(S[0])
else:
    ind = 0
    while S[ind] == "1" and ind < len(S) - 1:
        ind += 1
    if ind < K:
        print(S[ind])
    else:
        print("1")
