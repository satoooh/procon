A, B = input().split()
a, b = list(map(int, [A[0], A[1], A[2]])), list(map(int, [B[0], B[1], B[2]]))
ans = []
ans.append( 100*(a[0] - b[0]) + 10*(a[1] - b[1]) + (a[2] - b[2]) )
ans.append( 100*(9 - b[0]) + 10*(a[1] - b[1]) + (a[2] - b[2]) )
ans.append( 100*(a[0] - 1) + 10*(a[1] - b[1]) + (a[2] - b[2]) )
ans.append( 100*(a[0] - b[0]) + 10*(9 - b[1]) + (a[2] - b[2]) )
ans.append( 100*(a[0] - b[0]) + 10*(a[1] - 0) + (a[2] - b[2]) )
ans.append( 100*(a[0] - b[0]) + 10*(a[1] - b[1]) + (9 - b[2]) )
ans.append( 100*(a[0] - b[0]) + 10*(a[1] - b[1]) + (a[2] - 0) )
print(max(ans))
