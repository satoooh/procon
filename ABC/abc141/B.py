S = list(input())
if (set(S[0::2]) <= {"R", "U", "D"}) and (set(S[1::2]) <= {"L", "U", "D"}):
    print("Yes")
else:
    print("No")
