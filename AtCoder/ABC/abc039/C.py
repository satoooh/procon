S = input()
kenban = "WBWBWWBWBWBW"
kenbans = kenban*3
doremi = {0: "Do", 2: "Re", 4: "Mi", 5: "Fa", 7: "So", 9: "La", 11: "Si"}

if S in kenbans:
    print(doremi[kenbans.index(S)])
