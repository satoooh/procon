N = input()
w = list(input().split())
ans = w.count("TAKAHASHIKUN") + w.count("Takahashikun") + w.count("takahashikun")
if w[-1] == "TAKAHASHIKUN." or w[-1] == "Takahashikun." or w[-1] == "takahashikun.":
	ans += 1
print(ans)
