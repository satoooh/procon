def popcount(n):
    return bin(n).count("1")

def f(x):
    count = 0
    while x != 0:
        count += 1
        x %= popcount(x)
    return count

N = int(input())
X = "0b"+input()
intX = int(X, 2)
popcountX = X.count("1")
X_plus_mod = intX % (popcountX + 1)
X_minus_mod = intX % (popcountX - 1)

f_table = [f(i) for i in range(N)]  # 1 回やれば絶対この中に入る
print(f_table)

for i in range(N):
    if X[i+1] == "0":
        diff = pow(2, N-i-1) % (popcountX + 1)
        res = (X_plus_mod + diff) % (popcountX + 1)
    else:
        diff = -pow(2, N-i-1) % (popcountX - 1)
        res = (X_minus_mod + diff) % (popcountX - 1)
    ans = f_table[res]
    print(ans)
