N = list(map(int, input()[:: -1]))
print((sum(N[:: 2]) - sum(N[1:: 2])) % 11)
