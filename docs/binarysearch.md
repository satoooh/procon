# 最大値の最小化とかに二分探索が使える

- hoge の最大値を最小化したい
- → hoge の最大値を X 以下にできるか？
- と読み替えることができる

```python
def test(X):
    return (max(hoge) <= X)
```

みたいに判定して二分探索すれば良さそう。更新はつぎのようにできる

```python
l, r = ans_min, ans_max  # 答えの候補の min, max

while (l + 1 < r):
    mid = (l + r) // 2
    if test(mid):
        r = mid
    else:
        l = mid

ans = r
```

最小値の最大化にももちろん使える

https://betrue12.hateblo.jp/entry/2019/05/11/013403 に分かりやすく解説してあった
