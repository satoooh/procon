x = list(map(int, input().split()))
tmp = []
for i in range(3):
	for j in range(i + 1, 4):
		for k in range(j + 1, 5):
			tmp.append(x[i] + x[j] + x[k])
print(sorted(list(set(tmp)))[-3])
