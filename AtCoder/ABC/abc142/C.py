N = int(input())
A = list(map(int, input().split()))
B = []
for i in range(N):
    B.append([A[i]])
    B[i].append(i + 1)  # 出席番号をそれぞれ追加している
B = sorted(B)  # 人数でソート
ans = []
for ai in range(N):
    ans.append(B[ai][1])  # 人数順に出席番号で出力
print(" ".join(map(str, ans)))
