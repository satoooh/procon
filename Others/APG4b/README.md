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

## STL の関数

C++ で用意されている、関数等がまとまっているもののことを STL(Standard Template Library) という。

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
  int ans_1 = min(10, 5);  //2つの引数のうち小さいほうの値を返す

  int ans_2 = max(10, 5);  //2つの引数のうち大きいほうの値を返す

  int a = 10, b = 5;
  swap(a, b);  //2つの引数の値を交換する

  vector<int> vec = {1, 5, 3};
  reverse(vec.begin(), vec.end()); //配列の要素の並びを逆にする

  vector<int> vec = {2, 5, 2, 1};
  sort(vec.begin(), vec.end());  //配列の要素を小さい順に並び替える
}
```

## 関数の定義

関数の定義は main 関数より手前で行う。

```cpp
返り値の型 関数名(引数1の型 引数1の名前, 引数2の型 引数2の名前, ...) {
  処理
}
```

関数の返り値がないときは型に void を指定する。

処理が `return;` の行に到達した時点で関数の処理は終了する。

返り値がある関数で return 文を忘れると、どんな値が返ってくるかは決まっていない。

