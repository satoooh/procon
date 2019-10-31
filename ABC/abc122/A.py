b = input()
if b in ["A", "T"]:
    print(["A", "T"][["A", "T"].index(b) - 1])
else:
    print(["G", "C"][["G", "C"].index(b) - 1])
