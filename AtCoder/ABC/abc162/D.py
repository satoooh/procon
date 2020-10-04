N = int(input())
S = input()
ans = S.count("R") * S.count("G") * S.count("B")

for i in range(N-2):
    for d in range(1, (N-i-1)//2+1):
        if {S[i], S[i+d], S[i+2*d]} == {"R", "G", "B"}:
            ans -= 1

print(ans)
