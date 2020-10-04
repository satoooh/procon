N = int(input())
s = int(str(N)[-1])

if s in (2, 4, 5, 7, 9):
    print("hon")
elif s in (0, 1, 6, 8):
    print("pon")
else:
    print("bon")
