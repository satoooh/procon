h1, m1, h2, m2, k = map(int, input().split())
h = (h2 - h1) % 24
if m2 >= m1:
    res = h*60 + (m2 - m1)
else:
    res = (h-1)*60 + (m2 - m1 + 60)

print(res - k)
