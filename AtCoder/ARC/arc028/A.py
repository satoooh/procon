N, A, B = map(int, input().split())
while True:
	if N <= A:
		print("Ant")
		exit()
	else:
		N -= A
		if N <= B:
			print("Bug")
			exit()
		else:
			N -= B
