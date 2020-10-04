# AtCoder Beginner Contest 108

解説: Coming Soon...

## A - Pair

1 以上 K 以下の偶数は K//2 個なので、K // 2 * (K - K // 2) が答えになる。

## B - Ruined Square

点の回転を考えれば良さそう。

```python
z3
= z2 + i * (z2 - z1)
= (x2 + y1 - y2) + i * (y2 - x1 + x2)
```

## C - Triangular Relationship

当然愚直に書いても TLE になってしまう。

```python
N, K = map(int, input().split())
ans = 0
for a in range(1, N + 1):
    for b in range(1, N + 1):
        if (a + b) % K == 0:
            for c in range(1, N + 1):
                if (b + c) % K == 0 and (c + a) % K == 0:
                    ans += 1
print(ans)
```
