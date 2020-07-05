N = int(input())

ans = {"AC": 0, "WA": 0, "TLE": 0, "RE": 0}

for _ in range(N):
    s = input()
    ans[s] += 1

print(f"AC x {ans['AC']}")
print(f"WA x {ans['WA']}")
print(f"TLE x {ans['TLE']}")
print(f"RE x {ans['RE']}")
