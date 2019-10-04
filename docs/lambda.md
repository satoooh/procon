# Python の lambda について

Python3 の lambda (無名関数) について理解してもらう

Python では lambda を使って名前を持たない関数を作ることができる。

## 基本的な使い方

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

## lambda を利用するメリット

map や sort のときに、特別な動作をしたいが、わざわざ関数定義するのも面倒...というときにパパッとかける

### ex. すでにある整数リストのそれぞれを2乗して符号はそのままにしたい

```python
l = [2, -10, 5, -3, 6, 7, -8]

# 関数を定義する場合
def function(n):
    return (n ** 2) * (1, -1)[n < 0]

l = list(map(function, l))

# lambda を使う場合
l = list(map(lambda x: (x ** 2) * (1, -1)[x < 0], l))
```

### ex. 多重キーでソートしたい

```python
score = [["John", 33],  ["Kane", 24], ["Bob", 87], ["Tony", 74]]

print(sorted(score, key=lambda x: x[1]))
#[["Kane", 24], ["John", 33], ["Tony", 74], ["Bob", 87]]
```
