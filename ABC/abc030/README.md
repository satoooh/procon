## AtCoder Beginner Contest 030

解説: Coming Soon...

### A

大小比較しておわり

### B

針を度数法に変換して、なす角をxとして `min(x, 360 - x)` を出力しておわり

### C - 飛行機乗り

今いる時刻を更新しつつ、今の時刻に最も近い便に乗れば効率よく移動することができる。
乗る便の探し方は二分探索 `bisect_left` を採用した。

### D - へんてこ辞書

言われたとおりにコードを書くと k が大きいときに TLE になる。たとえば次のコード。

```python
N, a = map(int, input().split())
k = int(input())
b = list(map(int, input().split()))

now = a

for i in range(k):
	now = b[now - 1]

print(now)
```

そこで、これに工夫を加えてやる必要がある。
 k が莫大なとき、どこかで周期が発生するので、周期が発生するまでを記録して、周期発生以降は残った回数を周期で割ったあまりだけを考えややればよい。
具体的には次のようになる。Python3 で 108 ms で AC.

```python
N, a = map(int, input().split())
k = int(input())
b = list(map(int, input().split()))

now = a
l = []

for i in range(k):
	if now in l:
		l = l[l.index(now):]  # 周期発生部分だけ取り出す
		tmp = (k - i) % len(l)
		print(l[tmp])
		exit()
	else:
		l.append(now)
		now = b[now - 1]
	# print(l, now)

print(now)
```
