# panasonic 2020

## B

コーナーケースの処理に手間がかかる。片方の幅が1担ってしまうと、そもそも斜め移動ができなくなるという事実に気づければ OK

## C

sqrt(a) + sqrt(b) < sqrt(c)

a + b + 2 sqrt(ab) < c

2 sqrt(ab) < c - a - b

4ab < (c - a - b) ** 2 && c - a - b >= 0

## D

N = 1

```text
a
```

N = 2

```text
aa
ab
```

N = 3

```text
aaa
aab
aba
abb
abc
```

N = 4

```text
aaaa
aaab
aaba
aabb
aabc
abaa
abab
abac
abba
abbb
abbc
abca
abcb
abcc
abcd
```

という出力順的に、DFSっぽい発想で行けそうな気がする。
