import collections

N = int(input())
S = [""] * N
for i in range(N):
    S[i] = input()

c = collections.Counter(S)
c_most_num = c.most_common()[0][1]
ans = []
for ci in c.most_common():
    if ci[1] == c_most_num:
        ans.append(ci[0])
ans.sort()

for a in ans:
    print(a)
