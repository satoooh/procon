S = input()
K = int(input())
ans_s2, ans_s3 = 0, 0

# 例外処理
if len(S) == 1:
    print(K // 2)
    exit()
elif len(set(S)) == 1:
    print(len(S) * K // 2)
    exit()

S_double = S + S
for i in range(1, len(S_double)):
    if S_double[i] == S_double[i - 1]:
        S_double = S_double[: i] + "?" + S_double[i + 1:]
        ans_s2 += 1

S_triple = S + S + S
for j in range(1, len(S_triple)):
    if S_triple[j] == S_triple[j - 1]:
        S_triple = S_triple[: j] + "?" + S_triple[j + 1:]
        ans_s3 += 1

ans_increase = ans_s3 - ans_s2  #K>=3のときの増分

ans = ans_s2 + max(0, ans_increase * (K - 2))
print(ans)
