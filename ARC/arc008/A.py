# 全部パックで買ったほうが安い場合があることに注意。

N = int(input())
q, r = divmod(N, 10)  # 割り算の商と余りはdivmod(x, y)で取得できる
print(min(100 * (q + 1), 100 * q + 15 * r))
