from heapq import heappush, heappop


N, K = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(A, reverse=True)

MOD = 10**9 + 7

# case1. N == K のときは答えは確定
if N == K:
    ans = 1
    for i in range(K):
        ans *= A[i]
        ans %= MOD
    print(ans)
# case2. A が全部負の数のとき、 Kが奇数ならば残念ながら答えは負になるのでなるべく絶対値を小さくする
elif max(A) < 0 and K % 2 == 1:
    ans = 1
    for i in range(K):
        ans *= A[i]
        ans %= MOD
    print(ans)
else:
    # case3. それ以外は正にできる

    # K が奇数のとき、非負要素から1つ取って偶数の場合に帰着
    # K が偶数のとき、面倒なので 2 つセットで考えて K//2 個取る問題に帰着

    if K%2 == 1:
        ans = A.pop(0)  # あらかじめ最大値を確保
        n = (K-1)//2
    else:
        ans = 1
        n = K//2

    # 絶対値の降順にソートする
    A = sorted(A, key=lambda x: abs(x), reverse=True)

    # 候補テーブルを作成
    cand = []  # 非負要素、負要素をそれぞれ絶対値の大きい順に 2 つずつ掛けたもの

    BIGINT = 10**9 + 1  # tmp 用
    tmp1 = BIGINT
    tmp2 = BIGINT

    for a in A:
        if a >= 0:
            if tmp1 == BIGINT:
                tmp1 = a
            else:
                heappush(cand, -tmp1*a)
                tmp1 = BIGINT
        else:
            if tmp2 == BIGINT:
                tmp2 = a
            else:
                heappush(cand, -tmp2*a)
                tmp2 = BIGINT

    # あとは大きい方から n 個取る
    for i in range(n):
        ans *= -heappop(cand)
        ans %= MOD
    print(ans)
