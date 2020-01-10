# AtCoder Beginner Contest 140

## C - Maximal Value

A の各項は、B の隣り合う 2 項についての条件式をともに満たす

たとえば `A[i + 1]` は

```python
B[i] >= max(A[i], A[i + 1])
B[i + 1] >= max(A[i + 1], A[i + 2])
```

に出てくる。これらをともに満たすように `A[i + 1]` を最大化することを考えると、 `A[i + 1] = min(B[i], B[i + 1])` となる。
