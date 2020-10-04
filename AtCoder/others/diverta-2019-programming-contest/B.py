R, G, B, N = map(int, input().split())
ans = 0
for x in range(N // R + 1):
	for y in range(N // G + 1):
		if (N - R * x - G * y) % B == 0 and 0 <= (N - R * x - G * y) // B <= N // B:
			ans += 1
print(ans)
