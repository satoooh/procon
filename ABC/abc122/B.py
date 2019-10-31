S = input()
acgt = ["A", "C", "G", "T"]
ans = 0

for i in range(len(S)):
    res = 0
    if S[i] in acgt:
        while (i < len(S)) and (S[i] in acgt):
            res += 1
            i += 1
        ans = max(ans, res)
print(ans)
