def check(s):
    if s == [".###", ".#.#", ".#.#", ".#.#", ".###"]:
        return 0
    elif s == ["..#.", ".##.", "..#.", "..#.", ".###"]:
        return 1
    elif s == [".###", "...#", ".###", ".#..", ".###"]:
        return 2
    elif s == [".###", "...#", ".###", "...#", ".###"]:
        return 3
    elif s == [".#.#", ".#.#", ".###", "...#", "...#"]:
        return 4
    elif s == [".###", ".#..", ".###", "...#", ".###"]:
        return 5
    elif s == [".###", ".#..", ".###", ".#.#", ".###"]:
        return 6
    elif s == [".###", "...#", "...#", "...#", "...#"]:
        return 7
    elif s == [".###", ".#.#", ".###", ".#.#", ".###"]:
        return 8
    else:
        return 9


N = int(input())
S = [input() for _ in range(5)]

ans = ""
# 4*i ~ 4*i+3 文字を見る（0<=i<N）
for i in range(N):
    s = [S[j][4*i:4*i+4] for j in range(5)]
    ans += str(check(s))

print(ans)
