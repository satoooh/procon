## AtCoder Beginner Contest 121

解説リンク: まだ


### D - XOR World

XOR についての問題。ポイントは 2 つ。書こうと思ったけどこのサイトにキレイにまとまっている → [0からNまでの累積XORやAからBまでの区間XORについて - hryshtk's blog](http://hryshtk.hatenablog.com/entry/2019/03/15/0%E3%81%8B%E3%82%89N%E3%81%BE%E3%81%A7%E3%81%AE%E7%B4%AF%E7%A9%8DXOR)

#### D - 1. 累積 XOR の周期性について

次のように累積 XOR `xor(n)` を定義する。

```
xor(n) = 0 ^ 1 ^ 2 ^ ... ^ n
```

累積 XOR には周期 4 の規則性がある。

| n を 4 で割った余り | xor(n) |
| --- | --- |
| 0 | n |
| 1 | 1 |
| 2 | n + 1 |
| 3 | 0 |


#### D - 2. 区間 XOR について

次のように a から b までの区間 XOR `f(a, b)` を定義する。

```
f(a, b) = a ^ (a + 1) ^ ... ^ b
```

このとき、 `f(a, b) = f(0, a - 1) ^ f(0, b) = xor(a - 1) ^ xor(b)` が成り立つ。

これにより、区間 XOR を 2 つの累積 XOR どうしの XOR と表すことができ、累積 XOR は D - 1. で述べた周期性から簡単に求めることができる。
