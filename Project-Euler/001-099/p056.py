def digsum(n):
    """桁和
    """
    return sum(list(map(int, str(n))))

ans = 0

for a in range(1, 100):
    for b in range(1, 100):
        ans = max(ans, digsum(a**b))

print(ans)
