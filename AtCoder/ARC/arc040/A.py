N = int(input())
points = {"TAKAHASHI": 0, "AOKI": 0}

for _ in range(N):
    S = input()
    points["TAKAHASHI"] += S.count("R")
    points["AOKI"] += S.count("B")

if points["TAKAHASHI"] == points["AOKI"]:
    print("DRAW")
elif points["TAKAHASHI"] > points["AOKI"]:
    print("TAKAHASHI")
else:
    print("AOKI")
