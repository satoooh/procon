N = int(input())
S = input()

ans = 0

for i in range(10):
    if str(i) not in S:
        continue
    ind_i = S.index(str(i))
    for j in range(10):
        if str(j) not in S[ind_i+1:]:
            continue
        ind_j = S[ind_i+1:].index(str(j)) + ind_i+1
        for k in range(10):
            if str(k) in S[ind_j+1:]:
                ans += 1

print(ans)
