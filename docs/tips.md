# 心構えとか

## バグらせたときの対応

### print デバッグ

print文を適宜入れてエラーを検証・特定する。古典的な方法。

### assert 文を使う

```python
assert [condition], [error_message]
```

具体的には次のイメージ。 `N >= 10` でエラーが起こるようにしている

```python
N = int(input())
assert N < 10, f"N={N} is too big"
print(N)

# Traceback (most recent call last):
#   File "./Main.py", line 2, in <module>
#     assert N < 100000, f"N={N} is too big"
# AssertionError: N=1000000 is too big
```
