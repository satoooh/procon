# AtCoder Programming Guide for beginners (APG4b)

プログラミング教材の C++ の入門教材

## 内容 (目次)

- 基本文法
- 複雑な計算処理の書き方
- 競プロに役立つ知識
- 今まで説明していなかったこと

## 書き方 (基本形)

```cpp
#include <bits/stdc++.h>
using namespace std;  //stdという名前空間を利用

int main() {
}
```

- 同じ名前の変数は宣言できない（コンパイルエラーになる）
- 宣言と初期化が必要

## 条件式の結果と bool 型

- 条件式の結果は真のときに1、偽のとき0になる

## 文字列と文字

- `"文字列".size()` などは出来ず、一度変数に格納するか `"文字列"s.size()` のように `s` を `" "` の末尾に付ける必要がある。

## 配列

配列の受け取り方

```cpp
vector<int> vec(N);
for (int i = 0; i < N; i++) {
    cin >> vec.at(i);
}
```
