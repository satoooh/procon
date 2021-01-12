N = int(input())
S = [input() for _ in range(N)]

# hoge と !hoge があれば T = hoge が不満な文字列になる
s1 = set() # !なし文字列の集合
s2 = set() # !あり文字列から最初の文字を取り除いたものの集合

for i in range(N):
    tar = S[i]
    if tar[0] == "!":
        if tar[1:] in s1:
            print(tar[1:])
            exit()
        else:
            s2.add(tar[1:])
    else:
        if S[i] in s2:
            print(tar)
            exit()
        else:
            s1.add(tar)

print("satisfiable")
