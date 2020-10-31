A, B, C = map(int, input().split())
MOD = 998244353

# sum_a( sum_b( sum_c( a*b*c ) ) )
# = sum_a( sum_b( a*b*sum_c(c) ) )
# = sum_a( a * sum_b(b) * sum_c(c) )
# = sum_a(a) * sum_b(b) * sum_c(c)

ans = (A * (A+1) // 2) * (B * (B+1) // 2) * (C * (C+1) // 2) % MOD
print(ans)
