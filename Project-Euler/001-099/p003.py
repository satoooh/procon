"""
素数であることと因数であることに分解して考える。
素数かどうかを判定する関数 isPrime() を定義する。

探索時には、600851475143 が奇数であることから、3から順番に奇数を考えて行けばok
実行時間が 22.0s なのでヤバイ
"""


def is_prime(n):  # 素数かどうかを判定する関数isPrime()を定義
    if n == 1:
        return False

    for p in range(2, int(n ** 0.5) + 1):
        if n % p == 0:
            return False

    return True


N = 600851475143

for i in range(3, N + 1, 2):
    if N % i == 0:
        if is_prime(N // i):
            print(N // i)
            break
