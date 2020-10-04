A, B = map(int, input().split())
ans = max(A, B)
ans += max(max(A, B) - 1, min(A, B))
print(ans)
