N, M, Q = map(int, input().split())

hsolved = [[] for _ in range(N)]  # hsolved[i] : iが解いた問題のリスト
psolved = [[] for _ in range(M)]  # psolved[i] : 問題iを解いた人のリスト

for _ in range(Q):
    s = input()
    if s[0] == "1":
        n = int(s[2:]) - 1
        score = 0
        for p in hsolved[n]:
            score += N - len(psolved[p])  # psolved[p]: 人nが解いた問題pを解いた人のリスト
        print(score)
    else:
        n, m = map(int, s[2:].split())
        n -= 1
        m -= 1
        hsolved[n].append(m)
        psolved[m].append(n)
