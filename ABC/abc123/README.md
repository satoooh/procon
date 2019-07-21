# AtCoder Beginner Contest 123

解説リンク: https://www.planeta.tokyo/entry/3674/

## D - Cake 123

普通にやると TLE になってしまうので、うまく計算を分けて計算量を削減してあげる必要がある。

- まずは A, B の美味しさの和だけを考えて上から K 個取り出す。
- これを D とし、 C, D の美味しさの和を考えて上から K 個取り出す。

この方針で PyPy3 なら AC がもらえる。
