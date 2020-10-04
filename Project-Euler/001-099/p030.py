print("max_cand =", 9**5 * 5)
max_cand = 9**5 * 5

ans = 0

for i in range(2, max_cand+1):
    if i == sum([int(j)**5 for j in str(i)]):
        ans += i
        print(i)

print("ans", ans)
