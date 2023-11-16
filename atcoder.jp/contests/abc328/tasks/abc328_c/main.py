N, Q = map(int, input().split())
S = input()

# tmp[i]: S[0] ... S[i] まで S[:i+1] に同じ英小文字が2つ隣り合う場所が何個あるか
tmp = [0] * N
for i in range(N-1):
    if S[i] == S[i+1]:
        tmp[i+1] = tmp[i] + 1
    else:
        tmp[i+1] = tmp[i]

# tmp を使ってS[l-1:r]に同じ英小文字が2つ隣り合う場所が何個あるかを求める
for i in range(Q):
    l, r = map(int, input().split())
    ans = tmp[r-1] - tmp[l-1]
    print(ans)
