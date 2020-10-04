# 心構えとかテクとか

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

## list の要素を空白区切りにして出力する

例えば `l = [2, 3, 4, 5, 6, 7]` のリストの要素を `2 3 4 5 6 7` のように出力したいときは

```python
l = [2, 3, 4, 5, 6, 7]
print(*l)
```

とすればよい

## lambda について

Python では lambda を使って名前を持たない関数を作ることができる。

### 基本的な使い方

次の形式で書く

```python
lambda 引数: 返り値
```

引数を複数持ってくることもできる

```python
lambda 引数, 引数, 引数: 返り値
```

これは要するに、次の表記の短縮形であることがわかる

```python
def function(引数):
    return 返り値
```

### lambda を利用するメリット

map や sort のときに、特別な動作をしたいが、わざわざ関数定義するのも面倒...というときにパパッとかける

#### ex. すでにある整数リストのそれぞれを2乗して符号はそのままにしたい

```python
l = [2, -10, 5, -3, 6, 7, -8]

# 関数を定義する場合
def function(n):
    return (n ** 2) * (1, -1)[n < 0]

l = list(map(function, l))

# lambda を使う場合
l = list(map(lambda x: (x ** 2) * (1, -1)[x < 0], l))
```

#### ex. 多重キーでソートしたい

```python
score = [["John", 33],  ["Kane", 24], ["Bob", 87], ["Tony", 74]]

print(sorted(score, key=lambda x: x[1]))
#[["Kane", 24], ["John", 33], ["Tony", 74], ["Bob", 87]]
```
