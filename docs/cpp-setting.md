# VSCode で 競技プログラミング用の C++ 環境構築（mac OS）

macOS 上での競技プログラミング用の VSCode 環境構築についてのメモ

参考: [Visual studio codeで競プロ環境構築[mac OS] - Qiita](https://qiita.com/EngTks/items/ffa2a7b4d264e7a052c6)

## 目的

AtCoder の C++ のコンパイラは Clang 系と gcc 系の２つが用意されている。ただ、 MacOS では C++ のコンパイラとして Clang 系のみ標準搭載されている。（ `/usr/bin/g++` ）今回の目的のライブラリである `stdc++.h` は gcc にのみ入っているため、 `#include <bits/>stdc++.h>` を使えるビルド環境を構築することを目的とする。

- gcc 動作環境を整え、 VSCode からコンパイルと実行を行うようにする
- ライブラリ `bits/std++.h` を使えるようにする

## 準備

まずは VSCode で必要な Extension を入れておく。

- C/C++
- Visual Studio IntelliCode
- code-runner

## gcc をインストール

```bash
$ brew install gcc
```

## path の設定

この時点で mac 上に2種類のコンパイラが同居している状態になる。ただ、この状態で g++ コマンドを打っても、 `/usr/bin/g++` （clang）の方が呼び出されてしまう。

```bash
$ which g++
/usr/bin/g++
```

gcc を呼び出すために、 `/usr/local/bin/` に g++(gcc) のシンボリックリンクを作成する。

```bash
$ ln -s /usr/local/bin/g++-9 /usr/local/bin/g++
```

こうすることで g++ コマンドで `/usr/local/bin/g++` が呼び出されるようになった。これで、先程インストールした g++-9(gcc) が実行されるようになった。

```bash
$ which g++
/usr/local/bin/g++
```

（戻したい場合は先程のシンボリックリンクを削除すれば OK ）

## コンパイル

次に code-runner を使って C++ のコンパイルを行う。code-runner では、言語ごとに実行するスクリプトを設定できる。

### code-runner の設定ファイル編集

settings.json の編集から、次の内容を入れる。

```settings.json
{
    "runner.languageMap": {
        "cpp": "/Users/[user名]/vsc_run/cpp.sh"
    }
}
```

### スクリプト作成

中身では、シェルの実行時の引数 $1 にファイル名が入るように動作するので、「hogehoge.cpp をコンパイルし、実行ファイル hogehoge を作成して実行する」という処理になる。

```cpp.sh
#!/bin/sh
file = $1
objfile = `echo $f | sed 's/\.[^\.]*$//'`

g++ -g -o $objfile $file
./$objfile
```

## #include <bits/stdc++.h> を使えるようにする

最後に `stdc++.h` を使えるようにする。

### stdc++.h の準備

gcc をインストールした時点で、 `/usr/local/` 下の奥深くに `stdc++.h` は存在する。

```bash
$ cd /usr/local/
$ find . -name "stdc++.h"
./Cellar/gcc/9.2.0_2/include/c++/9.2.0/x86_64-apple-darwin19/bits/stdc++.h
```

これをコンパイラが認識できる `/usr/local` 下に設置する。具体的には `/usr/local/include/` 下に `bits` ディレクトリを作成し、 `stdc++.h` をコピーする。

```bash
$ mkdir /usr/local/include/bits
$ cp ./Cellar/gcc/9.2.0_2/include/c++/9.2.0/x86_64-apple-darwin19/bits/stdc++.h /usr/local/include/bits/
```

この時点で `#include` をつけてコンパイルができるようになる。

ただ、 Intellisense が stdc++.h を認識できてないので、警告が出てくる。

### C/C++ Intellisense の設定

`Command + Shift + P` でコマンドパレットを開き、 `C/Cpp: Edit congigurations` を選択。

- "includePath" に "/usr/local/include/**" を追記
- "compilerPath" に "/usr/local/bin/g++"
- "cppStandard" に "c++14"
- "intelliSenseMode" に "gcc-x64"

これで終了。
