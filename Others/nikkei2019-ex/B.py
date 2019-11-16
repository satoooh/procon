def ContinueCnt(A):
    datas = [_ for _ in range(max(A) + 1)]
    counts = [0] * len(datas)
    if set(datas) != set(A):
        print(0)
        exit()
    for j in range(max(A) + 1):
        counts[j] = A.count(j)
    return datas, counts

def power_func(a, n, p):
    bi = str(format(n, "b"))  # 2進表現に
    res = 1
    for i in range(len(bi)):
        res = (res * res) % p
        if bi[i] == "1":
            res = (res * a) % p
    return res

INF = 998244353

N = int(input())
D = list(map(int, input().split()))
D_datas, D_counts = ContinueCnt(D)

# first check zero
if D_counts[0] != 1:
    print(0)
    exit()

ans = 1
# check 1 ~ max(D)
for i in range(1, max(D_datas) + 1):
    ans *= power_func(D_counts[i - 1], D_counts[i], INF)
    ans %= INF

print(ans % INF)
