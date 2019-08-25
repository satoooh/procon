# AtCoder Beginner Contest 094

解説: Coming Soon...

## B - Toll Gates

A の中で X 未満のもの、 X より大きいものの個数を数えて比較する。

## C - Many Medians

普通に中央値を毎回計算すると TLE になってしまうので、中央値が各回ごとにどうなるかを考えてみる。
すると、中央値って sort した X について X[N // 2 - 1] か X[N // 2] しかありえなくて、どちらかは取り除く値が大きいか小さいかで決まるということが分かってくる。

## D - Binomial Coefficients

普通に計算すると TLE になってしまうので、 ai, aj にどんな数が来ればよいかを考えてみる。
まず ai には間違いなく max(a) がくればよい。このとき aj は、 ai/2 に近い値ほどよいのでこれを探せば完了。
