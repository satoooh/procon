# AtCoder Beginner Contest 135

解説: coming soon...

## A - Harmony

|A - K| = |B - K| を変形すると
A - K = B - K or K - B つまり
A = B or K = (A + B) / 2 となる。

今回問題文に A, B は相異なる整数と書いてあるので K = (A + B) / 2 であり、これが整数かどうかで IMPOSSIBLE かどうかを場合分けして考えれば OK。

## B - 0 or 1 Swap

p の index と p の値を比較し、それが異なるものをカウントしたときの個数が 2 以下のときに実現可能。

## C - City Savers

A[0] から順番に見ていく。B[0] が A[0] を上回っていた場合、余剰分が A[1] だけに作用する。（つまり、A[2]以降には作用しないことに注意）

そこで、余剰分 surplus を設定し、無駄のないように B[i] の前に surplus が A[i] に作用する用に書いてあげれば良し。
